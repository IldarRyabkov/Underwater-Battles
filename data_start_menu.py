#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pygame as pg

import config as c
from colors import BLUE, WHITE, COLOR_KEY


class StartMenuData:
    def __init__(self):
        self.BUBBLE_RADIUS = 11
        self.ANIMATION_TIME = 1500
        self.BUBBLES_COOLDOWN = 200
        self.background, self.caption_background = self.create_backgrounds()
        self.caption_label = None

    @staticmethod
    def create_backgrounds():
        bg_color_max = np.array([37., 192., 238.])
        bg_color_delta = np.array([-2, -62, -55])
        caption_label_color = np.array([125, 199, 240])

        background = pg.Surface((c.SCR_W, c.SCR_H))
        caption_background = pg.Surface((c.SCR_W, 160))
        caption_background.set_alpha(200)

        for i in range(60):
            bg_color = bg_color_max + bg_color_delta * i / 60
            pg.draw.rect(background, bg_color, pg.Rect(0, i * 10, c.SCR_W, 10))

            if 22 <= i <= 37:
                pg.draw.rect(caption_background, bg_color, pg.Rect(0, i * 10 - 220, c.SCR_W, 10))

        pg.draw.circle(caption_background, caption_label_color, (80, 80), 80)
        pg.draw.circle(caption_background, caption_label_color, (c.SCR_W - 80, 80), 80)
        pg.draw.rect(caption_background, caption_label_color, pg.Rect(80, 0, c.SCR_W - 160, 160))
        return background, caption_background

    def set_caption_label(self, text):
        pg.font.init()
        font = pg.font.Font(c.FONT_1, 70)
        caption = font.render(text, True, WHITE)
        self.caption_label = pg.Surface((caption.get_size()))
        self.caption_label.fill(COLOR_KEY)
        self.caption_label.set_colorkey(COLOR_KEY)
        self.caption_label.blit(caption, (0, 0))


class TriangleData:
    def __init__(self):
        self.TRIANGLE_COLOR_MIN = np.array([70., 163., 210.])
        self.TRIANGLE_COLOR_MAX = np.array([113., 186., 223.])

        self.TRIANGLE_DOTS_MIN = np.array([[-8.0, -15.0], [-8.0, 15.0], [8.0, 0.0]])
        self.TRIANGLE_DOTS_MAX = 1.75 * self.TRIANGLE_DOTS_MIN

        self.TRIANGLE_EDGE_DOTS_MIN = np.array([[-11.0, -23.0], [-11.0, 23.0], [13.0, 0.0]])
        self.TRIANGLE_EDGE_DOTS_MAX = 1.75 * self.TRIANGLE_EDGE_DOTS_MIN


class PlayLabelData:
    def __init__(self):
        self.PLAY_LABEL_COLOR_MIN = np.array([39., 146., 197.])
        self.PLAY_LABEL_COLOR_MAX = np.array([255., 255., 255.])


class StartButtonData:
    def __init__(self):
        self.K = 0.005
        self.BUTTON_A_MIN = 45
        self.BUTTON_A_MAX = 1.75 * self.BUTTON_A_MIN
        self.BUTTON_B_MIN = 35
        self.BUTTON_B_MAX = 1.75 * self.BUTTON_B_MIN

        self.BUTTON_COLOR_MIN = np.array([125., 199., 240.])
        self.BUTTON_COLOR_MAX = np.array([176., 213., 231.])
