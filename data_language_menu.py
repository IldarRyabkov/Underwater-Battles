#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
import config as c
import numpy as np
from colors import WHITE, BUTTON_COLOR_1


class LanguageMenuData:
    def __init__(self):
        self.background = self.create_background()

    @staticmethod
    def create_background():
        bg_color_max = np.array([37., 192., 238.])
        bg_color_delta = np.array([-2, -62, -55])

        background = pg.Surface((c.SCR_W, c.SCR_H))
        for i in range(60):
            bg_color = bg_color_max + bg_color_delta * i / 60
            pg.draw.rect(background, bg_color, pg.Rect(0, i * 10, c.SCR_W, 10))

        pg.font.init()
        font = pg.font.Font(c.FONT_1, 45)
        caption = font.render('Language', True, WHITE)
        caption_x = c.SCR_W2 - caption.get_size()[0] // 2
        background.blit(caption, (caption_x, 0.3 * c.SCR_H))

        pg.draw.line(background, WHITE, (200, 120),         (c.SCR_W-200,   120),         4)
        pg.draw.line(background, WHITE, (200, c.SCR_H-120), (c.SCR_W - 200, c.SCR_H-120), 4)

        rus_flag = pg.image.load('images/russian_flag.png').convert_alpha()
        eng_flag = pg.image.load('images/english_flag.png').convert_alpha()
        background.blit(eng_flag, (c.SCR_W2 - 105, int(0.45*c.SCR_H)))
        background.blit(rus_flag, (c.SCR_W2 - 105, int(0.6*c.SCR_H)))

        return background
