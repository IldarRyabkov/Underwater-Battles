#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
from math import cos, sin, hypot, pi
import numpy as np
from random import uniform

import bullets as b
import config as c
from special_effects import add_effect
from data_bullets import (HOMING_MISSILE_BODY_1, BIG_BUL_BODY_1,
                          STICKY_BUL_BODY, BOMB_BUL_BODY_1)
from body import Body
from math_functions import calculate_angle


def superpower_factory(superpower_name):
    if superpower_name is None: return NoneSuperPower()
    if superpower_name == 'Armor': return Armor()
    if superpower_name == 'Bombs': return Bombs()
    if superpower_name == 'Paralysing_explosion': return ParalysingExplosion()
    if superpower_name == 'Powerful_explosion': return PowerfulExplosion()
    if superpower_name == 'Fast_teleportation': return Teleportation(350)
    if superpower_name == 'Teleportation': return Teleportation(1200)
    if superpower_name == 'Ghost': return Ghost()
    if superpower_name == 'TwoHomingMissiles': return TwoHomingMissiles()
    if superpower_name == 'ThreeHomingMissiles': return ThreeHomingMissiles()
    if superpower_name == 'FourHomingMissiles': return FourHomingMissiles()
    if superpower_name == 'ExplosionStar': return ExplosionStar()
    if superpower_name == 'Shurikens': return Shurikens()
    if superpower_name == 'StickyCannon': return StickyCannon()
    if superpower_name == 'PowerfulCannon': return PowerfulCannon()
    if superpower_name == 'StickyExplosion': return StickyExplosion()


# ----------------------------------------------------------------------------- #
class SuperPower:
    def __init__(self, cooldown_time, ID):
        self.id = ID
        self.cooldown_time = cooldown_time
        self.time = cooldown_time
        self.on = False

    def update_time(self, dt):
        self.time = min([self.time + dt, self.cooldown_time])

    def update(self, *params):
        self.update_time(params[0])
        if self.time == self.cooldown_time and self.on:
            self.activate(*params[1::])


# ----------------------------------------------------------------------------- #
class HomingMissiles(SuperPower):
    def __init__(self, ID):
        SuperPower.__init__(self, cooldown_time=2000, ID=ID)

    @staticmethod
    def get_missiles_coords(pos, health, beta):
        return []

    def activate(self, pos, bullets, health, beta=0):
        self.time = 0
        missiles_coords = self.get_missiles_coords(pos, health, beta)
        for pos in missiles_coords:
            bullets.append(b.HomingMissile(*pos, 7, -5, 0.55, Body(HOMING_MISSILE_BODY_1)))


# ----------------------------------------------------------------------------- #
class NoneSuperPower(SuperPower):
    def __init__(self):
        SuperPower.__init__(self, cooldown_time=0, ID=0)

    def update(self):
        pass


# ----------------------------------------------------------------------------- #
class Armor(SuperPower):
    def __init__(self):
        SuperPower.__init__(self, cooldown_time=1000, ID=1)

    def activate(self, armor_on, top_effects):
        armor_on[0] = True
        self.time = 0
        add_effect('Armor', top_effects, c.SCR_W2 - 100, c.SCR_H2 - 100, 100)

    def update_armor_state(self, armor_on):
        if self.time >= 0.5 * self.cooldown_time and armor_on[0]:
            armor_on[0] = False

    def update(self, dt, armor_on, top_effects):
        super().update(dt, armor_on, top_effects)
        self.update_armor_state(armor_on)


# ----------------------------------------------------------------------------- #
class Bombs(SuperPower):
    def __init__(self):
        SuperPower.__init__(self, cooldown_time=1000, ID=2)

    @staticmethod
    def get_bullet_pos(pos):
        mouse_pos = pg.mouse.get_pos()
        alpha = calculate_angle(c.SCR_W2, c.SCR_H2, *mouse_pos)
        return pos + np.array([-64*cos(alpha), 64*sin(alpha)])

    def activate(self, pos, bullets):
        self.time = 0
        bullet_pos = self.get_bullet_pos(pos)
        bullets.append(b.BombBullet(*bullet_pos, Body(BOMB_BUL_BODY_1)))


