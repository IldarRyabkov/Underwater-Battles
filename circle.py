#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
import config as c
import colors as col
from math import sin, cos, pi, copysign
from math_functions import calculate_angle


glare_colors = {col.ORANGE:         [col.ORANGE_GLARE_1,        col.ORANGE_GLARE_2],
                col.BLUE:           [col.BLUE_GLARE_1,          col.BLUE_GLARE_2],
                col.BUBBLE_COLOR:   [col.BUBBLE_GLARE_1,        col.BUBBLE_GLARE_2],
                col.BUBBLE_COLOR_2: [col.BUBBLE_GLARE_3,        col.BUBBLE_GLARE_4],
                col.DARK_RED:       [col.PLAYER_BULLET_GLARE_1, col.PLAYER_BULLET_GLARE_2],
                col.VIOLET:         [col.VIOLET_GLARE_1,        col.VIOLET_GLARE_2],
                col.RED:            [col.RED_GLARE_1,           col.RED_GLARE_2],
                col.LIGHT_ORANGE:   [col.LIGHT_ORANGE_GLARE_1,  col.LIGHT_ORANGE_GLARE_2],
                col.PURPLE:         [col.PURPLE_GLARE_1,        col.PURPLE_GLARE_2]}


class Glare:
    def __init__(self, color, alpha, size):
        self.x = 0
        self.y = 0
        self.radius = 0
        self.color = color
        self.alpha = alpha
        self.size = size

    def update(self, x, y, r, alpha):
        self.x = x + 0.65 * r * cos(self.alpha + alpha)
        self.y = y - 0.65 * r * sin(self.alpha + alpha)
        self.radius = self.size * r

    def draw(self, surface, dx, dy):
        pg.draw.circle(surface, self.color, (int(self.x-dx), int(self.y-dy)), int(self.radius))


class Circle:
    def __init__(self,
                 radius,
                 edge,
                 color,
                 dist,
                 alpha,
                 is_scaling,
                 scale_speed,
                 amplitude,
                 phase,
                 is_visible,
                 adjusts_to_target=False,
                 adjusting_dist=0,
                 adjusting_alpha=0,
                 is_swinging=False,
                 swing_alpha=0,
                 rotating=False,
                 rotation_radius=0,
                 rotation_alpha=0):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.radius_0 = radius
        self.radius = radius
        self.edge = edge
        self.color = color
        self.dist = dist
        self.alpha = alpha

        self.is_scaling = is_scaling
        if self.is_scaling:
            self.scale_speed = scale_speed
            self.T = amplitude / self.scale_speed if self.scale_speed != 0 else 0
            self.time = self.T * phase

        self.adjusts_to_target = adjusts_to_target
        if self.adjusts_to_target:
            self.adj_dist = adjusting_dist
            self.adj_alpha = adjusting_alpha
        self.adj_x = 0
        self.adj_y = 0

        self.is_swinging = is_swinging
        if self.is_swinging:
            self.swing_alpha = swing_alpha
            self.swing_vel = 0.4
            self.swing_direction = 1
            self.swing_dist_max = 65
            self.swing_dist = 0

        self.rotating = rotating
        if self.rotating:
            self.rot_alpha = rotation_alpha
            self.rot_radius = rotation_radius

        self.is_visible = is_visible

        glares_alpha = adjusting_alpha if self.adjusts_to_target else alpha
        self.glares = self.create_glares(color, glares_alpha)

    @staticmethod
    def create_glares(color, alpha):
        k = copysign(1, alpha) * pi
        b = pi if alpha else 0
        glares = []
        if color in glare_colors.keys():
            glares.append(Glare(glare_colors[color][0], b + 0.9 * k, 0.25))
            glares.append(Glare(glare_colors[color][0], b + 0.6 * k, 0.17))
            glares.append(Glare(glare_colors[color][1], b - 0.25 * k, 0.25))
            glares.append(Glare(glare_colors[color][1], b - 0.5 * k, 0.17))
        return glares

    def update_glares(self, alpha):
        r = self.radius - self.edge
        for glare in self.glares:
            glare.update(self.x, self.y, r, alpha)

    def scale_radius(self, dt):
        self.time += dt

        while self.time >= self.T:
            self.time -= self.T

        if self.time > 0.75 * self.T:
            self.radius = self.radius_0 - self.scale_speed * (self.T - self.time)
        elif self.time > 0.5 * self.T:
            self.radius = self.radius_0 - self.scale_speed * (self.time - self.T / 2)
        elif self.time > 0.25 * self.T:
            self.radius = self.radius_0 + self.scale_speed * (self.T / 2 - self.time)
        else:
            self.radius = self.radius_0 + self.scale_speed * self.time

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        for glare in self.glares:
            glare.x += dx
            glare.y += dy

    def swing(self, dt, alpha):
        dr = self.swing_vel * dt

        if self.swing_direction == 1:
            if abs(self.swing_dist + dr) >= abs(self.swing_dist_max):
                self.swing_dist = self.swing_dist_max
                self.swing_direction *= -1
            else:
                self.swing_dist += dr
        else:
            if abs(self.swing_dist) <= abs(dr):
                self.swing_dist = 0
                self.swing_direction *= -1
            else:
                self.swing_dist -= dr

        dx = self.swing_dist * cos(self.swing_alpha+alpha)
        dy = -self.swing_dist * sin(self.swing_alpha+alpha)
        self.move(dx, dy)

    def reverse_swing_params(self):
        self.swing_vel *= -1
        self.swing_dist *= -1
        self.swing_dist_max *= -1

    def rotate(self, dt):
        self.rot_alpha += 2*pi * dt/1000
        self.x += self.rot_radius * cos(self.rot_alpha)
        self.y -= self.rot_radius * sin(self.rot_alpha)

    def update_pos(self, x, y, target, beta, gamma):
        angle = self.alpha + gamma
        self.x = x + self.dist * cos(angle) + self.dx
        self.y = y - self.dist * sin(angle) + self.dy
        if self.adjusts_to_target:
            if self.dist:
                beta = calculate_angle(self.x, self.y, target[0], target[1])
            angle = self.adj_alpha + beta
            if self.adj_dist:
                self.adj_x = self.adj_dist * cos(angle)
                self.adj_y = -self.adj_dist * sin(angle)

        self.x += self.adj_x
        self.y += self.adj_y

        if self.radius >= 8:
            self.update_glares(angle)

    def update(self, x, y, dt, target=(0, 0), beta=0, gamma=0):
        if self.is_scaling:
            self.scale_radius(dt)

        self.update_pos(x, y, target, beta, gamma)

        if self.rotating:
            self.rotate(dt)

        if self.is_swinging:
            if self.adjusts_to_target:
                self.swing(dt, beta)
            else:
                self.swing(dt, gamma)

    def is_on_screen(self, dx, dy):
        return self.is_visible and -self.radius <= self.x - dx <= self.radius + c.SCR_W and \
                                   -self.radius <= self.y - dy <= self.radius + c.SCR_H

    def draw(self, surface, dx, dy):

            x, y, r = int(self.x - dx), int(self.y - dy), int(self.radius)
            if self.edge:
                pg.draw.circle(surface, col.WHITE, (x, y), r)

            pg.draw.circle(surface, self.color, (x, y), r - self.edge)

            if self.radius >= 8:
                for glare in self.glares:
                    glare.draw(surface, dx, dy)

