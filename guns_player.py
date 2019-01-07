#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi, sin, cos, hypot

from gun import Gun, GunSingle, GunAutomatic
from math_functions import calculate_angle
from data_bullets import SMALL_BUL_BODY_1, BIG_BUL_BODY_1
from bullets import RegularBullet, EllipticBullet
from body import Body


def guns_factory(name):
    if name == 'Gun00': return Gun00()
    if name == 'Gun10': return Gun10()
    if name == 'Gun11': return Gun11()
    if name == 'Gun12': return Gun12()
    if name == 'Gun20': return Gun20()
    if name == 'Gun21': return Gun21()
    if name == 'Gun22': return Gun22()
    if name == 'Gun23': return Gun23()
    if name == 'Gun30': return Gun30()
    if name == 'Gun31': return Gun31()
    if name == 'Gun32': return Gun32()
    if name == 'Gun33': return Gun33()
    if name == 'Gun34': return Gun34()
    if name == 'Gun35': return Gun35()
    if name == 'Gun40': return Gun40()
    if name == 'Gun41': return Gun41()
    if name == 'Gun42': return Gun42()
    if name == 'Gun43': return Gun43()
    if name == 'Gun44': return Gun44()
    if name == 'Gun45': return Gun45()
    if name == 'Gun50': return Gun50()
    if name == 'Gun51': return Gun51()
    if name == 'Gun52': return Gun52()
    if name == 'Gun53': return Gun53()
    if name == 'Gun54': return Gun54()
    if name == 'Gun55': return Gun55()


# ----------------------------------------------------------------------------- #
class Gun00(GunSingle):
    def __init__(self):
        super().__init__(16, 1, -1, 'SmallBullet_1', 300, 0)


# ----------------------------------------------------------------------------- #
class Gun10(GunSingle):
    def __init__(self):
        super().__init__(16, 1, -1, 'SmallBullet_1', 75, 0)


# ----------------------------------------------------------------------------- #
class Gun11(Gun):
    def __init__(self):
        super().__init__(16, 1, -1, 'SmallBullet_1', 150, 0)

    def generate_bullets(self, x, y, target, gamma):
        angle = calculate_angle(x, y, *target)
        xo, yo = self.get_reference_point(x, y, angle)
        pos_0 = xo + 6 * sin(angle), yo + 6 * cos(angle)
        pos_1 = xo - 6 * sin(angle), yo - 6 * cos(angle)

        return [RegularBullet(*pos_0, self.bul_dmg, self.bul_vel, angle, Body(self.bul_body)),
                RegularBullet(*pos_1, self.bul_dmg, self.bul_vel, angle, Body(self.bul_body))]


# ----------------------------------------------------------------------------- #
class Gun12(GunSingle):
    def __init__(self):
        super().__init__(16, 0.75, -5, 'BigBullet_1', 300, 0)


# ----------------------------------------------------------------------------- #
class Gun20(Gun):
    def __init__(self):
        super().__init__(16, 1, -1, 'SmallBullet_1', 125, 0)

    def generate_bullets(self, x, y, target, gamma):
        angle = calculate_angle(x, y, *target)
        xo, yo = self.get_reference_point(x, y, angle)
        pos_0 = (xo, yo)
        pos_1 = (xo + 15 * sin(angle - 0.17*pi), yo + 15 * cos(angle - 0.17*pi))
        pos_2 = (xo - 15 * sin(angle + 0.17*pi), yo - 15 * cos(angle + 0.17*pi))

        return [RegularBullet(*pos_0, self.bul_dmg, self.bul_vel, angle,             Body(self.bul_body)),
                RegularBullet(*pos_1, self.bul_dmg, self.bul_vel, angle - 0.17 * pi, Body(self.bul_body)),
                RegularBullet(*pos_2, self.bul_dmg, self.bul_vel, angle + 0.17 * pi, Body(self.bul_body))]


# ----------------------------------------------------------------------------- #
class Gun21(Gun):
    def __init__(self):
        super().__init__(45, 1, -1, 'SmallBullet_1', 150, 0)

    def generate_bullets(self, x, y, target, gamma):
        angle = calculate_angle(x, y, *target)
        xo, yo = self.get_reference_point(x, y, angle)
        pos_0 = (xo, yo)
        pos_1 = (xo + 14 * sin(angle), yo + 14 * cos(angle))
        pos_2 = (xo - 14 * sin(angle), yo - 14 * cos(angle))

        return [RegularBullet(*pos_0, self.bul_dmg, self.bul_vel, angle, Body(self.bul_body)),
                RegularBullet(*pos_1, self.bul_dmg, self.bul_vel, angle, Body(self.bul_body)),
                RegularBullet(*pos_2, self.bul_dmg, self.bul_vel, angle, Body(self.bul_body))]


# ----------------------------------------------------------------------------- #
class Gun22(Gun21):
    def __init__(self):
        super().__init__()


