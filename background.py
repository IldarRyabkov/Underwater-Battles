#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
import numpy as np
from math import hypot, sqrt, cos, sin, pi

from colors import (BG_COLOR_1, BG_COLOR_2, ROOM_HIGHLIGHT_COLOR,
                    ROOM_COLOR, WHITE, COLOR_KEY, PLAYER_BG_COLOR)

import config as c


class ScreenBackground:
    def __init__(self):
        self.surface = self.create_background()

    @staticmethod
    def create_background():
        background = pg.Surface((c.SCR_W, c.SCR_H))

        gradient_color_1 = np.array(BG_COLOR_1)
        gradient_color_2 = np.array(BG_COLOR_2)
        color_delta = gradient_color_1 - gradient_color_2

        height = 2
        n = c.SCR_H // height
        for i in range(n):
            color = gradient_color_1 - color_delta * i/(n-1)
            color = color.astype(int)
            pg.draw.rect(background, color, pg.Rect(0, height * i, c.SCR_W, height))

        return background

    def draw(self, screen):
        screen.blit(self.surface, (0, 0))
# _________________________________________________________________


class RoomHighlight:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.surface = self.create_surface(radius)

    @staticmethod
    def create_surface(radius):
        diameter = 2*radius
        surface = pg.Surface((diameter, diameter), 0x00010000)
        array = pg.PixelArray(surface)

        for x in range(radius):
            for y in range(radius):
                if hypot(x - radius, y - radius) < radius:
                    array[x, y] = ROOM_HIGHLIGHT_COLOR
                    array[diameter-x-1, y] = ROOM_HIGHLIGHT_COLOR
                    array[x, diameter-y-1] = ROOM_HIGHLIGHT_COLOR
                    array[diameter-x-1, diameter-y-1] = ROOM_HIGHLIGHT_COLOR

        result = array.make_surface()
        return result

    def draw(self, surface, dx, dy):
        surface.blit(self.surface, (self.x - dx, self.y - dy))
# _________________________________________________________________


class RoomBackground:
    def __init__(self, ring_width):
        self.surfaces = self.create_background(ring_width)
        self.x = c.SCR_W2 - c.ROOM_RADIUS
        self.y = c.SCR_H2 - c.ROOM_RADIUS

    @staticmethod
    def create_room_surface(ring_width):
        radius = c.ROOM_RADIUS
        diameter = 2 * radius
        surface = pg.Surface((diameter, diameter), 0x00010000)
        array = pg.PixelArray(surface)

        for x in range(0, radius):
            for y in range(0, radius):
                dist = hypot(x - radius, y - radius)
                if radius - ring_width < dist < radius:
                    if dist > radius - 5:
                        color = WHITE
                    else:
                        k = (dist - radius + ring_width) / ring_width
                        color = (192, 226, 250, int(255 * k))

                    array[x, y] = color
                    array[diameter - x - 1, y] = color
                    array[x, diameter - y - 1] = color
                    array[diameter - x - 1, diameter - y - 1] = color

        room_surface = array.make_surface()
        return room_surface

    @staticmethod
    def create_room_background_rectangles(w):
        rectangles = []
        r = c.ROOM_RADIUS
        step = 25
        for y in range(0, w, step):
            d = sqrt(r * r - (r - y - step) * (r - y - step))
            rectangles.append(pg.Rect(r - d, y, 2 * d, step))

        for y in range(w, r, step):
            d1 = sqrt(r * r - (r - y - step) * (r - y - step))
            d2 = sqrt((r - w) * (r - w) - (r - y) * (r - y))
            rectangles.append(pg.Rect(r - d1, y, d1 - d2, step))
            rectangles.append(pg.Rect(r + d2, y, d1 - d2, step))

        for y in range(r, 2*r - w, step):
            d1 = sqrt(r * r - (r - y) * (r - y))
            d2 = sqrt((r - w) * (r - w) - (r - y - step) * (r - y - step))
            rectangles.append(pg.Rect(r - d1, y, d1 - d2, step))
            rectangles.append(pg.Rect(r + d2, y, d1 - d2, step))

        for y in range(2*r - w, 2*r, step):
            d = sqrt(r * r - (r - y) * (r - y))
            rectangles.append(pg.Rect(r - d, y, 2 * d, step))
        return rectangles

    def create_background(self, ring_width):
        parent_surface = self.create_room_surface(ring_width)
        rectangles = self.create_room_background_rectangles(ring_width)

        result = []
        for rectangle in rectangles:
            result.append(parent_surface.subsurface(rectangle))
        return result

    def draw(self, screen, dx, dy):
        for surface in self.surfaces:
            pos = surface.get_offset()
            x = self.x - int(dx) + pos[0]
            y = self.y - int(dy) + pos[1]
            screen.blit(surface, (x, y))
