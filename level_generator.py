#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from random import randint

from data_text_rus import RUS_ROOM_TEXTS
from data_text_eng import ENG_ROOM_TEXTS

PLAYER_EXTRA_HEALTH = {0: 0, 1: 75, 2: 200, 3: 400, 4: 800, 5: 1300}

MOBS_DICT = {'BossSkeleton': 0,
             'BossLeg': 0,
             'Infusoria': 0,
             'Cell': 0,
             'Ameba': 0,
             'Baby': 0,
             'Turtle': 0,
             'Turtle_dmg': 0,
             'Terrorist': 0,
             'BenLaden': 0,
             'Ant': 0,
             'Scarab': 0,
             'Bug': 0,
             'Gull': 0,
             'Cockroach': 0,
             'GullMother': 0,
             'BugMother': 0,
             'ScarabMother': 0,
             'BomberShooter': 0,
             'Beetle': 0,
             'Spreader': 0,
             'BigEgg': 0,
             'Spider': 0,
             'MachineGunner': 0,
             'Turret': 0}


class DataMatrix:
    def __init__(self):
        self.size = 2001
        self.size2 = self.size // 2
        self.matrix = self.create_matrix()

        self.pos = np.array([self.size2, self.size2])
        self.visited_rooms = [self.pos.copy()]

        self.offset = {'UP':   np.array((0, -1)),
                       'DOWN':  np.array((0, 1)),
                       'LEFT': np.array((-1, 0)),
                       'RIGHT': np.array((1, 0))}

    def create_matrix(self):
        matrix = []
        for i in range(self.size):
            matrix.append([None] * self.size)
        matrix[self.size2][self.size2] = [{}, True]
        return matrix

    def reset(self):
        for room in self.visited_rooms:
            self.matrix[room[0]][room[1]] = None

        self.pos = np.array([self.size2, self.size2])
        self.matrix[self.pos[0]][self.pos[1]] = [{}, True]
        self.visited_rooms = [self.pos.copy()]

    def new_room(self):
        return self.matrix[self.pos[0]][self.pos[1]] is None

    def save_mobs(self, mobs_data):
        self.matrix[self.pos[0]][self.pos[1]][0] = mobs_data

    def get_mobs(self):
        """
        :return: dictionary of mobs in current room
        """
        return self.matrix[self.pos[0]][self.pos[1]][0]

    def get_map_pos(self):
        return [self.pos[0] - self.size2, self.pos[1] - self.size2]

    def update_pos(self, direction):
        self.pos += self.offset[direction]

    def update_visited_rooms(self, new_mobs):
        self.matrix[self.pos[0]][self.pos[1]] = [new_mobs, True]
        self.visited_rooms.append(self.pos.copy())


class RoomTextGenerator:
    def __init__(self):
        self.room_texts = None
        self.player_got_first_superpower = False
        self.superpower_text_was_shown = False

    def reset(self):
        self.player_got_first_superpower = False
        self.superpower_text_was_shown = False

    def set_room_texts(self, language):
        if language == 'English':
            self.room_texts = ENG_ROOM_TEXTS
        elif language == 'Русский':
            self.room_texts = RUS_ROOM_TEXTS

    def text(self, n):
        if n in range(1, 6):
            return self.room_texts[n - 1]
        elif self.player_got_first_superpower:
            self.player_got_first_superpower = False
            self.superpower_text_was_shown = True
            return self.room_texts[5]
        return ''

    def update(self, player_level):
        if player_level == 2 and not self.superpower_text_was_shown:
            self.player_got_first_superpower = True