# ----------------------------------------------------------------------------- #
class Gun23(Gun):
    def __init__(self):
        super().__init__(45, 1, -1, 'SmallBullet_1', 150, 0)

    def generate_bullets(self, x, y, target, gamma):
        angle = calculate_angle(x, y, *target)
        xo, yo = self.get_reference_point(x, y, angle)
        sina, cosa = sin(angle), cos(angle)
        coords = [(xo, yo),
                  (xo + 14*sina,          yo + 14*cosa),
                  (xo - 14*sina,          yo - 14*cosa),
                  (xo + 28*sina - 4*cosa, yo + 28*cosa + 4*sina),
                  (xo - 28*sina - 4*cosa, yo - 28*cosa + 4*sina)]

        bullets = []
        for pos in coords:
            bullets.append(RegularBullet(*pos, self.bul_dmg, self.bul_vel, angle, Body(self.bul_body)))
        return bullets


# ----------------------------------------------------------------------------- #
class Gun30(GunSingle):
    def __init__(self):
        super().__init__(10, 1.35, -10, 'SniperBullet', 350, 0)

    def generate_bullets(self, x, y, target, gamma):
        angle = calculate_angle(x, y, *target)
        xo, yo = self.get_reference_point(x, y, angle)
        return [EllipticBullet(xo, yo, self.bul_dmg, self.bul_vel, angle, self.bul_body)]


# ----------------------------------------------------------------------------- #
class Gun31(GunSingle):
    def __init__(self):
        super().__init__(20, 1, -2, 'SmallBullet_1', 75, 0)


# ----------------------------------------------------------------------------- #
class Gun32(Gun):
    def __init__(self):
        super().__init__(35, 1, -1, 'SmallBullet_1', 150, 0)

    @staticmethod
    def get_bullets_angles(angle):
        return angle, angle - 0.075*pi, angle + 0.075*pi, angle - 0.15*pi, angle + 0.15*pi

    @staticmethod
    def get_bullets_coords(xo, yo, angles):
        return [(xo, yo),
                (xo + 7.5 * sin(angles[1]), yo + 7.5 * cos(angles[1])),
                (xo - 7.5 * sin(angles[2]), yo - 7.5 * cos(angles[2])),
                (xo + 15 * sin(angles[3]),  yo + 15 * cos(angles[3])),
                (xo - 15 * sin(angles[4]),  yo - 15 * cos(angles[4]))]

    def generate_bullets(self, x, y, target, gamma):
        angle = calculate_angle(x, y, *target)
        xo, yo = self.get_reference_point(x, y, angle)
        angles = self.get_bullets_angles(angle)
        coords = self.get_bullets_coords(xo, yo, angles)

        bullets = []
        for i in range(5):
            bullets.append(RegularBullet(*coords[i], self.bul_dmg, self.bul_vel, angles[i], Body(self.bul_body)))
        return bullets


# ----------------------------------------------------------------------------- #
class Gun33(Gun32):
    def __init__(self):
        super().__init__()


# ----------------------------------------------------------------------------- #
class Gun34(Gun):
    def __init__(self):
        super().__init__(0, 0.7, -5, 'BigBullet_1', 300, 0)

    def generate_bullets(self, x, y, target, gamma):
        xo, yo = x + 80 * cos(gamma + 0.76*pi), y - 80 * sin(gamma + 0.76*pi)
        angle_0 = calculate_angle(xo, yo, *target)
        pos_0 = (xo + 40 * cos(angle_0), yo - 40 * sin(angle_0))

        xo, yo = x + 80 * cos(gamma - 0.76*pi), y - 80 * sin(gamma - 0.76*pi)
        angle_1 = calculate_angle(xo, yo, *target)
        pos_1 = (xo + 40 * cos(angle_1), yo - 40 * sin(angle_1))

        return [RegularBullet(*pos_0, self.bul_dmg, self.bul_vel, angle_0, Body(self.bul_body)),
                RegularBullet(*pos_1, self.bul_dmg, self.bul_vel, angle_1, Body(self.bul_body))]


# ----------------------------------------------------------------------------- #
class Gun35(GunAutomatic):
    def __init__(self):
        super().__init__(30, 0.75, -5, 'BigBullet_1', 250, 0, 200)

    @staticmethod
    def generate_bullets_auto(x, y, target, gamma):
        pos_0 = (x + 87 * cos(gamma + 0.25*pi), y - 87 * sin(gamma + 0.25*pi))
        pos_1 = (x + 87 * cos(gamma - 0.25*pi), y - 87 * sin(gamma - 0.25*pi))
        angle_0 = calculate_angle(*pos_0, *target)
        angle_1 = calculate_angle(*pos_1, *target)

        return [RegularBullet(*pos_0, -1, 1.5, angle_0, Body(SMALL_BUL_BODY_1)),
                RegularBullet(*pos_1, -1, 1.5, angle_1, Body(SMALL_BUL_BODY_1))]


