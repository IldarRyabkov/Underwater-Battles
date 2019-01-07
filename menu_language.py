#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
import sys

import config as c
from colors import WHITE, BUTTON_COLOR_1, BUTTON_COLOR_2, BLUE, UPG_CIRCLE_COLOR_2
from gui_elements import PauseButton
from data_language_menu import LanguageMenuData


class LanguageMenu(LanguageMenuData):
    def __init__(self):
        LanguageMenuData.__init__(self)

        self.buttons = self.create_buttons()

        self.chosen_language = None
        self.running = True

    @staticmethod
    def create_buttons():
        colors = (UPG_CIRCLE_COLOR_2, BUTTON_COLOR_2)
        return [PauseButton(c.SCR_W2 - 55, int(0.45*c.SCR_H), False, 'English', colors),
                PauseButton(c.SCR_W2 - 55, int(0.6*c.SCR_H), False, 'Русский', colors)]

    def handle_mouse_click(self):
        pos = pg.mouse.get_pos()
        for button in self.buttons:
            if button.cursor_on_button(pos):
                button.is_pressed = True
                self.running = False
                self.chosen_language = button.text
                break

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.handle_mouse_click()

    def update(self):
        pos = pg.mouse.get_pos()
        for button in self.buttons:
            button.update_color(pos)

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)

    def run(self, screen):
        screen.blit(self.background, (0, 0))

        while self.running:

            self.handle_events()
            self.update()
            self.draw(screen)

            pg.display.update()