# _________________________________________________________________


class PlayerBackground:
    def __init__(self, radius):
        self.x = c.SCR_W2 - radius
        self.y = c.SCR_H2 - radius
        self.radius = radius
        self.bg_color = PLAYER_BG_COLOR
        self.color_key = COLOR_KEY
        self.background = None
        self.set_background(100)

    def set_background(self, radius):
        self.radius = radius
        self.x = c.SCR_W2 - radius
        self.y = c.SCR_H2 - radius
        self.background = pg.Surface((2*radius, 2*radius))
        self.background.set_colorkey(self.color_key)

    def is_visible(self, dx, dy):
        return hypot(dx, dy) > c.ROOM_RADIUS - self.radius - 15

    def draw(self, surface, dx, dy):
        if self.is_visible(dx, dy):
            self.background.fill(self.color_key)
            pg.draw.circle(self.background, WHITE,
                           (self.radius, self.radius), self.radius)
            pg.draw.circle(self.background, self.bg_color,
                           (self.radius, self.radius), self.radius-5)
            pg.draw.circle(self.background, self.color_key,
                           (self.radius-int(dx), self.radius-int(dy)), c.ROOM_RADIUS-15)
            surface.blit(self.background, (self.x, self.y))
# _________________________________________________________________


class Trail:
    def __init__(self):
        self.coords = []

    def set_coords(self, x, y, dist, alpha):
        self.coords = []
        self.coords.append((x + 0.05*dist*cos(alpha), y - 0.05*dist*sin(alpha)))
        self.coords.append((x + 0.05*dist*cos(alpha) + 60*cos(alpha+0.15*pi),
                            y - 0.05*dist*sin(alpha) - 60*sin(alpha+0.15*pi)))
        self.coords.append((x + 0.05*dist*cos(alpha) + 40*cos(alpha-0.25*pi),
                            y - 0.05*dist*sin(alpha) - 40*sin(alpha-0.25*pi)))

    def draw(self, screen, dx, dy):
        for i in range(3):
            radius = 14 if i == 0 else 10
            x = int(self.coords[i][0] - dx)
            y = int(self.coords[i][1] - dy)
            pg.draw.circle(screen, WHITE, (x, y), radius, 3)
# _________________________________________________________________


class DestinationCircle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = ROOM_COLOR

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, dx, dy):
        pg.draw.circle(screen, ROOM_COLOR, (self.x-dx, self.y-dy), 11)
        pg.draw.circle(screen, WHITE,      (self.x-dx, self.y-dy), 7)
# _________________________________________________________________


class Background:
    def __init__(self):
        self.screen_background = ScreenBackground()
        self.room_background = RoomBackground(ring_width=175)
        self.room_highlights = self.create_room_highlights()
        self.player_background = PlayerBackground(100)
        self.destination_circle = DestinationCircle()
        self.trail = Trail()

    @staticmethod
    def create_room_highlights():
        return [RoomHighlight(-70, -170, 100),
                RoomHighlight(175, -255, 55),
                RoomHighlight(650,  550, 100),
                RoomHighlight(515,  745, 55)]

    def set_player_background(self, radius):
        self.player_background.set_background(radius)

    def set_trail_pos(self, x, y, dist, alpha):
        self.trail.set_coords(x, y, dist, alpha)

    def set_destination_circle_pos(self, pos):
        self.destination_circle.set_pos(*pos)

    def draw_background(self, screen):
        self.screen_background.draw(screen)

    def draw_room_background(self, screen, dx, dy):
        self.room_background.draw(screen, dx, dy)

    def draw_player_background(self, screen, dx, dy):
        self.player_background.draw(screen, dx, dy)

    def draw_room_highlights(self, surface, dx, dy):
        for highlight in self.room_highlights:
            highlight.draw(surface, dx, dy)

    def draw_trail(self, screen, dx, dy):
        self.trail.draw(screen, dx, dy)

    def draw_destination_circle(self, surface, dx, dy):
        self.destination_circle.draw(surface, int(dx), int(dy))

    def draw_transportation(self, screen, offset_new, offset_old, time):
        self.draw_background(screen)
        self.draw_room_background(screen, *offset_new)
        self.draw_room_background(screen, *offset_old)
        self.draw_destination_circle(screen, *offset_new)
        if time >= 0.2 * c.TRANSPORTATION_TIME:
            self.draw_trail(screen, *offset_new)
        if time <= 0.25 * c.TRANSPORTATION_TIME:
            self.draw_player_background(screen, *offset_old)
        else:
            self.draw_player_background(screen, *offset_new)
