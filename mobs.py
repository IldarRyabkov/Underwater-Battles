#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import cos, sin, pi
from random import uniform, choice
import pygame as pg

from math_functions import calculate_angle, circle_collidepoint
from body import Body
from guns_mobs import guns_factory as guns_factory_mobs
from guns_player import guns_factory as guns_factory_player

import data_mobs as m
import config as c


def mob_factory(name):
    if name == 'BossSkeleton': return MobBossSkeleton()
    if name == 'BossLeg': return MobBossLeg()
    if name == 'BossHandLeft': return MobBossHand(side='left')
    if name == 'BossHandRight': return MobBossHand(side='right')
    if name == 'BossHead': return MobBossHead()
    if name == 'Infusoria': return MobInfusoria()
    if name == 'Cell': return MobCell()
    if name == 'Ameba': return MobAmeba()
    if name == 'Baby': return MobBaby()
    if name == 'Turtle': return MobTurtle(damaging=False)
    if name == 'Turtle_dmg': return MobTurtle(damaging=True)
    if name == 'Terrorist': return MobTerrorist()
    if name == 'Bug': return MobBug()
    if name == 'Ant': return MobAnt()
    if name == 'Scarab': return MobScarab()
    if name == 'Gull': return MobGull()
    if name == 'GullMother': return MobGullMother()
    if name == 'Cockroach': return MobCockroach()
    if name == 'BenLaden': return MobBenLaden()
    if name == 'BomberShooter': return MobBomberShooter()
    if name == 'Beetle': return MobBeetle()
    if name == 'Spreader': return MobSpreader()
    if name == 'BigEgg': return MobBigEgg()
    if name == 'Spider': return MobSpider()
    if name == 'MachineGunner': return MobMachineGunner()
    if name == 'Turret': return MobTurret()


class Mob:
    def __init__(self,
                 name,
                 x,
                 y,
                 health,
                 health_states,
                 bubbles,
                 radius,
                 body,
                 gun_type='PeacefulGun',
                 time=0.0,
                 w=0.0,
                 body_rect=None):

        self.gun = guns_factory_player(gun_type) if name == 'Player' else guns_factory_mobs(gun_type)
        self.name = name
        self.xo = x
        self.yo = y
        self.x = x
        self.y = y
        self.time = time
        self.w = w
        self.speed = [0, 0]
        self.max_health = health
        self.health = health
        self.health_states = health_states
        self.bubbles = bubbles
        self.radius = radius
        self.body = Body(body)
        self.body_rect = body_rect
        self.is_paralysed = False
        self.paralysed_time = 0
        self.gamma = 0
        self.is_frozen = False
        self.frost_time = 0

    def trajectory(self, t):
        return self.xo, self.yo

    def rose_curve_1(self, t):
        x = self.xo + 170 * (cos(9*t/4) + 7/3) * cos(t)
        y = self.yo + 170 * (cos(9*t/4) + 7/3) * sin(t)
        return x, y

    def rose_curve_2(self, t):
        x = self.xo + 500 * sin(3/4 * t) * cos(t)
        y = self.yo - 500 * sin(3/4 * t) * sin(t)
        return x, y

    def rose_curve_3(self, t):
        x = self.xo + 375 * cos(t) + 30 * cos(5 * t)
        y = self.yo + 375 * sin(t) + 30 * sin(5 * t)
        return x, y

    def rose_curve_4(self, t):
        x = self.xo + 250 * sin(2/3 * t) * cos(t)
        y = self.yo - 250 * sin(2/3 * t) * sin(t)
        return x, y

    def epicycloid(self, t):
        x = self.xo + 250 * cos(t) + 20 * cos(5 * t)
        y = self.yo + 250 * sin(t) + 20 * sin(5 * t)
        return x, y

    def collide_bullet(self, x, y):
        return circle_collidepoint(self.x, self.y, self.radius, x, y)

    def change_body(self):
        for circle in self.body.circles:
            circle.is_visible = True
        k = 0
        for i in range(len(self.health_states)):
            if self.health <= self.health_states[i][0]:
                k = i
        for i in range(1, len(self.health_states[k])):
            for j in range(self.health_states[k][i][0], self.health_states[k][i][1]):
                self.body.circles[j].is_visible = False

        if self.is_frozen:
            self.make_body_frozen()
        else:
            self.make_body_unfrozen()

    def handle_injure(self, damage):
        if damage:
            self.health += damage
            self.change_body()
        else:
            self.make_frozen()

    def count_gamma(self):
        dt = 0.01 if self.w > 0 else -0.01
        x, y = self.trajectory(self.time + dt)
        return calculate_angle(self.x, self.y, x, y)

    def move(self, dx, dy):
        self.body.move(dx, dy)
        self.body_rect = self.body_rect.move(dx, dy)

    def update_pos(self, dt, generated_mobs=list()):
        self.time += dt/1000 * self.w
        self.x, self.y = self.trajectory(self.time)
        self.body_rect.center = (self.x, self.y)

    def update_body(self, dt, target):
        self.body.update(self.x, self.y, dt, target, self.gamma)

    def make_paralysed(self):
        self.is_paralysed = True
        self.paralysed_time = 0

    def make_body_frozen(self):
        for i in range(-10, 0):
            self.body.circles[i].is_visible = True

    def make_body_unfrozen(self):
        for i in range(-10, 0):
            self.body.circles[i].is_visible = False

    def make_unfrozen(self):
        self.is_frozen = False
        self.frost_time = 0
        self.make_body_unfrozen()

    def make_frozen(self):
        self.is_frozen = True
        self.frost_time = 0
        self.make_body_frozen()

    def update_paralysed_state(self, dt):
        if self.is_paralysed:
            self.paralysed_time += dt
            if self.paralysed_time >= 2000:
                self.paralysed_time = 0
                self.is_paralysed = False

    def update_frozen_state(self, dt):
        if self.is_frozen:
            self.frost_time += dt
            if self.frost_time >= 3000:
                self.make_unfrozen()

    def update(self, target, bullets, homing_bullets,
               generated_mobs, screen_rect, dt):
        if not self.is_paralysed:
            if not self.is_frozen:
                self.update_pos(dt, generated_mobs)

            self.gun.update_time(dt)
            self.gamma = self.count_gamma()
            list_of_bullets = homing_bullets if self.gun.shooting_homing_bullets else bullets
            self.gun.append_bullets(self.x, self.y, target, list_of_bullets, self.gamma)

            if self.body_rect.colliderect(screen_rect):
                self.update_body(dt, target)

        self.update_paralysed_state(dt)
        self.update_frozen_state(dt)