class LevelGenerator:
    def __init__(self):
        self.data_matrix = DataMatrix()
        self.text_generator = RoomTextGenerator()
        self.num_of_visited_rooms = 1
        self.boss_was_generated = False
        self.boss_new = False

    def set_language(self, language):
        self.text_generator.set_room_texts(language)

    def reset(self):
        self.data_matrix.reset()
        self.text_generator.reset()
        self.num_of_visited_rooms = 1
        self.boss_was_generated = False
        self.boss_new = False

    def generate_mobs(self, player_level, player_health):
        mobs = {}
        health = player_health + PLAYER_EXTRA_HEALTH[player_level]

        if health <= 30:
            if not self.boss_was_generated:
                n_peaceful_mobs = 0
                mobs['BossSkeleton'] = 1
                mobs['BossLeg'] = 1
                mobs['BossHandLeft'] = 1
                mobs['BossHandRight'] = 1
                mobs['BossHead'] = 1
                self.boss_was_generated = True
                self.boss_new = True
            else:
                n_peaceful_mobs = randint(2, 4)

        elif health <= 60:
            n_peaceful_mobs = randint(3, 6)

        elif health <= 120:
            n_peaceful_mobs = randint(1, 3)
            mobs['Turtle'] = randint(1, 3)

        elif health <= 240:
            n_peaceful_mobs = randint(1, 3)
            mobs['Turtle_dmg'] = randint(1, 2)

            group_1 = randint(1, 4)
            if group_1 == 1:
                mobs['Terrorist'] = 1
            elif group_1 == 2:
                mobs['Gull'] = randint(1, 3)
            elif group_1 == 3:
                mobs['Bug'] = randint(1, 3)
            else:
                mobs['Scarab'] = randint(1, 3)

        elif health <= 360:
            n_peaceful_mobs = randint(0, 3)
            mobs['Turtle'] = randint(1, 2)
            mobs['Turtle_dmg'] = randint(1, 2)

            group_1 = randint(1, 3)
            if group_1 == 1:
                mobs['Gull'] = randint(1, 3)
            elif group_1 == 2:
                mobs['Bug'] = randint(1, 3)
            else:
                mobs['Scarab'] = randint(1, 3)

        elif health <= 500:
            n_peaceful_mobs = randint(1, 2)

            group_1 = randint(1, 4)
            if group_1 == 1:
                mobs['Ant'] = 14
            else:
                if group_1 == 2:
                    mobs['Bug'] = randint(1, 2)
                elif group_1 == 3:
                    mobs['Gull'] = randint(1, 2)
                elif group_1 == 4:
                    mobs['Scarab'] = randint(1, 2)

                group_2 = randint(1, 4)
                if group_2 == 1:
                    mobs['GullMother'] = 1
                elif group_2 == 2:
                    mobs['Cockroach'] = randint(1, 2)
                elif group_2 == 3:
                    mobs['BomberShooter'] = 1
                elif group_2 == 4:
                    mobs['Turtle'] = randint(1, 2)
                    mobs['Turtle_dmg'] = randint(1, 2)

        elif health <= 660:
            n_peaceful_mobs = randint(1, 2)

            group_1 = randint(1, 3)
            if group_1 == 1:
                mobs['Spider'] = randint(1, 2)
                mobs['Spreader'] = randint(1, 2)
            elif group_1 == 2:
                mobs['BigEgg'] = randint(3, 4)
            elif group_1 == 3:
                mobs['Beetle'] = randint(1, 2)

                group_2 = randint(1, 4)
                if group_2 == 1:
                    mobs['Cockroach'] = randint(2, 3)
                elif group_2 == 2:
                    mobs['Bug'] = randint(2, 3)
                elif group_2 == 3:
                    mobs['Gull'] = randint(2, 3)
                elif group_2 == 4:
                    mobs['Scarab'] = randint(2, 3)

        elif health <= 860:
            n_peaceful_mobs = randint(1, 3)

            group_1 = randint(1, 1)
            if group_1 == 1:
                mobs['Beetle'] = randint(2, 3)
                mobs['Turtle'] = randint(1, 2)

            group_2 = randint(1, 4)
            if group_2 == 1:
                mobs['Cockroach'] = randint(2, 3)
            elif group_2 == 2:
                mobs['Bug'] = randint(2, 3)
            elif group_2 == 3:
                mobs['Gull'] = randint(2, 3)
            elif group_2 == 4:
                mobs['Scarab'] = randint(2, 3)

        else:
            n_peaceful_mobs = randint(1, 4)

            group_1 = randint(1, 2)
            if group_1 == 1:
                mobs['Turret'] = 2

                group_2 = randint(1, 3)
                if group_2 == 1:
                    mobs['Cockroach'] = randint(3, 5)
                elif group_2 == 2:
                    mobs['Bug'] = randint(3, 5)
                elif group_2 == 3:
                    mobs['Gull'] = randint(3, 5)
            elif group_1 == 2:
                mobs['MachineGunner'] = randint(1, 2)
                mobs['Turtle'] = randint(0, 2)

                group_2 = randint(1, 4)
                if group_2 == 1:
                    mobs['Cockroach'] = randint(1, 2)
                elif group_2 == 2:
                    mobs['Bug'] = randint(1, 2)
                elif group_2 == 3:
                    mobs['Gull'] = randint(1, 2)
                elif group_2 == 4:
                    mobs['Beetle'] = randint(1, 2)

        mobs['Baby'] = randint(0, n_peaceful_mobs // 2)
        mobs['Cell'] = randint(0, (n_peaceful_mobs - mobs['Baby']) // 2)
        mobs['Ameba'] = randint(0, (n_peaceful_mobs - mobs['Baby'] - mobs['Cell']))
        mobs['Infusoria'] = n_peaceful_mobs - mobs['Baby'] - mobs['Cell'] - mobs['Ameba']

        return mobs

    def get_room_text(self):
        return self.text_generator.text(self.num_of_visited_rooms)

    def setup_game_map(self, game_map):
        game_map.update_data(self.data_matrix.get_map_pos())
        if self.boss_new:
            game_map.set_boss_location()
            self.boss_new = False

    def setup_room(self, room):
        room.setup_new_mobs(self.data_matrix.get_mobs())
        room.setup_text(self.get_room_text())

    def update(self, mobs_dict, direction, player_level, player_health):
        self.text_generator.update(player_level)
        self.data_matrix.save_mobs(mobs_dict)
        self.data_matrix.update_pos(direction)
        self.num_of_visited_rooms += 1

        if self.data_matrix.new_room():
            new_mobs = self.generate_mobs(player_level, player_health)
            self.data_matrix.update_visited_rooms(new_mobs)