# ----------------------------------------------------------------------------- #
class Gun40(Gun):
    def __init__(self):
        super().__init__(20, 1.35, -15, 'SniperBullet', 425, 0)

    def generate_bullets(self, x, y, target, gamma):
        angle = calculate_angle(x, y, *target)
        xo, yo = self.get_reference_point(x, y, angle)
        return [EllipticBullet(xo, yo, self.bul_dmg, self.bul_vel, angle, self.bul_body)]


# ----------------------------------------------------------------------------- #
class Gun41(Gun11):
    def __init__(self):
        super().__init__()
        self.cooldown_time = 80


# ----------------------------------------------------------------------------- #
class Gun42(Gun):
    def __init__(self):
        super().__init__(10, 1, -1, 'SmallBullet_1', 200, 0)

    def generate_bullets(self, x, y, target, gamma):
        angle = calculate_angle(x, y, *target)
        xo, yo = self.get_reference_point(x, y, angle)
        pos_0 = (xo, yo)
        pos_1 = (xo + 53 * cos(angle + 0.48*pi), yo - 53 * sin(angle + 0.48*pi))
        pos_2 = (xo + 53 * cos(angle - 0.48*pi), yo - 53 * sin(angle - 0.48*pi))

        return [(RegularBullet(*pos_0, -5, 0.75, angle, Body(BIG_BUL_BODY_1))),
                (RegularBullet(*pos_1, -1, 1,  angle, Body(SMALL_BUL_BODY_1))),
                (RegularBullet(*pos_2, -1, 1,  angle, Body(SMALL_BUL_BODY_1)))]


# ----------------------------------------------------------------------------- #
class Gun43(Gun):
    def __init__(self):
        super().__init__(20, 0.8, -2, 'MediumBullet_1', 150, 0)

    def generate_bullets(self, x, y, target, gamma):
        angle = calculate_angle(x, y, *target)
        pos_0 = (x + 20 * cos(angle + 0.74*pi), y - 20 * sin(angle + 0.74*pi))
        pos_1 = (x + 20 * cos(angle - 0.74*pi), y - 20 * sin(angle - 0.74*pi))

        return [(RegularBullet(*pos_0, self.bul_dmg, self.bul_vel, angle, Body(self.bul_body))),
                (RegularBullet(*pos_1, self.bul_dmg, self.bul_vel, angle, Body(self.bul_body)))]


# ----------------------------------------------------------------------------- #
class Gun44(GunAutomatic):
    def __init__(self):
        super().__init__(30, 0.7, -5, 'BigBullet_1', 200, 0, 200)

    @staticmethod
    def generate_bullets_auto(x, y, target, gamma):
        pos_0 = (x + 96 * cos(gamma + 0.25*pi), y - 96 * sin(gamma + 0.25*pi))
        pos_1 = (x + 96 * cos(gamma - 0.25*pi), y - 96 * sin(gamma - 0.25*pi))
        angle_0 = calculate_angle(*pos_0, *target)
        angle_1 = calculate_angle(*pos_1, *target)

        return [RegularBullet(*pos_0, -1, 1.5, angle_0, Body(SMALL_BUL_BODY_1)),
                RegularBullet(*pos_1, -1, 1.5, angle_1, Body(SMALL_BUL_BODY_1))]

    def generate_bullets(self, x, y, target, gamma):
        xo, yo = x + 90 * cos(gamma + 0.75*pi), y - 90 * sin(gamma + 0.75*pi)
        angle_0 = calculate_angle(xo, yo, *target)
        pos_0 = (xo + 40 * cos(angle_0), yo - 40 * sin(angle_0))

        xo, yo = x + 90 * cos(gamma - 0.75*pi), y - 90 * sin(gamma - 0.75*pi)
        angle_1 = calculate_angle(xo, yo, *target)
        pos_1 = (xo + 40 * cos(angle_1), yo - 40 * sin(angle_1))

        return [RegularBullet(*pos_0, self.bul_dmg, self.bul_vel, angle_0, Body(self.bul_body)),
                RegularBullet(*pos_1, self.bul_dmg, self.bul_vel, angle_1, Body(self.bul_body))]


# ----------------------------------------------------------------------------- #
class Gun45(Gun00):
    def __init__(self):
        super().__init__()


# ----------------------------------------------------------------------------- #
class Gun50(Gun40):
    def __init__(self):
        super().__init__()
        self.cooldown_time = 500
        self.radius = 40
        self.bul_dmg = -25


# ----------------------------------------------------------------------------- #
class Gun51(Gun21):
    def __init__(self):
        super().__init__()
        self.cooldown_time = 80
        self.radius = 15


# ----------------------------------------------------------------------------- #
class Gun52(Gun00):
    def __init__(self):
        super().__init__()


# ----------------------------------------------------------------------------- #
class Gun53(Gun00):
    def __init__(self):
        super().__init__()


# ----------------------------------------------------------------------------- #
class Gun54(Gun00):
    def __init__(self):
        super().__init__()


# ----------------------------------------------------------------------------- #
class Gun55(Gun00):
    def __init__(self):
        super().__init__()