class MobBossHead(Mob):
    def __init__(self):
        Mob.__init__(self,
                     name='BossHead',
                     x=c.SCR_W2,
                     y=c.SCR_H2 - 625,
                     health=150,
                     health_states=m.BOSS_HEAD_HEALTH_STATES,
                     bubbles=(0, 5, 3),
                     radius=82,
                     body=m.BOSS_HEAD_BODY,
                     gun_type='GunBossHead',
                     time=0,
                     w=0,
                     body_rect=pg.Rect(0, 0, 290, 280))

    def update_pos(self, dt, generated_mobs=list()):
        super().update_pos(dt, generated_mobs)
        self.body_rect.y += 150

    def collide_bullet(self, x, y):
        return circle_collidepoint(self.x, self.y + 100, self.radius, x, y)

    def update_body(self, dt, player_pos):
        index = 0
        for circle in self.body.circles:
            if circle.is_visible:
                target = self.gun.target if 16 <= index < 24 else player_pos
                circle.update(self.x, self.y, dt, target, 0, -0.5 * pi)
            index += 1


class MobBossHand(Mob):
    def __init__(self, side):
        name = 'BossHandLeft' if side == 'left' else 'BossHandRight'
        x = -11 if side == 'left' else 811

        Mob.__init__(self,
                     name=name,
                     x=x,
                     y=-99,
                     health=150,
                     health_states=m.BOSS_HAND_HEALTH_STATES,
                     bubbles=(0, 5, 3),
                     radius=75,
                     body=m.BOSS_HAND_BODY,
                     gun_type='GunBossHand',
                     time=0,
                     w=0,
                     body_rect=pg.Rect(0, 0, 260, 260))

        if side == 'left':
            for circle in self.body.circles:
                circle.alpha *= -1


class MobBossLeg(Mob):
    def __init__(self):
        Mob.__init__(self,
                     name='BossLeg',
                     x=c.SCR_W2,
                     y=c.SCR_H2 + 520,
                     health=150,
                     health_states=m.BOSS_LEG_HEALTH_STATES,
                     bubbles=(0, 5, 3),
                     radius=75,
                     body=m.BOSS_LEG_BODY,
                     gun_type='GunBossLeg',
                     time=0,
                     w=0,
                     body_rect=pg.Rect(0, 0, 250, 350))

        for circle in self.body.circles:
            circle.alpha += pi


