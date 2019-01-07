#!/usr/bin/env python3
# -*- coding: utf-8 -*-1

import pygame as pg

import config as c
from gui_elements import StatusBar, PopupWindow
from colors import WHITE
from data_text_eng import ENG_TANK_NAMES, ENG_BUBBLES_TEXTS
from data_text_rus import RUS_TANK_NAMES, RUS_BUBBLES_TEXTS


class WindowHealth(PopupWindow):
    def __init__(self):
        PopupWindow.__init__(self, 115, c.SCR_H, c.SCR_W-230, 66, -0.7, 1250)
        self.max_health = 75
        self.status_bar = StatusBar(self.x+10, self.y+35, self.width-20, 20, 0, self.max_health)

        self.tank_names = None
        self.bubbles_texts = None
        self.tank_name_label = None
        self.bubbles_label = None

        pg.font.init()
        self.font = pg.font.SysFont('calibri', 19, True)

    def set_language(self, language):
        if language == 'English':
            self.tank_names = ENG_TANK_NAMES
            self.bubbles_texts = ENG_BUBBLES_TEXTS
        else:
            self.tank_names = RUS_TANK_NAMES
            self.bubbles_texts = RUS_BUBBLES_TEXTS

    def set_status_bar(self, player_state, max_health, health):
        value = max_health if player_state[0] == 5 else health

        self.status_bar.set_max_value(max_health)
        self.status_bar.set_value(value)

    def set_bubbles_label(self, health, player_state):
        if player_state[0] != 5:
            bubbles_text = str(self.max_health - health) + self.bubbles_texts[0]
        else:
            bubbles_text = self.bubbles_texts[1]
        self.bubbles_label = self.font.render(bubbles_text, True, WHITE)

    def set_tank_name_label(self, player_state):
        self.tank_name_label = self.font.render(self.tank_names[player_state], True, WHITE)

    def setup(self, player_state, max_health, health):
        self.max_health = max_health
        self.set_status_bar(player_state, max_health, health)
        self.set_tank_name_label(player_state)
        self.set_bubbles_label(health, player_state)

    def activate(self, health, player_state):
        super().activate()

        if player_state[0] != 5:
            self.status_bar.set_value(health)
            self.set_bubbles_label(health, player_state)

    def reset(self):
        super().reset()
        self.status_bar.move(self.x+10, self.y+35)

    def update(self, dt):
        super().update(dt)
        self.status_bar.move(self.x+10, self.y+35)

    def draw(self, screen):
        if self.is_on_screen():
            screen.blit(self.background, (self.x, int(self.y)))
            self.status_bar.draw(screen)

            x = c.SCR_W-self.x-15 - self.bubbles_label.get_size()[0]
            screen.blit(self.bubbles_label, (int(x), int(self.y) + 10))
            screen.blit(self.tank_name_label, (self.x + 15, int(self.y) + 10))
