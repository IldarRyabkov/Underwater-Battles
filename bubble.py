#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import uniform
from math import hypot, cos, sin

from body import Body
from math_functions import calculate_angle, circle_collidepoint
import config as c
import data_bubble as data


class Bubble:
    def __init__(self, x, y, alpha, gravity_r=0, type_marker=0):
        self.x = x
        self.y = y
        self.radius = data.BUBBLE_RADIUS[type_marker]
        self.health = data.BUBBLE_HEALTH[type_marker]
        self.vel = uniform(0.7, 1.7) * data.BUBBLE_MAX_VEL
        self.max_vel = data.BUBBLE_MAX_VEL
        self.acc = data.BUBBLE_ACC
        self.alpha = alpha
        self.gravity_r = gravity_r
        self.in_player_gravity = False

        self.body = Body(data.BUBBLE_BODY[type_marker])
        self.body.randomise_body_scale()

    def is_on_screen(self, dx, dy):
        if -self.radius <= self.x-dx <= c.SCR_W+self.radius and \
           -self.radius <= self.y-dy <= c.SCR_H+self.radius:
            return True
        return False

    def is_outside(self):
        return not circle_collidepoint(c.SCR_W2, c.SCR_H2, c.ROOM_RADIUS, self.x, self.y)

    def check_player_pos(self, player_x, player_y):
        if hypot(self.x-player_x, self.y-player_y) <= self.gravity_r:
            self.in_player_gravity = True
            self.acc = data.BUBBLE_ACC
        else:
            self.in_player_gravity = False

    def maximize_vel(self):
        self.vel = 2 * data.BUBBLE_MAX_VEL

    def go_to_player(self, x, y, dt):
        self.alpha = calculate_angle(self.x, self.y, x, y)

        dr = self.vel * dt + self.acc * dt*dt / 2
        dist = hypot(self.x-x, self.y-y)
        if dr > dist:
            self.x = x
            self.y = y
        else:
            self.x += dr * cos(self.alpha)
            self.y -= dr * sin(self.alpha)

        self.vel += self.acc * dt
        if self.vel >= self.max_vel:
            self.vel = self.max_vel
            self.acc = 0

    def slow_down(self, dt):
        self.acc = -data.BUBBLE_ACC
        dr = self.vel * dt + self.acc * dt*dt / 2
        self.x += dr * cos(self.alpha)
        self.y -= dr * sin(self.alpha)

        dv = self.acc * dt
        if self.vel * (self.vel + dv) < 0:
            self.vel = 0
            self.acc = 0
        else:
            self.vel += dv

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.body.move(dx, dy)

    def update(self, x, y, dt):
        if self.vel or self.is_on_screen(x-c.SCR_W2, y-c.SCR_H2):
            self.check_player_pos(x, y)
            if self.in_player_gravity:
                self.go_to_player(x, y, dt)
            elif self.vel:
                self.slow_down(dt)

            self.body.update(self.x, self.y, dt)

    def draw(self, surface, dx=0, dy=0):
        if self.is_on_screen(dx, dy):
            self.body.draw(surface, dx, dy)