class MobBossSkeleton(Mob):
    def __init__(self):
        Mob.__init__(self,
                     name='BossSkeleton',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=1,
                     health_states=m.BOSS_SKELETON_HEALTH_STATES,
                     bubbles=(0, 0, 0),
                     radius=0,
                     body=m.BOSS_SKELETON_BODY,
                     gun_type='GunPeaceful',
                     time=0,
                     w=0,
                     body_rect=pg.Rect(0, 0, 2000, 2000))

        for circle in self.body.circles:
            circle.alpha += pi

    def update(self, target, bullets, homing_bullets,
               generated_mobs, screen_rect, dt):
        pass


class MobAmeba(Mob):
    def __init__(self):
        Mob.__init__(self,
                     name='Ameba',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=4,
                     health_states=m.AMEBA_HEALTH_STATES,
                     bubbles=(2, 0, 0),
                     radius=25,
                     body=m.AMEBA_BODY,
                     gun_type='GunPeaceful',
                     time=uniform(0, 1000),
                     w=choice([-0.2, 0.2]),
                     body_rect=pg.Rect(0, 0, 56, 56))

        self.trajectory = self.rose_curve_1


class MobCell(Mob):
    def __init__(self):
        Mob.__init__(self,
                     name='Cell',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=4,
                     health_states=m.CELL_HEALTH_STATES,
                     bubbles=(3, 0, 0),
                     radius=15,
                     body=m.CELL_BODY,
                     gun_type='GunPeaceful',
                     time=uniform(0, 1000),
                     w=choice([-0.65, 0.65]),
                     body_rect=pg.Rect(0, 0, 50, 50))

        self.trajectory = self.rose_curve_1


class MobInfusoria(Mob):
    def __init__(self):
        Mob.__init__(self,
                     name='Infusoria',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=2,
                     health_states=m.INFUSORIA_HEALTH_STATES,
                     bubbles=(7, 0, 0),
                     radius=25,
                     body=m.INFUSORIA_BODY,
                     gun_type='GunPeaceful',
                     time=uniform(0, 1000),
                     w=choice([-0.45, 0.45]),
                     body_rect=pg.Rect(0, 0, 70, 70))

        self.trajectory = self.rose_curve_1


class MobBaby(Mob):
    def __init__(self):
        Mob.__init__(self,
                     name='Baby',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=1,
                     health_states=m.BABY_HEALTH_STATES,
                     bubbles=(1, 0, 0),
                     radius=15,
                     body=m.BABY_BODY,
                     gun_type='GunPeaceful',
                     time=uniform(0, 1000),
                     w=choice([-0.3, 0.3]),
                     body_rect=pg.Rect(0, 0, 40, 40))

        self.trajectory = self.rose_curve_1


class MobTurtle(Mob):
    def __init__(self, damaging):
        name = 'Turtle_dmg' if damaging else 'Turtle'
        bubbles = (3, 1, 0) if damaging else (6, 0, 0)
        gun_type = 'GunTurtleDMG' if damaging else 'GunTurtle'

        Mob.__init__(self,
                     name=name,
                     x=c.SCR_W2 + choice([-200, 200]),
                     y=c.SCR_H2 + choice([-200, 200]),
                     health=21,
                     health_states=m.TURTLE_HEALTH_STATES,
                     bubbles=bubbles,
                     radius=54,
                     body=m.TURTLE_BODY,
                     gun_type=gun_type,
                     time=uniform(0, 1000),
                     w=choice([-0.5, 0.5]),
                     body_rect=pg.Rect(0, 0, 150, 150))

        self.trajectory = self.epicycloid

        if self.name == 'Turtle_dmg':
            self.adjust_body()

    def adjust_body(self):
        for i in range(-18, -14):
            self.body.circles.pop(i)


class MobTerrorist(Mob):
    def __init__(self):

        Mob.__init__(self,
                     name='Terrorist',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=18,
                     health_states=m.TERRORIST_HEALTH_STATES,
                     bubbles=(9, 0, 0),
                     radius=70,
                     body=m.TERRORIST_BODY,
                     gun_type='GunTerrorist',
                     time=uniform(0, 1000),
                     w=choice([-0.15, 0.15]),
                     body_rect=pg.Rect(0, 0, 210, 210))

        self.trajectory = self.rose_curve_2

    def change_body(self):
        super().change_body()
        if self.health <= 4:
            self.gun = guns_factory_mobs('GunPeaceful')


class MobBenLaden(Mob):
    def __init__(self):

        Mob.__init__(self,
                     name='BenLaden',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=50,
                     health_states=m.BENLADEN_HEALTH_STATES,
                     bubbles=(20, 0, 0),
                     radius=90,
                     body=m.BENLADEN_BODY,
                     gun_type='GunBenLaden',
                     time=uniform(0, 1000),
                     w=choice([-0.18, 0.18]),
                     body_rect=pg.Rect(0, 0, 290, 290))

        self.trajectory = self.rose_curve_3


