#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame as pg

import config as c
import data_text_rus as rus
import data_text_eng as eng

from colors import WHITE, PAUSEMENU_PLAYER_BG
from gui_elements import PauseButton, ExitButton, SideButton, TextBox
from game_map import GameMap
from body import Body
from data_statswindow_player import PLAYER_BODIES


class StatsWindow:
    def __init__(self):
        self.captions = []

        self.tank_data = None
        self.tank_name = None
        self.tank_desc = None

        self.player_bodies = PLAYER_BODIES
        self.tank_body = None

    def set_captions(self, language):
        pg.font.init()
        font_1 = pg.font.SysFont('Arial', 35, True)
        font_2 = pg.font.SysFont('Arial', 28, True)
        if language == 'English':
            captions = eng.ENG_STATSWINDOW_CAPTIONS
        else:
            captions = rus.RUS_STATSWINDOW_CAPTIONS

        self.captions.append(font_1.render(captions[0], True, WHITE))
        self.captions.append(font_2.render(captions[1], True, WHITE))
        self.captions.append(font_2.render(captions[2], True, WHITE))

    def set_tank_data(self, language):
        if language == 'English':
            self.tank_data = eng.ENG_UPGRADE_TEXT
        else:
            self.tank_data = rus.RUS_UPGRADE_TEXT

    def set_language(self, language):
        self.set_captions(language)
        self.set_tank_data(language)

    def setup_tank_name(self, player_state):
        pg.font.init()
        font = pg.font.SysFont('Arial', 26, True)
        self.tank_name = font.render(self.tank_data[player_state][0], True, WHITE)

    def setup_tank_desc(self, player_state):
        self.tank_desc = (TextBox(self.tank_data[player_state][3], c.FONT_2, 20, False, WHITE, (120, 205), False),
                          TextBox(self.tank_data[player_state][1], 'Arial',  22, True,  WHITE, (120, 410), False),
                          TextBox(self.tank_data[player_state][2], 'Arial',  22, True,  WHITE, (430, 410), False),
                          TextBox(self.tank_data[player_state][4], c.FONT_2, 20, False, WHITE, (120, 463), False),
                          TextBox(self.tank_data[player_state][5], c.FONT_2, 20, False, WHITE, (430, 463), False))

    def setup(self, player_state):
        self.setup_tank_name(player_state)
        self.setup_tank_desc(player_state)
        self.tank_body = Body(self.player_bodies[player_state])

    def update(self, dt):
        self.tank_body.update(595, 260, dt, (605, 260))

    def draw_captions(self, screen):
        screen.blit(self.captions[0], (320, 110))
        screen.blit(self.captions[1], (120, 370))
        screen.blit(self.captions[2], (430, 370))

    def draw_tank_name(self, screen):
        screen.blit(self.tank_name, (120, 170))

    def draw_tank_desc(self, screen):
        for text in self.tank_desc:
            text.draw(screen)

    @staticmethod
    def draw_player_background(screen):
        pg.draw.circle(screen, WHITE, (595, 260), 93)
        pg.draw.circle(screen, PAUSEMENU_PLAYER_BG, (595, 260), 89)

    def draw(self, screen):
        self.draw_captions(screen)
        self.draw_tank_name(screen)
        self.draw_tank_desc(screen)
        self.draw_player_background(screen)
        self.tank_body.draw(screen)


class MapWindow:
    def __init__(self):
        self.caption = None
        self.game_map = GameMap()

    def set_caption(self, language):
        pg.font.init()
        font = pg.font.SysFont('Arial', 35, True)
        if language == 'English':
            text = eng.ENG_MAPWINDOW_CAPTION
        else:
            text = rus.RUS_MAPWINDOW_CAPTION
        self.caption = font.render(text, True, WHITE)

    def reset_data(self):
        self.game_map.reset()

    def update(self, dt):
        self.game_map.update(dt)

    def draw(self, screen):
        screen.blit(self.caption, (365, 110))
        self.game_map.draw(screen)


