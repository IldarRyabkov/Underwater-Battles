#!/usr/bin/env python3
# -*- coding: utf-8 -*-1

import pygame as pg
import config as c
from gui_elements import StatusBar, PopupWindow

from data_text_eng import ENG_WINDOW_COOLDOWN_LABELS
from data_text_rus import RUS_WINDOW_COOLDOWN_LABELS


class WindowCooldown(PopupWindow):
    def __init__(self):
        PopupWindow.__init__(self, c.SCR_W-165, -60, 155, 60, 0.7, 1000)
        self.cooldown_1 = 300
        self.cooldown_2 = 0

        self.status_bar_1 = StatusBar(self.x+35, self.y+7, self.width-45, 20, 0, self.cooldown_1)
        self.status_bar_2 = StatusBar(self.x+35, self.y+33, self.width-45, 20, 0, self.cooldown_2)

        self.label_1 = None
        self.label_2 = None

    def set_labels(self, language):
        if language == 'English':
            texts = ENG_WINDOW_COOLDOWN_LABELS
        else:
            texts = RUS_WINDOW_COOLDOWN_LABELS

        pg.font.init()
        font = pg.font.SysFont('Arial', 16, True)

        self.label_1 = font.render(texts[0], True, (255, 255, 255))
        self.label_2 = font.render(texts[1], True, (255, 255, 255))

    def setup(self, cooldown_1, cooldown_2):
        self.status_bar_1.set_max_value(cooldown_1)
        self.status_bar_1.set_value(0)
        self.status_bar_2.set_max_value(cooldown_2)
        self.status_bar_2.set_value(0)

    def reset(self):
        super().reset()
        self.status_bar_1.move(self.x+35, self.y+7)
        self.status_bar_2.move(self.x+35, self.y+33)

    def update(self, player, dt):
        on_superpower = player.superpower.on and player.superpower.id not in [0, 6, 10]
        on_gun = player.is_shooting and not player.invisible[0]

        if on_gun or on_superpower:
            self.activate()
        super().update(dt)

        if on_gun or 0 < self.status_bar_1.value <= self.status_bar_1.max_value:
            if self.status_bar_1.value != self.status_bar_1.max_value:
                self.status_bar_1.add_value(dt)
            else:
                self.status_bar_1.set_value(0)

        if on_superpower or 0 < self.status_bar_2.value <= self.status_bar_2.max_value:
            if self.status_bar_2.value != self.status_bar_2.max_value:
                self.status_bar_2.add_value(dt)
            else:
                self.status_bar_2.set_value(0)

        self.status_bar_1.move(self.x+35, self.y+7)
        self.status_bar_2.move(self.x+35, self.y+33)

    def draw(self, screen):
        if self.is_on_screen():
            screen.blit(self.background, (self.x, int(self.y)))
            screen.blit(self.label_1, (self.x+10, int(self.y)+9))
            screen.blit(self.label_2, (self.x+10, int(self.y)+35))
            self.status_bar_1.draw(screen)
            self.status_bar_2.draw(screen)
