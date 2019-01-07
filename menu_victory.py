#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
import sys

import config as c
from colors import WHITE
from bubble import Bubble
from gui_elements import PauseButton
from data_text_eng import ENG_VICTORYMENU_CAPTION, ENG_VICTORYMENU_TEXT, ENG_VICTORYMENU_BUTTON
from data_text_rus import RUS_VICTORYMENU_CAPTION, RUS_VICTORYMENU_TEXT, RUS_VICTORYMENU_BUTTON


class VictoryMenu:
    def __init__(self):
        self.caption = None
        self.text = None
        self.button = None
        self.bubbles = self.create_bubbles()

        self.bg_surface = pg.Surface((c.SCR_W, c.SCR_H))
        self.mask_surface = pg.Surface((c.SCR_W, c.SCR_H))
        self.mask_surface.set_alpha(195)

        self.running = True

        self.clock = pg.time.Clock()

    @staticmethod
    def create_bubbles():
        bubbles = [Bubble(c.SCR_W2 - 120, c.SCR_H2 - 50, 0, 0, 2),
                   Bubble(c.SCR_W2 + 120, c.SCR_H2 - 50, 0, 0, 2),
                   Bubble(c.SCR_W2,       c.SCR_H2 - 50, 0, 0, 2)]
        for bubble in bubbles:
            bubble.vel = 0

        return bubbles

    def create_caption(self, text):
        pg.font.init()
        font = pg.font.Font(c.FONT_1, 56)
        self.caption = font.render(text, True, WHITE)

    def create_text(self, text):
        pg.font.init()
        font = pg.font.Font(c.FONT_2, 30)
        self.text = font.render(text, True, WHITE)

    def create_button(self, text):
        x = int(c.SCR_W2 - 80)
        y = int(0.75 * c.SCR_H - 20)
        self.button = PauseButton(x, y, False, text)

    def set_language(self, language):
        if language == 'English':
            caption_text = ENG_VICTORYMENU_CAPTION
            text = ENG_VICTORYMENU_TEXT
            button_text = ENG_VICTORYMENU_BUTTON
        else:
            caption_text = RUS_VICTORYMENU_CAPTION
            text = RUS_VICTORYMENU_TEXT
            button_text = RUS_VICTORYMENU_BUTTON

        self.create_caption(caption_text)
        self.create_text(text)
        self.create_button(button_text)

    def handle_mouse_click(self):
        if self.button.cursor_on_button(pg.mouse.get_pos()):
            self.running = False

    def show_fps(self):
        pg.display.set_caption('FPS: ' + str(int(self.clock.get_fps()/2)))

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

    def update(self, player, bubbles, dt):
        if player.superpower.id == 6:
            player.superpower.update_body(player.body)
        player.update_body(dt)

        for bubble in bubbles:
            bubble.body.update(bubble.x, bubble.y, dt)
        for bubble in self.bubbles:
            bubble.body.update(bubble.x, bubble.y, dt)

        self.button.update_color(pg.mouse.get_pos())

    def draw_bubbles(self, screen):
        for bubble in self.bubbles:
            bubble.draw(screen)

    def draw(self, screen, draw_foreground):
        screen.blit(self.bg_surface, (0, 0))
        draw_foreground()
        screen.blit(self.mask_surface, (0, 0))
        screen.blit(self.caption, (c.SCR_W2 - self.caption.get_width()/2, 80))
        screen.blit(self.text,    (c.SCR_W2 - self.text.get_width()/2, 145))
        self.button.draw(screen)
        self.draw_bubbles(screen)

    def run(self, screen, player, bubbles, draw_foreground):
        self.running = True
        dt = 0

        while self.running:
            self.handle_events()

            self.clock.tick()

            self.update(player, bubbles, dt)

            self.draw(screen, draw_foreground)

            dt = self.clock.tick()

            pg.display.update()
            self.show_fps()
