#!/usr/bin/env python3
# -*- coding: utf-8 -*-1

from random import uniform, random
from math import pi

from math_functions import calculate_angle
from circle import Circle


class Body:
    def __init__(self, body):
        self.circles = []
        self.body_angle = 0
        for params in body:
            self.circles.append(Circle(*params))
        self.randomise_body_scale()

    def randomise_body_scale(self):
        for circle in self.circles:
            if circle.is_scaling:
                circle.time += circle.T * random()

    def rotate(self, dest_angle, dt):
        if self.body_angle <= dest_angle:
            d_angle = min(0.0002*pi * dt, dest_angle - self.body_angle)
        else:
            d_angle = max(-0.0002*pi * dt, dest_angle - self.body_angle)
        self.body_angle += d_angle

        for circle in self.circles:
            circle.alpha += d_angle

    def move(self, dx, dy):
        for circle in self.circles:
            circle.move(dx, dy)

    def update(self, x, y, dt, target=(0, 0), gamma=0):
        beta = calculate_angle(x, y, target[0], target[1])
        for circle in self.circles:
            if circle.is_visible:
                circle.update(x, y, dt, target, beta, gamma)

    def draw(self, surface, dx=0, dy=0):
        for circle in self.circles:
            if circle.is_on_screen(dx, dy):
                circle.draw(surface, dx, dy)
