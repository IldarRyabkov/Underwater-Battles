#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
from math import pi
from colors import RED, DARK_RED, VIOLET, COLOR_KEY, WHITE, RED_GLARE_1


SMALL_BUL_BODY_1 = [[8, 1, DARK_RED, 0, 0, False, 0, 0, 0, True, False]]
SMALL_BUL_BODY_2 = [[8, 1, RED,      0, 0, False, 0, 0, 0, True, False]]

MEDIUM_BUL_BODY_1 = [[14, 2, DARK_RED, 0, 0, True, 0.022, 13, 0, True, False]]
MEDIUM_BUL_BODY_2 = [[14, 2, RED,      0, 0, True, 0.022, 13, 0, True, False]]

BIG_BUL_BODY_1 = [[18, 2, DARK_RED, 0, 0, True, 0.023, 13, 0,    True, False]]
BIG_BUL_BODY_2 = [[18, 2, RED,      0, 0, True, 0.023, 13, 0.25, True, False]]

BOMB_BUL_BODY_1 = [[6,  1, DARK_RED, 12, 0,      False, 0, 0, 0, True, False],
                   [6,  1, DARK_RED, 12, 2*pi/3, False, 0, 0, 0, True, False],
                   [6,  1, DARK_RED, 12, 4*pi/3, False, 0, 0, 0, True, False],
                   [12, 2, DARK_RED, 0,  0,      False, 0, 0, 0, True, False]]

BOMB_BUL_BODY_2 = [[6,  1, RED,      12, 0,      False, 0, 0, 0, True, False],
                   [6,  1, RED,      12, 2*pi/3, False, 0, 0, 0, True, False],
                   [6,  1, RED,      12, 4*pi/3, False, 0, 0, 0, True, False],
                   [12, 2, RED,      0,  0,      False, 0, 0, 0, True, False]]

STICKY_BUL_BODY = [[18, 1, VIOLET, 0, 0, False, 0, 0, 0, True, False]]

SMALL_SCALING_BUL_BODY_1 = [[9, 1, DARK_RED, 0, 0, True, 0.016, 9, 0, True, False]]
SMALL_SCALING_BUL_BODY_2 = [[9, 1, RED,      0, 0, True, 0.016, 9, 0, True, False]]

HOMING_MISSILE_BODY_1 = [[10, 1, DARK_RED, 0, 0, False, 0, 0, 0, True, True],
                         [5,  1, DARK_RED, 0, 0, False, 0, 0, 0, True, True, 12, 0.72 * pi],
                         [5,  1, DARK_RED, 0, 0, False, 0, 0, 0, True, True, 12, -0.72 * pi],
                         [4,  1, DARK_RED, 0, 0, False, 0, 0, 0, True, True, 10, pi],
                         [6,  1, DARK_RED, 0, 0, False, 0, 0, 0, True, True, 12, 0],
                         [4,  1, DARK_RED, 0, 0, False, 0, 0, 0, True, True, 18, 0]]

HOMING_MISSILE_BODY_2 = [[10, 1, RED, 0, 0, False, 0, 0, 0, True, True],
                         [5,  1, RED, 0, 0, False, 0, 0, 0, True, True, 12, 0.72 * pi],
                         [5,  1, RED, 0, 0, False, 0, 0, 0, True, True, 12, -0.72 * pi],
                         [4,  1, RED, 0, 0, False, 0, 0, 0, True, True, 10, pi],
                         [6,  1, RED, 0, 0, False, 0, 0, 0, True, True, 12, 0],
                         [4,  1, RED, 0, 0, False, 0, 0, 0, True, True, 18, 0]]

SHURIKEN_BODY = [[8, 1, DARK_RED, 0, 0, False, 0, 0, 0, True, True],
                 [5, 1, DARK_RED, 0, 0, False, 0, 0, 0, True, True, 10, pi],
                 [5, 1, DARK_RED, 0, 0, False, 0, 0, 0, True, True, 10, -0.6 * pi],
                 [5, 1, DARK_RED, 0, 0, False, 0, 0, 0, True, True, 10, -0.2 * pi],
                 [5, 1, DARK_RED, 0, 0, False, 0, 0, 0, True, True, 10, 0.2 * pi],
                 [5, 1, DARK_RED, 0, 0, False, 0, 0, 0, True, True, 10, 0.6 * pi]]
####################################################################################
SNIPER_BULLET_BODY = pg.Surface((28, 18))
rect_1 = pg.Rect(0, 0, 28, 18)
rect_2 = pg.Rect(1, 1, 26, 16)
SNIPER_BULLET_BODY.fill(COLOR_KEY)
pg.draw.ellipse(SNIPER_BULLET_BODY, WHITE, rect_1)
pg.draw.ellipse(SNIPER_BULLET_BODY, RED, rect_2)
pg.draw.circle(SNIPER_BULLET_BODY, RED_GLARE_1, (7, 7), 2)
SNIPER_BULLET_BODY.set_colorkey(COLOR_KEY)
####################################################################################
