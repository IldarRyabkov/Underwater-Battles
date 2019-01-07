#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from random import uniform
import pygame as pg

from data_start_menu import StartMenuData
import config as c
from gui_elements import StartButton
from bubble import Bubble

from data_text_eng import ENG_START_MENU_CAPTION, ENG_PLAY_LABEL
from data_text_rus import RUS_START_MENU_CAPTION, RUS_PLAY_LABEL


class StartMenu(StartMenuData):
    def __init__(self):
        StartMenuData.__init__(self)
        self.button = StartButton()

        self.clock = pg.time.Clock()
        self.bubbles = []
        self.time = 0
        self.is_running = True

    def set_language(self, language):
        if language == 'English':
            caption = ENG_START_MENU_CAPTION
            play_label = ENG_PLAY_LABEL
        else:
            caption = RUS_START_MENU_CAPTION
            play_label = RUS_PLAY_LABEL

        self.set_caption_label(caption)
        self.button.set_play_label(play_label)
        self.button.play_label.set_text('')

    def reset(self):
        self.button.reset()
        self.caption_background.set_alpha(200)
        self.caption_label.set_alpha(255)
        self.is_running = True
        self.bubbles = []
        self.time = 0

    def handle_mouse_click(self):
        pos = pg.mouse.get_pos()
        if self.button.cursor_on_button(pos[0], pos[1]):
            self.is_running = False

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.handle_mouse_click()

    def add_bubble(self):
        x = uniform(0, c.SCR_W)
        y = c.SCR_H + self.BUBBLE_RADIUS
        new_bubble = Bubble(x, y, 0)
        new_bubble.vel = -0.2 - uniform(0, 0.4)
        self.bubbles.append(new_bubble)

    def move_bubbles(self, dt):
        for bubble in self.bubbles:
            bubble.y += bubble.vel * dt
            bubble.body.update(bubble.x, bubble.y, dt)

    def delete_needless_bubbles(self):
        bubbles = []
        for i in range(len(self.bubbles)):
            if self.bubbles[i].y <= -self.BUBBLE_RADIUS:
                bubbles.append(i)
        bubbles.reverse()
        for i in bubbles:
            self.bubbles.pop(i)

    def update_bubbles(self, dt):
        if self.time >= self.BUBBLES_COOLDOWN:
            self.time -= self.BUBBLES_COOLDOWN
            self.add_bubble()

        self.move_bubbles(dt)
        self.delete_needless_bubbles()

    def update_caption_alpha(self, time, action_marker):
        if action_marker == -1:
            alpha_1 = int(255 * (1-time/self.ANIMATION_TIME))
            alpha_2 = int(200 * (1-time/self.ANIMATION_TIME))
        else:
            alpha_1 = int(255 * time/self.ANIMATION_TIME)
            alpha_2 = int(200 * time/self.ANIMATION_TIME)

        self.caption_label.set_alpha(alpha_1)
        self.caption_background.set_alpha(alpha_2)

    def update(self, dt, time=0, action_marker=0):
        pos = pg.mouse.get_pos()
        self.button.update(pos[0], pos[1], dt, time, action_marker)
        self.update_bubbles(dt)

        if action_marker:
            self.update_caption_alpha(time, action_marker)

    def draw_label(self, surface):
        surface.blit(self.caption_background, (0, c.SCR_H2 - 80))
        surface.blit(self.caption_label, (25, 270))

    def draw(self, surface):
        surface.blit(self.background, (0, 0))

        for bubble in self.bubbles:
            bubble.draw(surface, 0, 0)

        self.draw_label(surface)
        self.button.draw(surface)

    def show_fps(self):
        fps_value = str(int(self.clock.get_fps() / 2))
        pg.display.set_caption('FPS: ' + fps_value)

    def run_animation(self, screen, action_marker):
        self.button.adjust_pos(action_marker)

        run_time, dt = 0, 0
        while run_time <= self.ANIMATION_TIME:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()

            self.clock.tick()
            self.update(dt, run_time, action_marker)
            self.draw(screen)
            pg.display.update()

            dt = self.clock.tick()
            self.time += dt
            run_time += dt
            self.show_fps()

        self.button.adjust_pos(-action_marker)

    def run(self, screen):
        self.run_animation(screen, action_marker=1)

        dt = 0
        self.is_running = True
        while self.is_running:
            self.handle_events()

            self.clock.tick()

            self.update(dt)
            self.draw(screen)

            pg.display.update()

            dt = self.clock.tick()
            self.time += dt
            self.show_fps()

        self.run_animation(screen, action_marker=-1)