class MobBug(Mob):
    def __init__(self):

        Mob.__init__(self,
                     name='Bug',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=5,
                     health_states=m.BUG_HEALTH_STATES,
                     bubbles=(3, 0, 0),
                     radius=20,
                     body=m.BUG_BODY,
                     gun_type='GunBug',
                     time=uniform(0, 1000),
                     w=choice([-0.7, 0.7]),
                     body_rect=pg.Rect(0, 0, 85, 85))

        self.trajectory = self.rose_curve_1


class MobAnt(Mob):
    def __init__(self):

        Mob.__init__(self,
                     name='Ant',
                     x=c.SCR_W2 + choice([-250, 250]),
                     y=c.SCR_H2 + choice([-250, 250]),
                     health=4,
                     health_states=m.ANT_HEALTH_STATES,
                     bubbles=(2, 0, 0),
                     radius=25,
                     body=m.ANT_BODY,
                     gun_type='GunAnt',
                     time=uniform(0, 1000),
                     w=choice([-1.3, 1.3]),
                     body_rect=pg.Rect(0, 0, 95, 95))

        self.trajectory = self.rose_curve_4


class MobScarab(Mob):
    def __init__(self):

        Mob.__init__(self,
                     name='Scarab',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=6,
                     health_states=m.SCARAB_HEALTH_STATES,
                     bubbles=(6, 0, 0),
                     radius=26,
                     body=m.SCARAB_BODY,
                     gun_type='GunScarab',
                     time=uniform(0, 1000),
                     w=choice([-0.7, 0.7]),
                     body_rect=pg.Rect(0, 0, 90, 90))

        self.trajectory = self.rose_curve_1


class MobGull(Mob):
    def __init__(self):

        Mob.__init__(self,
                     name='Gull',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=5,
                     health_states=m.GULL_HEALTH_STATES,
                     bubbles=(6, 0, 0),
                     radius=35,
                     body=m.GULL_BODY,
                     gun_type='GunGull',
                     time=uniform(0, 1000),
                     w=choice([-0.7, 0.7]),
                     body_rect=pg.Rect(0, 0, 120, 120))

        self.trajectory = self.rose_curve_1


class MobMother(Mob):
    def __init__(self, name):
        Mob.__init__(self,
                     name=name,
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=90,
                     health_states=m.MOTHER_HEALTH_STATES,
                     bubbles=(5, 0, 1),
                     radius=95,
                     body=m.MOTHER_BODY,
                     gun_type='GunPeaceful',
                     time=uniform(0, 1000),
                     w=choice([-0.15, 0.15]),
                     body_rect=pg.Rect(0, 0, 260, 260))

        self.trajectory = self.rose_curve_1
        self.generation_time = 5000
        self.generation_cooldown = 7000

    def __mob_factory(self):
        if self.name == 'GullMother':
            return MobGull()
        if self.name == 'BugMother':
            return MobBug()
        if self.name == 'ScarabMother':
            return MobScarab()

    def generate_child(self, dt):
        child = []
        self.generation_time += dt
        if self.generation_time >= self.generation_cooldown:
            self.generation_time -= self.generation_cooldown
            mob = self.__mob_factory()
            mob.xo = self.xo
            mob.yo = self.yo
            mob.x = self.x
            mob.y = self.y
            mob.time = self.time
            mob.body.update(mob.x, mob.y, 0)
            child = [mob]
        return child

    def update_pos(self, dt, generated_mobs=list()):
        super().update_pos(dt, generated_mobs)
        generated_mobs.extend(self.generate_child(dt))


class MobGullMother(MobMother):
    def __init__(self):
        MobMother.__init__(self, name='GullMother')


class MobBugMother(MobMother):
    def __init__(self):
        MobMother.__init__(self, name='BugMother')


class MobScarabMother(MobMother):
    def __init__(self):
        MobMother.__init__(self, name='ScarabMother')


class MobCockroach(Mob):
    def __init__(self):

        Mob.__init__(self,
                     name='Cockroach',
                     x=c.SCR_W2 + choice([-250, 250]),
                     y=c.SCR_H2 + choice([-250, 250]),
                     health=10,
                     health_states=m.COCKROACH_HEALTH_STATES,
                     bubbles=(5, 0, 0),
                     radius=45,
                     body=m.COCKROACH_BODY,
                     gun_type='GunCockroach',
                     time=uniform(0, 1000),
                     w=choice([-1.3, 1.3]),
                     body_rect=pg.Rect(0, 0, 110, 110))

        self.trajectory = self.rose_curve_4

    def change_body(self):
        super().change_body()
        if self.health <= 3:
            self.gun = guns_factory_mobs('GunPeaceful')


