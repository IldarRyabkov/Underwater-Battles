#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from menu_upgrade import UpgradeMenu
from menu_start import StartMenu
from menu_pause import PauseMenu
from menu_victory import VictoryMenu
from menu_language import LanguageMenu

from window_health import WindowHealth
from window_cooldown import WindowCooldown


class Gui:
    def __init__(self):
        self.language_menu = LanguageMenu()
        self.start_menu = StartMenu()
        self.upgrade_menu = UpgradeMenu()
        self.pause_menu = PauseMenu()
        self.victory_menu = VictoryMenu()

        self.window_health = WindowHealth()
        self.window_cooldown = WindowCooldown()

    def set_language(self):
        language = self.language_menu.chosen_language
        self.start_menu.set_language(language)
        self.pause_menu.set_language(language)
        self.victory_menu.set_language(language)
        self.upgrade_menu.set_language(language)
        self.window_cooldown.set_labels(language)
        self.window_health.set_language(language)

    def reset(self, player):
        self.start_menu.reset()
        self.pause_menu.reset()
        self.window_cooldown.reset()
        self.window_health.reset()
        self.setup_popup_windows(player)

    def setup_popup_windows(self, player):
        self.window_health.setup(player.state, player.max_health, player.health)
        self.window_cooldown.setup(player.gun.cooldown_time, player.superpower.cooldown_time)

    def update_popup_windows(self, player, dt):
        self.window_health.update(dt)
        self.window_cooldown.update(player, dt)

    def handle_player_state_change(self, player):
        self.setup_popup_windows(player)
        self.pause_menu.stats_window.setup(player.state)