# ----------------------------------------------------------------------------- #
class ParalysingExplosion(SuperPower):
    def __init__(self):
        SuperPower.__init__(self, cooldown_time=2000, ID=3)

    @staticmethod
    def get_explosion_pos(pos):
        mouse_pos = pg.mouse.get_pos()
        alpha = calculate_angle(c.SCR_W2, c.SCR_H2, *mouse_pos)
        return pos + np.array([-47 * cos(alpha), 47 * sin(alpha)])

    def activate(self, pos, mobs, top_effects, bottom_effects, camera):
        self.time = 0
        for mob in mobs:
            if hypot(pos[0] - mob.x, pos[1] - mob.y) <= 200:
                mob.make_paralysed()
                add_effect('StarsAroundMob', top_effects, mob.x, mob.y, mob.radius)
        explosion_pos = self.get_explosion_pos(pos)
        add_effect('ParalyzingExplosion', bottom_effects, *explosion_pos)
        add_effect('Flash', top_effects)
        camera.start_shaking(250)


# ----------------------------------------------------------------------------- #
class PowerfulExplosion(SuperPower):
    def __init__(self):
        SuperPower.__init__(self, cooldown_time=2000, ID=4)

    @staticmethod
    def get_explosion_pos(pos):
        mouse_pos = pg.mouse.get_pos()
        alpha = calculate_angle(c.SCR_W2, c.SCR_H2, *mouse_pos)
        return pos + np.array([-49 * cos(alpha), 49 * sin(alpha)])

    def activate(self, pos, mobs, top_effects, bottom_effects, camera):
        coords = self.get_explosion_pos(pos)
        self.time = 0
        for mob in mobs:
            if hypot(coords[0] - mob.x, coords[1] - mob.y) <= 200:
                mob.health -= 20
                mob.change_body()
                add_effect('BulletHitLines', top_effects, mob.x, mob.y)
        add_effect('PowerfulExplosion', bottom_effects, *coords)
        add_effect('Flash', top_effects)
        camera.start_shaking(250)


# ----------------------------------------------------------------------------- #
class Teleportation(SuperPower):
    def __init__(self, cooldown):
        SuperPower.__init__(self, cooldown_time=cooldown, ID=5)

    @staticmethod
    def teleportation_offset():
        mouse_pos = pg.mouse.get_pos()
        return np.array(mouse_pos) - np.array([c.SCR_W2, c.SCR_H2])

    def activate(self, pos, top_effects, camera):
        self.time = 0
        add_effect('TeleportationFlash', top_effects, *pos)
        add_effect('Flash', top_effects)
        pos += self.teleportation_offset()
        camera.update(*pos, 0)


# ----------------------------------------------------------------------------- #
class Ghost(SuperPower):
    def __init__(self):
        SuperPower.__init__(self, cooldown_time=0, ID=6)

        self.dist = 0
        self.vel = 0.5
        self.offsets = ((0.53, -0.94 * pi),
                        (0.2,  -0.95 * pi),
                        (0.24, -0.92 * pi),
                        (0.18, 0.25 * pi),
                        (0.6,  -0.17 * pi),
                        (0.18, 0.75 * pi),
                        (0.36, -0.63 * pi),
                        (0.4,  pi),
                        (0.5,  -0.95 * pi),
                        (0.25, 0.32 * pi),
                        (0.54, -0.3 * pi),
                        (0.57, 0.34 * pi),
                        (0.7,  -0.18 * pi),
                        (0.3,  0.25 * pi),
                        (0.62, -0.43 * pi),
                        (0.45, 0.94 * pi),
                        (0.59, -0.07 * pi),
                        (0.3,  -0.3 * pi),)

    def update_body(self, body):
        beta = calculate_angle(c.SCR_W2, c.SCR_H2, *pg.mouse.get_pos())

        for i in range(1, len(body.circles)-6):
            body.circles[i].dx = self.offsets[i-1][0] * self.dist * cos(beta + self.offsets[i-1][1])
            body.circles[i].dy = -self.offsets[i-1][0] * self.dist * sin(beta + self.offsets[i-1][1])

    def update(self, dt, invisible, body):
        if self.on:
            invisible[0] = True
            self.update_body(body)
            if self.dist != 100:
                self.dist = min(self.dist + self.vel * dt, 100)

        elif self.dist:
            self.dist = max(self.dist - self.vel * dt, 0)
            self.update_body(body)
            if self.dist == 0:
                invisible[0] = False


