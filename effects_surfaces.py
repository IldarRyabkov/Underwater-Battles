#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pygame as pg
from math import hypot


#############################################################################
radius = 200
d = 2 * radius
edge_0 = radius - 5
edge_1 = radius - 15
edge_2 = radius - 55
edge_3 = radius - 65
edge_4 = radius - 75

PARALYZING_EXPLOSION_SURFACE = pg.Surface((d, d), 0x00010000)
arr = pg.PixelArray(PARALYZING_EXPLOSION_SURFACE)

for x in range(0, radius):
    for y in range(0, radius):
        dist = hypot(x - radius, y - radius)
        if edge_0 < dist <= radius:
            alpha = int((radius-dist)/5 * 255)
        elif edge_1 < dist <= edge_0:
            alpha = int((dist-edge_1)/10 * 255)
        elif edge_2 < dist <= edge_1:
            alpha = int((edge_1-dist)/40 * 127)
        elif edge_3 < dist <= edge_2:
            alpha = int(127 + (edge_2-dist)/10 * 128)
        elif edge_4 < dist <= edge_3:
            alpha = int((dist-edge_4)/10 * 255)
        elif dist <= edge_4:
            alpha = int((edge_4-dist)/125 * 255)
        else:
            alpha = 0

        color = (255, 255, 255, alpha)
        arr[x, y] = color
        arr[d-1 - x, y] = color
        arr[x, d-1 - y] = color
        arr[d-1 - x, d-1 - y] = color

PARALYZING_EXPLOSION_SURFACE = arr.make_surface()
############################################################################
radius = 200
d = 2 * radius
edge_0 = radius - 5
edge_1 = radius - 10
edge_2 = radius - 15
edge_3 = radius - 30
edge_4 = radius - 40
edge_5 = radius - 50

POWERFUL_EXPLOSION_SURFACE = pg.Surface((d, d), 0x00010000)
arr = pg.PixelArray(POWERFUL_EXPLOSION_SURFACE)

pink = np.array([211, 200, 201])
white = np.array([255, 255, 255])
color_delta = white - pink
for x in range(0, radius):
    for y in range(0, radius):
        dist = hypot(x - radius, y - radius)
        if edge_0 < dist <= radius:
            alpha = int((radius-dist)/5 * 220)
            color = (255, 255, 255, alpha)

        elif edge_1 < dist <= edge_0:
            color = white - color_delta * (edge_0-dist)/5
            color = (int(color[0]), int(color[1]), int(color[2]), 220)

        elif edge_2 < dist <= edge_1:
            alpha = int((dist-edge_2)/5 * 220)
            color = (211, 200, 201, alpha)

        elif edge_3 < dist <= edge_2:
            alpha = int((edge_2-dist)/15 * 230)
            color = (211, 200, 201, alpha)

        elif edge_4 < dist <= edge_3:
            color = white - color_delta * (dist-edge_4)/10
            color = (int(color[0]), int(color[1]), int(color[2]), 240)

        elif edge_5 < dist <= edge_4:
            color = white - color_delta * (edge_4-dist)/10
            color = (int(color[0]), int(color[1]), int(color[2]), 255)

        elif dist <= edge_5:
            alpha = int(110 + dist/150 * 145)
            color = (211, 192, 191, alpha)

        else:
            color = (255, 255, 255, 0)

        arr[x, y] = color
        arr[d-1 - x, y] = color
        arr[x, d-1 - y] = color
        arr[d-1 - x, d-1 - y] = color

POWERFUL_EXPLOSION_SURFACE = arr.make_surface()
############################################################################
radius = 100
d = 2 * radius
edge_0 = 80
edge_1 = 75
edge_3 = 25

TELEPORTATION_SURFACE = pg.Surface((d, d), 0x00010000)
arr = pg.PixelArray(TELEPORTATION_SURFACE)

for x in range(0, radius):
    for y in range(0, radius):
        dist = hypot(x - radius, y - radius)
        if edge_0 < dist <= radius:
            alpha = int((radius - dist)/20 * 155)
        elif edge_1 < dist <= edge_0:
            alpha = int(155 + (edge_0 - dist)/5 * 100)
        elif edge_3 < dist <= edge_1:
            alpha = int((dist - edge_3)/50 * 255)
        else:
            alpha = 0

        color = (255, 255, 255, alpha)
        arr[x, y] = color
        arr[d-1 - x, y] = color
        arr[x, d-1 - y] = color
        arr[d-1 - x, d-1 - y] = color

TELEPORTATION_SURFACE = arr.make_surface()
############################################################################
