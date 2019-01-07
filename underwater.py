#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
from math import hypot, sqrt, pi
from collections import defaultdict
import numpy as np

from player import Player
from camera import Camera
from sound_player import SoundPlayer
from gui import Gui
from room import Room
from background import Background
from level_generator import LevelGenerator
from math_functions import calculate_angle
from special_effects import add_effect

import config as c
from data_cursor import CURSOR


class Underwater:
    def __init__(self):
        self.is_running = True
        self.transportation = False
        self.dt = 0
        self.language = None
        #self.screen = pygame.display.set_mode((c.SCR_W, c.SCR_H), pygame.FULLSCREEN |
        #                                      pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.screen = pygame.display.set_mode((c.SCR_W, c.SCR_H))
        self.sound_player = SoundPlayer()
        self.clock = pygame.time.Clock()
        self.level_generator = LevelGenerator()
        self.room = Room()
        self.player = None
        self.camera = Camera()
        self.background = Background()
        self.gui = Gui()
        self.key_handlers = defaultdict(list)

    def reset_data(self):
        self.is_running = True
        self.transportation = False
        self.level_generator.reset()
        self.room.reset(new_game=True)
        self.room.setup_text(self.level_generator.get_room_text())
        self.player = Player()
        self.key_handlers = defaultdict(list)
        self.setup_key_handlers()
        self.background.set_player_background(self.player.bg_radius)
        self.gui.reset(self.player)

    def show_fps(self):
        pygame.display.set_caption('FPS: ' + str(int(self.clock.get_fps()/2)))

    def handler(self, e_type, key):
        if e_type == pygame.KEYDOWN:
            if key == pygame.K_p:
                if not self.transportation:
                    self.run_pause_menu()
            elif key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def setup_key_handlers(self):
        self.key_handlers[pygame.K_a].append(self.player.handler)
        self.key_handlers[pygame.K_d].append(self.player.handler)
        self.key_handlers[pygame.K_w].append(self.player.handler)
        self.key_handlers[pygame.K_s].append(self.player.handler)
        self.key_handlers[1].append(self.player.handler)
        self.key_handlers[pygame.K_SPACE].append(self.player.handler)
        self.key_handlers[pygame.K_p].append(self.handler)
        self.key_handlers[pygame.K_ESCAPE].append(self.handler)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                for handler in self.key_handlers[event.key]:
                    handler(event.type, event.key)
            elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]:
                for handler in self.key_handlers[event.button]:
                    handler(event.type, event.button)

    def handle_bubble_eating(self):
        self.sound_player.reset()

        eaten_bubbles = []
        index = 0
        for b in self.room.bubbles:
            if self.player.collide_bubble(b.x, b.y):
                self.player.health += b.health
                self.player.change_body()
                self.gui.window_health.activate(self.player.health, self.player.state)
                eaten_bubbles.append(index)
                self.sound_player.play_sound('bubble_death')
            index += 1

        eaten_bubbles.reverse()
        for index in eaten_bubbles:
            self.room.bubbles.pop(index)

        if self.player.is_ready_to_upgrade():
            self.upgrade_player()

    def downgrade_player(self):
        self.player.downgrade()
        self.gui.handle_player_state_change(self.player)
        self.background.set_player_background(self.player.bg_radius)
        self.room.setup_gravity(self.player.bg_radius)

    def upgrade_player(self):
        if self.player.in_latest_state():
            self.gui.upgrade_menu.run(self.player.get_next_states(), self.screen)
            self.clock.tick()
            self.player.upgrade(1, self.gui.upgrade_menu.chosen_state)
        else:
            self.player.upgrade(0)

        self.gui.handle_player_state_change(self.player)
        self.background.set_player_background(self.player.bg_radius)
        self.room.setup_gravity(self.player.bg_radius)

    def handle_mob_injure(self, mob, bullet):
        """
        Method updates bullet's hit-flag, updates mob's state according to damage,
        Adds a hit-effect to the list of effects and plays an appropriate sound.

        """
        bullet.hit_the_target = True

        mob.handle_injure(bullet.damage)

        add_effect(bullet.hit_effect, self.room.top_effects, bullet.x, bullet.y)

        if bullet.exploding:
            self.room.handle_bullet_explosion(bullet.x, bullet.y)
            self.camera.start_shaking(250)

        if mob.health > 0:
            self.sound_player.play_sound('player_bullet_hit')
        else:
            self.sound_player.play_sound('mob_death')

    def handle_mobs_collisions(self):
        """
        Handles collisions between objects:
            mobs and player's bullets;
            mobs and player's shurikens;
            mobs and player's homing bullets;
            mobs' homing bullets and player's bullets.

        """
        self.sound_player.reset()

        for b in self.player.bullets:
            for mob in self.room.mobs:
                if mob.collide_bullet(b.x, b.y) and mob.health > 0:
                    self.handle_mob_injure(mob, b)
                    break

            if not b.hit_the_target:
                for h_b in self.room.homing_bullets:
                    if h_b.collide_bullet(b.x, b.y) and h_b.health > 0:
                        self.handle_mob_injure(h_b, b)
                        break

        for s in self.player.shurikens:
            for mob in self.room.mobs:
                if mob.collide_bullet(s.x, s.y) and mob.health > 0:
                    self.handle_mob_injure(mob, s)
                    break

        for b in self.player.homing_bullets:
            for mob in self.room.mobs:
                if mob.collide_bullet(b.x, b.y) and mob.health > 0:
                    self.handle_mob_injure(mob, b)
                    break

    def handle_player_injure(self, bullet):
        """
        Method updates bullet's hit-flag, updates player's state according to damage,
        Adds a hit-effect to the list of effects and plays an appropriate sound.

        """
        bullet.hit_the_target = True

        self.player.handle_injure(bullet.damage)

        add_effect(bullet.hit_effect, self.room.top_effects, bullet.x, bullet.y)

        if not self.player.armor_on[0]:
            self.sound_player.play_sound('player_injure')

    def handle_player_collisions(self):
        """
        Handles collisions between objects:
            player and mobs' bullets;
            player and mobs' homing bullets.
            player's homing bullets and mobs' bullets.

        If player's health becomes <= 0, calls a 'downgrade_player' method.

        """
        self.sound_player.reset()

        for b in self.room.bullets:
            if not self.player.invisible[0] and self.player.collide_bullet(b.x, b.y):
                self.handle_player_injure(b)
                break

            if not b.hit_the_target:
                for h_b in self.player.homing_bullets:
                    if h_b.collide_bullet(b.x, b.y) and h_b.health > 0:
                        self.handle_mob_injure(h_b, b)
                        break

        for b in self.room.homing_bullets:
            if not self.player.invisible[0] and self.player.collide_bullet(b.x, b.y):
                self.handle_player_injure(b)
                break

        if self.player.health < 0:
            self.downgrade_player()

    def handle_collisions(self):
        self.handle_mobs_collisions()
        self.handle_player_collisions()

    def update_transportation(self, dt):
        """ Update all objects during transportation. """
        self.player.move(self.player.vel_x * dt, self.player.vel_y * dt)
        self.player.update_superpower(dt, self.room.mobs, self.room.top_effects,
                                      self.room.bottom_effects, self.camera,
                                      transportation=True)
        self.player.update_body(dt)
        self.player.update_shurikens(dt, self.room.mobs)
        self.camera.update(*self.player.pos, dt)
        self.room.set_screen_rect(self.player.pos)
        self.room.update_new_mobs(*self.player.pos, dt)
        self.gui.update_popup_windows(self.player, dt)

    def draw_transportation(self, time, dx, dy):
        """ Draw all objects during transportation. """
        offset_new = self.camera.offset
        offset_old = (self.camera.dx - dx, self.camera.dy - dy)

        self.background.draw_transportation(self.screen, offset_new, offset_old, time)

        if self.room.boss_in_room:
            self.room.draw_boss_skeleton(self.screen, *offset_new, new_room=True)
        self.room.draw_text(self.screen, *offset_new)
        self.room.draw_bubbles(self.screen, *offset_new)
        self.player.draw(self.screen, *offset_new)
        self.room.draw_mobs(self.screen, *offset_new)
        self.room.draw_new_mobs(self.screen, *offset_new)
        self.room.draw_bullets(self.screen, *offset_new)

        self.background.draw_room_highlights(self.screen, *offset_new)
        self.background.draw_room_highlights(self.screen, *offset_old)

        self.gui.window_health.draw(self.screen)
        self.gui.window_cooldown.draw(self.screen)

    def run_transportation(self, dx, dy):
        time, dt = 0, 0
        while time < c.TRANSPORTATION_TIME and self.is_running:
            self.handle_events()
            self.clock.tick()

            self.update_transportation(dt)

            self.draw_transportation(time, dx, dy)

            pygame.display.update()

            dt = self.clock.tick()
            time += dt
            self.show_fps()

    def get_offset_and_destination(self, direction):
        """
        Method returns offset of all objects in previous room
        and the player's destination during transportation.

        """
        radius = c.ROOM_RADIUS - self.player.radius - 150

        if direction == 'UP':
            offset = (0, c.DIST_BETWEEN_ROOMS)
            destination = np.array([c.SCR_W2, c.SCR_H2 + radius])
        elif direction == 'DOWN':
            offset = (0, -c.DIST_BETWEEN_ROOMS)
            destination = np.array([c.SCR_W2, c.SCR_H2 - radius])
        elif direction == 'LEFT':
            offset = (c.DIST_BETWEEN_ROOMS, 0)
            destination = np.array([c.SCR_W2 + radius, c.SCR_H2])
        else:
            offset = (-c.DIST_BETWEEN_ROOMS, 0)
            destination = np.array([c.SCR_W2 - radius, c.SCR_H2])

        return offset, destination

    def transport_player(self, direction):
        self.transportation = True

        self.level_generator.update(self.room.encode_mobs(self.room.mobs), direction,
                                    self.player.state[0], self.player.health)
        self.level_generator.setup_game_map(self.gui.pause_menu.map_window.game_map)
        self.level_generator.setup_room(self.room)

        offset, destination = self.get_offset_and_destination(direction)
        self.room.move_objects(offset)
        self.player.move(*offset)
        self.camera.stop_shaking()
        self.camera.update(*self.player.pos, 0)

        distance = hypot(*(self.player.pos - destination))
        player_vel = distance / c.TRANSPORTATION_TIME
        alpha = calculate_angle(*self.player.pos, *destination)

        self.player.set_transportation_vel(alpha, player_vel)
        self.player.clear_bullets()

        self.background.set_trail_pos(*self.player.pos, distance, alpha)
        self.background.set_destination_circle_pos(destination)

        self.run_transportation(*offset)

        self.room.reset()
        self.player.stop()
        self.clock.tick()
        self.transportation = False

    def get_direction(self, offset):
        """
        :param offset: player's offset relative to the center of the room
        :return: direction of transportation
        """
        if -1 / sqrt(2) <= self.camera.dx / offset <= 1 / sqrt(2):
            direction = 'UP' if self.camera.dy < 0 else 'DOWN'
        else:
            direction = 'RIGHT' if self.camera.dx > 0 else 'LEFT'
        return direction

    def analyse_player_pos(self):
        """Checks if player is outside the room.
        If yes, determines the direction of transportation
        and transports player to the next room.

        """
        offset = hypot(*self.camera.offset)
        if offset > c.ROOM_RADIUS:
            direction = self.get_direction(offset)
            self.transport_player(direction)

    def update(self):
        self.handle_bubble_eating()
        self.handle_collisions()
        self.player.update(self.dt, self.room.mobs, self.room.top_effects,
                           self.room.bottom_effects, self.camera, self.sound_player)
        self.camera.update(*self.player.pos, self.dt)

        self.room.update(self.player.pos,  self.dt)
        if self.room.game_is_over():
            self.is_running = False
            self.run_victory_menu()
        else:
            self.gui.update_popup_windows(self.player, self.dt)
            self.analyse_player_pos()

    def draw_background(self, surface):
        self.background.draw_background(surface)
        self.background.draw_room_background(surface, *self.camera.offset)
        self.background.draw_player_background(surface, *self.camera.offset)
        if self.room.boss_in_room:
            self.room.draw_boss_skeleton(surface, *self.camera.offset)
        self.room.draw_text(surface, *self.camera.offset)
        self.room.draw_bottom_effects(surface, *self.camera.offset)

    def draw_foreground(self):
        self.room.draw_bubbles(self.screen, *self.camera.offset)
        self.player.draw(self.screen, *self.camera.offset)
        self.room.draw_mobs(self.screen, *self.camera.offset)
        self.room.draw_bullets(self.screen, *self.camera.offset)
        self.room.draw_top_effects(self.screen, *self.camera.offset)
        self.background.draw_room_highlights(self.screen, *self.camera.offset)
        self.gui.window_health.draw(self.screen)
        self.gui.window_cooldown.draw(self.screen)

    def draw(self):
        self.draw_background(self.screen)
        self.draw_foreground()

    def run_language_menu(self):
        self.gui.language_menu.run(self.screen)

        self.gui.set_language()
        self.language = self.gui.language_menu.chosen_language
        self.level_generator.set_language(self.language)

    def run_start_menu(self):
        self.reset_data()
        self.gui.start_menu.run(self.screen)
        self.clock.tick()

    def run_pause_menu(self):
        self.draw_background(self.gui.pause_menu.bg_surface)
        self.gui.pause_menu.run(self.screen, self.player, self.room.bubbles,
                                self.room.mobs, self.draw_foreground, self.sound_player)
        self.is_running = self.gui.pause_menu.game_is_running
        self.clock.tick()

    def run_victory_menu(self):
        self.draw_background(self.gui.victory_menu.bg_surface)
        self.gui.victory_menu.run(self.screen, self.player,
                                  self.room.bubbles, self.draw_foreground)
        self.is_running = False
        self.clock.tick()

    def run_game(self):
        while self.is_running:
            self.handle_events()
            self.clock.tick()
            self.update()
            self.draw()
            pygame.display.update()
            self.dt = self.clock.tick()
            self.show_fps()

    def run(self):
        self.run_language_menu()

        while True:
            self.sound_player.play_music(1)
            self.run_start_menu()

            self.sound_player.play_music(2)
            self.run_game()


def main():
    pygame.mixer.pre_init(44100, 16, 2, 1024)
    pygame.init()
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP,
                              pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])
    cursor = pygame.cursors.compile(CURSOR, black='.', white='X')
    pygame.mouse.set_cursor((32, 32), (0, 0), *cursor)

    Underwater().run()


if __name__ == '__main__':
    main()