# ----------------------------------------------------------------------------- #
class TwoHomingMissiles(HomingMissiles):
    def __init__(self):
        HomingMissiles.__init__(self, ID=7)

    @staticmethod
    def get_missiles_coords(pos, health, beta):
        beta = calculate_angle(c.SCR_W2, c.SCR_H2, *pg.mouse.get_pos())
        pos_0 = pos + np.array([65 * cos(beta + 0.43*pi), -65 * sin(beta + 0.43*pi)])
        pos_1 = pos + np.array([65 * cos(beta - 0.43*pi), -65 * sin(beta - 0.43*pi)])
        return pos_0, pos_1


# ----------------------------------------------------------------------------- #
class ThreeHomingMissiles(HomingMissiles):
    def __init__(self):
        HomingMissiles.__init__(self, ID=8)

    @staticmethod
    def get_missiles_coords(pos, health, beta):
        beta = calculate_angle(c.SCR_W2, c.SCR_H2, *pg.mouse.get_pos())
        pos_0 = pos + np.array([66 * cos(beta + 0.88*pi), -66 * sin(beta + 0.88*pi)])
        pos_1 = pos + np.array([66 * cos(beta - 0.88*pi), -66 * sin(beta - 0.88*pi)])
        pos_2 = pos + np.array([63 * cos(beta),           -63 * sin(beta)])
        return [pos_0, pos_1, pos_2]


# ----------------------------------------------------------------------------- #
class ExplosionStar(SuperPower):
    def __init__(self):
        SuperPower.__init__(self, cooldown_time=2000, ID=9)

    def activate(self, pos, bullets):
        self.time = 0
        beta = calculate_angle(c.SCR_W2, c.SCR_H2, *pg.mouse.get_pos())
        coords = pos + np.array([51 * cos(beta), -51 * sin(beta)])
        bullets.append(b.FrangibleBullet(*coords, beta, Body(BIG_BUL_BODY_1)))


# ----------------------------------------------------------------------------- #
class Shurikens(SuperPower):
    def __init__(self):
        SuperPower.__init__(self, cooldown_time=333, ID=10)

    def update(self, dt, pos, shurikens):
        self.time = min(self.cooldown_time, self.time + dt)
        if len(shurikens) < 5 and self.time == self.cooldown_time:
            shurikens.append(b.Shuriken(*pos, uniform(0, 2*pi)))
            self.time = 0


# ----------------------------------------------------------------------------- #
class FourHomingMissiles(HomingMissiles):
    def __init__(self):
        super().__init__(ID=11)

    @staticmethod
    def get_missiles_coords(pos, health, beta):
        pos_0 = pos + np.array([71 * cos(beta + 0.55 * pi), -71 * sin(beta + 0.55 * pi)])
        pos_1 = pos + np.array([71 * cos(beta - 0.55 * pi), -71 * sin(beta - 0.55 * pi)])
        pos_2 = pos + np.array([92 * cos(beta + 0.8 * pi),  -92 * sin(beta + 0.8 * pi)])
        pos_3 = pos + np.array([92 * cos(beta - 0.8 * pi),  -92 * sin(beta - 0.8 * pi)])
        return [pos_0, pos_1, pos_2, pos_3]


# ----------------------------------------------------------------------------- #
class StickyCannon(SuperPower):
    def __init__(self):
        SuperPower.__init__(self, cooldown_time=300, ID=12)

    def activate(self, x, y, gamma, target, bullets):
        self.time -= self.cooldown_time
        xo, yo = x + 80 * cos(gamma), y - 80 * sin(gamma)
        angle = calculate_angle(xo, yo, *target)
        pos = (xo + 34 * cos(angle), yo - 34 * sin(angle))
        bullets.append(b.RegularBullet(*pos, 0, 0.7, angle, Body(STICKY_BUL_BODY)))


# ----------------------------------------------------------------------------- #
class PowerfulCannon(SuperPower):
    def __init__(self):
        super().__init__(cooldown_time=1500, ID=13)

    def activate(self, x, y, target, bullets):
        self.time -= self.cooldown_time
        angle = calculate_angle(x, y, *target)
        pos = (x + 120 * cos(angle), y - 120 * sin(angle))
        bullets.append(b.ExplodingBullet(*pos, angle))


# ----------------------------------------------------------------------------- #
class StickyExplosion(SuperPower):
    def __init__(self):
        super().__init__(cooldown_time=1750, ID=14)

    def activate(self, x, y, bullets):
        self.time -= self.cooldown_time
        for i in range(36):
            angle = i * pi/18
            bullets.append(b.RegularBullet(x, y, 0, 0.7, angle, Body(STICKY_BUL_BODY)))
