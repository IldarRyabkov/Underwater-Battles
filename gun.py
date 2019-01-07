#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi, sin, cos, hypot

import data_bullets as b
from math_functions import calculate_angle
from bullets import RegularBullet, BombBullet, EllipticBullet
from body import Body


def bullets_factory(name):
    if name == 'SmallBullet_1': return b.SMALL_BUL_BODY_1
    if name == 'SmallBullet_2': return b.SMALL_BUL_BODY_2
    if name == 'MediumBullet_1': return b.MEDIUM_BUL_BODY_1
    if name == 'MediumBullet_2': return b.MEDIUM_BUL_BODY_2
    if name == 'BigBullet_1': return b.BIG_BUL_BODY_1
    if name == 'BigBullet_2': return b.BIG_BUL_BODY_2
    if name == 'StickyBullet': return b.STICKY_BUL_BODY
    if name == 'BombBullet_1': return b.BOMB_BUL_BODY_1
    if name == 'BombBullet_2': return b.BOMB_BUL_BODY_2
    if name == 'SmallScalingBullet_1': return b.SMALL_SCALING_BUL_BODY_1
    if name == 'SmallScalingBullet_2': return b.SMALL_SCALING_BUL_BODY_2
    if name == 'SniperBullet': return b.SNIPER_BULLET_BODY
    if name == 'HomingMissile_1': return b.HOMING_MISSILE_BODY_1
    if name == 'HomingMissile_2': return b.HOMING_MISSILE_BODY_2


# ----------------------------------------------------------------------------- #
class Gun:
    """ A parent class for all gun classes. """
    def __init__(self, radius, bul_vel, bul_dmg, bul_name, cooldown_time, time):
        self.radius = radius
        self.bul_vel = bul_vel
        self.bul_dmg = bul_dmg
        self.bul_body = bullets_factory(bul_name)
        self.cooldown_time = cooldown_time
        self.time = time
        self.automatic = False
        self.is_aiming = True
        self.shooting_homing_bullets = False

    def get_reference_point(self, x, y, angle):
        xo = x + self.radius * cos(angle)
        yo = y - self.radius * sin(angle)
        return xo, yo

    def generate_bullets(self, x, y, target, gamma):
        """ Returns list of generated bullets. """
        return []

    def append_bullets(self, x, y, target, bullets, gamma=0):
        """
        Appends new bullets to the given list of bullets.
        :param x: x-coord of mob
        :param y: y_coord of mob
        :param target: target coords
        :param bullets: list of bullets
        :param gamma: mob's body angle

        """
        if self.time >= 0:
            self.time -= self.cooldown_time
            bullets.extend(self.generate_bullets(x, y, target, gamma))

    def update_time(self, dt):
        """
        Update the time counter. Time = 0 means
        that gun is recharged and ready to shoot.

        """
        self.time = min([self.time + dt, 0])


# ----------------------------------------------------------------------------- #
class GunSingle(Gun):
    """ A gun that fires one regular bullet at a time. """
    def __init__(self, radius, bul_vel, bul_dmg, bul_type, cooldown_time, time):
        super().__init__(radius, bul_vel, bul_dmg, bul_type, cooldown_time, time)

    def generate_bullets(self, x, y, target, gamma):
        angle = calculate_angle(x, y, *target)
        coords = self.get_reference_point(x, y, angle)

        return [RegularBullet(*coords, self.bul_dmg, self.bul_vel, angle, Body(self.bul_body))]


# ----------------------------------------------------------------------------- #
class GunAutomatic(GunSingle):
    """ A gun that can shoot bullets automatically. """
    def __init__(self, radius, bul_vel, bul_dmg, bul_type,
                 cooldown_time, time, cooldown_time_auto):

        super().__init__(radius, bul_vel, bul_dmg, bul_type, cooldown_time, time)

        self.automatic = True
        self.time_auto = 0
        self.cooldown_time_auto = cooldown_time_auto

    @staticmethod
    def generate_bullets_auto(x, y, target, gamma):
        return []

    def append_bullets_auto(self, x, y, mobs, bullets, gamma=0):
        if self.time_auto >= 0:
            self.time_auto -= self.cooldown_time_auto
            mob = -1
            distance = 9001
            for i in range(len(mobs)):
                d = hypot(x - mobs[i].x, y - mobs[i].y)
                if d < distance:
                    distance = d
                    mob = i
            target = [mobs[mob].x, mobs[mob].y]
            bullets.extend(self.generate_bullets_auto(x, y, target, gamma))

    def update_time(self, dt):
        super().update_time(dt)
        self.time_auto = min([self.time_auto+dt, 0])


# ----------------------------------------------------------------------------- #
class GunPeaceful:
    """ A gun that shoots no bullets. """
    def __init__(self):
        self.shooting_homing_bullets = False

    def append_bullets(self, x, y, target, bullets, gamma=0):
        pass

    def update_time(self, dt):
        pass