class OptionsWindow:
    def __init__(self):
        self.caption = None
        self.label_1 = None
        self.label_2 = None

        self.buttons = ()

        self.music_on = True
        self.sound_on = True

    def set_labels(self, caption, label_1, label_2):
        pg.font.init()
        font = pg.font.SysFont('Arial', 35, True)
        self.caption = font.render(caption, True, WHITE)
        self.label_1 = font.render(label_1, True, WHITE)
        self.label_2 = font.render(label_2, True, WHITE)

    def set_buttons(self, buttons_texts):
        self.buttons = (PauseButton(130, 210, True, buttons_texts[0]),
                        PauseButton(350, 210, False, buttons_texts[1]),
                        PauseButton(130, 320, True, buttons_texts[0]),
                        PauseButton(350, 320, False, buttons_texts[1]),
                        PauseButton(590, 520, False, buttons_texts[2]))

    def initialise_objects(self, language):
        if language == 'English':
            caption = eng.ENG_OPTIONSWINDOW_CAPTION
            label_1 = eng.ENG_OPTIONSWINDOW_LABEL_1
            label_2 = eng.ENG_OPTIONSWINDOW_LABEL_2
            buttons_texts = eng.ENG_OPTIONSWINDOW_BUTTONS_TEXTS
        else:
            caption = rus.RUS_OPTIONSWINDOW_CAPTION
            label_1 = rus.RUS_OPTIONSWINDOW_LABEL_1
            label_2 = rus.RUS_OPTIONSWINDOW_LABEL_2
            buttons_texts = rus.RUS_OPTIONSWINDOW_BUTTONS_TEXTS

        self.set_labels(caption, label_1, label_2)
        self.set_buttons(buttons_texts)

    def handle_mouse_click(self, pos, sound_player):
        if (self.buttons[0].cursor_on_button(pos) and not self.buttons[0].is_pressed) or \
                (self.buttons[1].cursor_on_button(pos) and not self.buttons[1].is_pressed):
            self.buttons[0].is_pressed = not self.buttons[0].is_pressed
            self.buttons[1].is_pressed = not self.buttons[1].is_pressed

        elif (self.buttons[2].cursor_on_button(pos) and not self.buttons[2].is_pressed) or \
                (self.buttons[3].cursor_on_button(pos) and not self.buttons[3].is_pressed):
            self.buttons[2].is_pressed = not self.buttons[2].is_pressed
            self.buttons[3].is_pressed = not self.buttons[3].is_pressed

        elif self.buttons[4].cursor_on_button(pos):
            return False, False

        sound_player.update_data(self.buttons[0].is_pressed,
                                 self.buttons[2].is_pressed)
        return True, True

    def update(self, pos):
        for button in self.buttons:
            button.update_color(pos)

    def draw(self, screen):
        screen.blit(self.caption, (350, 110))
        screen.blit(self.label_1, (135, 165))
        screen.blit(self.label_2, (135, 275))

        for button in self.buttons:
            button.draw(screen)