class MobBomberShooter(Mob):
    def __init__(self):

        Mob.__init__(self,
                     name='BomberShooter',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=27,
                     health_states=m.BOMBERSHOOTER_HEALTH_STATES,
                     bubbles=(11, 0, 0),
                     radius=75,
                     body=m.BOMBERSHOOTER_BODY,
                     gun_type='GunBomberShooter',
                     time=uniform(0, 1000),
                     w=choice([-0.45, 0.45]),
                     body_rect=pg.Rect(0, 0, 200, 200))

        self.trajectory = self.rose_curve_1


class MobBeetle(Mob):
    def __init__(self):

        Mob.__init__(self,
                     name='Beetle',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=30,
                     health_states=m.BEETLE_HEALTH_STATES,
                     bubbles=(9, 0, 0),
                     radius=70,
                     body=m.BEETLE_BODY,
                     gun_type='GunBeetle',
                     time=uniform(0, 1000),
                     w=choice([-0.45, 0.45]),
                     body_rect=pg.Rect(0, 0, 230, 230))

        self.trajectory = self.rose_curve_1

    def change_body(self):
        super().change_body()
        if self.health <= 6 and self.gun.cooldown_time == 450:
            self.gun = guns_factory_mobs('GunBeetleReserve')


class MobSpreader(Mob):
    def __init__(self):

        Mob.__init__(self,
                     name='Spreader',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=18,
                     health_states=m.SPREADER_HEALTH_STATES,
                     bubbles=(15, 0, 0),
                     radius=52,
                     body=m.SPREADER_BODY,
                     gun_type='GunSpreader',
                     time=uniform(0, 1000),
                     w=choice([-0.15, 0.15]),
                     body_rect=pg.Rect(0, 0, 110, 110))

        self.trajectory = self.rose_curve_1


class MobBigEgg(Mob):
    def __init__(self):

        Mob.__init__(self,
                     name='BigEgg',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=50,
                     health_states=m.BIGEGG_HEALTH_STATES,
                     bubbles=(15, 0, 0),
                     radius=75,
                     body=m.BIGEGG_BODY,
                     gun_type='GunBigEgg',
                     time=uniform(0, 1000),
                     w=choice([-0.6, 0.6, -0.55, 0.55]),
                     body_rect=pg.Rect(0, 0, 150, 150))

        self.trajectory = self.rose_curve_2


class MobSpider(Mob):
    def __init__(self):
        Mob.__init__(self,
                     name='Spider',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=130,
                     health_states=m.SPIDER_HEALTH_STATES,
                     bubbles=(12, 0, 0),
                     radius=95,
                     body=m.SPIDER_BODY,
                     gun_type='GunSpider',
                     time=uniform(0, 1000),
                     w=choice([-0.45, 0.45]),
                     body_rect=pg.Rect(0, 0, 230, 230))

        self.trajectory = self.rose_curve_2

    def change_body(self):
        super().change_body()
        if self.health <= 70:
            self.gun.small_gun_is_alive = False


class MobMachineGunner(Mob):
    def __init__(self):

        Mob.__init__(self,
                     name='MachineGunner',
                     x=c.SCR_W2,
                     y=c.SCR_H2,
                     health=50,
                     health_states=m.MACHINEGUNNER_HEALTH_STATES,
                     bubbles=(8, 0, 0),
                     radius=55,
                     body=m.MACHINEGUNNER_BODY,
                     gun_type='GunMachineGunner',
                     w=choice([-0.8, 0.8]),
                     body_rect=pg.Rect(0, 0, 130, 130))

        self.trajectory = self.rose_curve_2


class MobTurret(Mob):
    def __init__(self):
        r, fi = uniform(0, 500), uniform(0, 2*pi)

        Mob.__init__(self,
                     name='Turret',
                     x=c.SCR_W2 + r*cos(fi),
                     y=c.SCR_H2 - r*sin(fi),
                     health=55,
                     health_states=m.TURRET_HEALTH_STATES,
                     bubbles=(18, 0, 0),
                     radius=72,
                     body=m.TURRET_BODY,
                     gun_type='GunTurret',
                     time=uniform(0, 1000),
                     w=-1,
                     body_rect=pg.Rect(0, 0, 230, 230))

        self.update_body(0, (0, 0))

    def update_body(self, dt, target):
        self.body.update(self.x, self.y, dt, self.gun.target, 0)
