#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame as pg

import config as c

from gui_elements import UpgradeButton, UpgradeCaption

from data_text_eng import ENG_UPGRADE_TEXT, ENG_UPGRADEMENU_LABELS, ENG_UPGRADEMENU_CAPTION
from data_text_rus import RUS_UPGRADE_TEXT, RUS_UPGRADEMENU_LABELS, RUS_UPGRADEMENU_CAPTION


class UpgradeMenu:
    def __init__(self):
        self.caption = UpgradeCaption()
        self.buttons = []
        self.clock = pg.time.Clock()
        self.chosen_state = None
        self.is_running = False
        self.text = None
        self.button_labels = None
        self.bg_surface = pg.Surface((c.SCR_W, c.SCR_H))

    def set_language(self, language):
        if language == 'English':
            self.text = ENG_UPGRADE_TEXT
            self.button_labels = ENG_UPGRADEMENU_LABELS
            self.caption.set_caption(ENG_UPGRADEMENU_CAPTION)
        else:
            self.text = RUS_UPGRADE_TEXT
            self.button_labels = RUS_UPGRADEMENU_LABELS
            self.caption.set_caption(RUS_UPGRADEMENU_CAPTION)

    def setup(self, states):
        self.is_running = True
        self.caption.reset_velocity()
        self.buttons = []

        if len(states) == 3:
            self.buttons.append(UpgradeButton(*self.text[states[0]], self.button_labels, 1, states[0]))
            self.buttons.append(UpgradeButton(*self.text[states[1]], self.button_labels, 2, states[1]))
            self.buttons.append(UpgradeButton(*self.text[states[2]], self.button_labels, 3, states[2]))
        else:
            self.buttons.append(UpgradeButton(*self.text[states[0]], self.button_labels, 4, states[0]))
            self.buttons.append(UpgradeButton(*self.text[states[1]], self.button_labels, 5, states[1]))

    def handle_mouse_click(self):
        pos = pg.mouse.get_pos()
        for b in self.buttons:
            if b.cursor_on_button(pos):
                self.chosen_state = b.player_state
                self.is_running = False
                break

    def move(self, screen, action_marker):
        if action_marker == 'close':
            self.caption.vel_y *= -1
            for button in self.buttons:
                button.vel_x *= -1
                button.vel_y *= -1

        time, dt = 0, 0
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.clock.tick()
            self.update(dt)
            self.draw(screen)
            pg.display.update()
            dt = self.clock.tick()
            if time >= 350:
                running = False
            else:
                time = 350 if time+dt > 350 else time+dt

    def update(self, dt):
        for button in self.buttons:
            button.update(dt)
        self.caption.update_pos(dt)

    def draw(self, surface):
        surface.blit(self.bg_surface, (0, 0))
        for button in self.buttons:
            button.draw(surface)
        self.caption.draw(surface)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.handle_mouse_click()

    def run(self, player_states, screen):
        self.setup(player_states)

        self.bg_surface.blit(screen, (0, 0))

        self.move(screen, 'open')

        while self.is_running:
            self.handle_events()
            self.update(0)
            self.draw(screen)
            pg.display.update()

        self.move(screen, 'close')