class PauseMenu:
    def __init__(self):
        self.caption = None

        self.exit_button = None
        self.stats_button = None
        self.map_button = None
        self.options_button = None

        self.bg_surface = pg.Surface((c.SCR_W, c.SCR_H))

        self.mask_surfaces = None
        self.mask_surfaces_coords = None
        self.create_mask_surfaces()

        self.stats_window = StatsWindow()
        self.map_window = MapWindow()
        self.options_window = OptionsWindow()

        self.current_window = 3

        self.is_running = True
        self.game_is_running = True

        self.clock = pg.time.Clock()

    def create_mask_surfaces(self):
        self.mask_surfaces = (pg.Surface((100, c.SCR_H)),
                              pg.Surface((670, 100)),
                              pg.Surface((30, c.SCR_H)),
                              pg.Surface((670, 100)),
                              pg.Surface((670, 475)))

        for i in range(len(self.mask_surfaces)):
            alpha = 175 if i != 4 else 213
            self.mask_surfaces[i].set_alpha(alpha)

        self.mask_surfaces_coords = ((0, 0), (100, 0), (770, 0), (100, 575), (100, 100))

    def reset(self):
        self.map_window.reset_data()
        self.stats_window.setup((0, 0))

    def create_caption(self, text):
        pg.font.init()
        font = pg.font.Font(c.FONT_1, 35)
        self.caption = font.render(text, True, WHITE)

    def create_buttons(self, stats_button_name, map_button_name, options_button_name):
        self.exit_button = ExitButton()
        self.stats_button = SideButton(40, 100, stats_button_name, False)
        self.map_button = SideButton(40, 220, map_button_name, False)
        self.options_button = SideButton(40, 340, options_button_name, True)

    def initialise_objects(self, language):
        if language == 'English':
            caption = eng.ENG_PAUSEMENU_CAPTION
            stats_button_name = eng.ENG_STATSBUTTON_NAME
            map_button_name = eng.ENG_MAPBUTTON_NAME
            options_button_name = eng.ENG_OPTIONSBUTTON_NAME
        else:
            caption = rus.RUS_PAUSEMENU_CAPTION
            stats_button_name = rus.RUS_STATSBUTTON_NAME
            map_button_name = rus.RUS_MAPBUTTON_NAME
            options_button_name = rus.RUS_OPTIONSBUTTON_NAME

        self.create_caption(caption)
        self.create_buttons(stats_button_name, map_button_name, options_button_name)

    def set_language(self, language):
        self.initialise_objects(language)
        self.stats_window.set_language(language)
        self.map_window.set_caption(language)
        self.options_window.initialise_objects(language)

    def show_fps(self):
        pg.display.set_caption('FPS: ' + str(int(self.clock.get_fps()/2)))

    def handle_mouse_click(self, sound_player):
        pos = pg.mouse.get_pos()

        if self.exit_button.cursor_on_button(pos):
            self.is_running = False
            self.exit_button.color = self.exit_button.colors[0]

        elif self.stats_button.is_chosen(pos):
            self.stats_button.set_pressed()
            self.map_button.set_unpressed()
            self.options_button.set_unpressed()
            self.current_window = 1

        elif self.map_button.is_chosen(pos):
            self.map_button.set_pressed()
            self.stats_button.set_unpressed()
            self.options_button.set_unpressed()
            self.current_window = 2

        elif self.options_button.is_chosen(pos):
            self.options_button.set_pressed()
            self.stats_button.set_unpressed()
            self.map_button.set_unpressed()
            self.current_window = 3

        elif self.current_window == 3:
            self.is_running, self.game_is_running = self.options_window.handle_mouse_click(pos, sound_player)

    def handle_events(self, sound_player):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_p:
                    self.is_running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.handle_mouse_click(sound_player)

    def update(self, dt, player, bubbles, mobs):
        if player.superpower.id == 6:
            player.superpower.update_body(player.body)
        player.update_body(dt)

        for mob in mobs:
            mob.update_body(dt, (player.x, player.y))

        for bubble in bubbles:
            bubble.body.update(bubble.x, bubble.y, dt)

        pos = pg.mouse.get_pos()
        if self.current_window == 1:
            self.stats_window.update(dt)
        elif self.current_window == 2:
            self.map_window.update(dt)
        elif self.current_window == 3:
            self.options_window.update(pos)

        self.exit_button.update_color(pos)

    def draw_mask_surfaces(self, screen):
        for i in range(len(self.mask_surfaces)):
            screen.blit(self.mask_surfaces[i], self.mask_surfaces_coords[i])

    def draw(self, screen, draw_foreground):
        screen.blit(self.bg_surface, (0, 0))
        draw_foreground()
        self.draw_mask_surfaces(screen)
        screen.blit(self.caption, (c.SCR_W2-70, 25))

        if self.current_window == 1:
            self.stats_window.draw(screen)
        elif self.current_window == 2:
            self.map_window.draw(screen)
        elif self.current_window == 3:
            self.options_window.draw(screen)

        self.stats_button.draw(screen)
        self.map_button.draw(screen)
        self.options_button.draw(screen)
        self.exit_button.draw(screen)

    def run(self, screen, player, bubbles, mobs, draw_foreground, sound_player):
        self.is_running = True
        self.game_is_running = True

        dt = 0
        while self.is_running:
            self.handle_events(sound_player)

            self.clock.tick()

            self.update(dt, player, bubbles, mobs)

            self.draw(screen, draw_foreground)

            dt = self.clock.tick()

            pg.display.update()
            self.show_fps()
