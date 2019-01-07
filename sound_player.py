#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg


class SoundPlayer:
    def __init__(self):
        self.sounds = {}
        self.create_sounds()
        self.sound_on = True
        self.sound_was_played = False

        self.music = {1: './music/start_music.wav',
                      2: './music/game_music.wav'}
        self.music_on = True

    def create_sounds(self):
        pg.mixer.pre_init(44100, 16, 2, 1024)
        sounds = dict(player_bullet_hit='./sound_effects/player_bullet_hit.wav',
                      player_bullet_shot='./sound_effects/player_bullet_shot.wav',
                      mob_death='./sound_effects/mob_death.wav',
                      player_injure='./sound_effects/player_injure.wav',
                      bubble_death='./sound_effects/bubble_death.wav')
        self.sounds = {name: pg.mixer.Sound(sound)
                       for name, sound in sounds.items()}

    def reset(self):
        self.sound_was_played = False

    def play_sound(self, name):
        if self.sound_on and not self.sound_was_played:
            self.sounds[name].play()
            self.sound_was_played = True

    def play_music(self, music_marker):
        pg.mixer.music.load(self.music[music_marker])
        pg.mixer.music.play(-1, 0.0)
        if not self.music_on:
            pg.mixer.music.pause()

    def update_data(self, music_is_on, sound_is_on):
        if self.music_on and not music_is_on:
            self.music_on = False
            pg.mixer.music.pause()
        elif not self.music_on and music_is_on:
            self.music_on = True
            pg.mixer.music.unpause()

        self.sound_on = sound_is_on
