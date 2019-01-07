#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###############################################################################
# LevelGenerator text data
ENG_ROOM_TEXTS = [
                  ['       W', 'Use A S D', 'to move.',
                   ' Use mouse to aim,', 'hold down the left ', 'mouse button',
                   'to shoot.', 'Try to get out', 'of this bubble...'],

                  ['You moved to a', 'new bubble-field!',
                   'Destroy the', 'bubble-tank', 'enemies to',
                   'take away', 'the bubbles', 'from them', 'and GROW!'],

                  ['Taking damage from', 'enemy tanks',
                   'will make your', 'tank weaker.', 'If you are defeated,',
                   'you will be', 'transported to', 'the nearest safe', 'bubble-field.'],

                  ['Sometimes the best', ' way is to', 'just run away!', '', '', '',
                   '', 'press "p" to pause'],

                  ['The further', 'you go from', 'the initial',
                   'bubble-field, the', 'more difficult the', 'enemies will be!',
                   'So be careful, and...', 'GOOD LUCK!'],

                  ['Now one more skill', 'is available to you!',
                   'To activate', 'this skill,', 'press "SPACE"']]
###############################################################################
# StartMenu text data
ENG_START_MENU_CAPTION = 'Underwater battles'
ENG_PLAY_LABEL = 'PLAY'
###############################################################################
# PauseMenu text data
ENG_STATSWINDOW_CAPTIONS = ['Statistics', 'Main weapon', 'Second weapon']
ENG_MAPWINDOW_CAPTION = 'Map'
ENG_OPTIONSWINDOW_CAPTION = 'Options'
ENG_OPTIONSWINDOW_LABEL_1 = 'Music'
ENG_OPTIONSWINDOW_LABEL_2 = 'Sound'
ENG_OPTIONSWINDOW_BUTTONS_TEXTS = ['ON.', 'OFF.', 'TO MENU']
ENG_PAUSEMENU_CAPTION = 'PAUSE'
ENG_STATSBUTTON_NAME = 'Statistics'
ENG_MAPBUTTON_NAME = 'Map'
ENG_OPTIONSBUTTON_NAME = 'Options'
###############################################################################
# UpgradeMenu text data
upg_text_00 = 'Basic tank', ['Basic cannon'], ['N\A'], ['This is your starting tank.'],\
              ['Shoots regular bullets.'], ['-']

upg_text_10 = 'Hunter #1', ['Machine gun'], ['N\A'], \
              ['Small, fast and', 'maneuverable tank', 'with high rate of fire.'],\
              ['Shoots regular bullets', 'with high rate of fire.'], ['-']

upg_text_11 = 'Balanced #1', ['2 parallel shots'], ['N\A'], ['Balance between speed', 'and strength.'],\
              ['Shoots 2 bullets', 'next to each other.'], ['-']

upg_text_12 = 'Heavy  #1', ['Heavy cannon'], ['N\A'], \
              ['Slightly slower and', 'less maneuverable, but', 'delivers more', 'powerful hits.'],\
              ['Shoots ordinary,', 'heavy bullets that cause', 'significant damage.'], ['-']

upg_text_20 = 'Hunter #2', ['3 bullets scattered'], ['Armor'], \
              ['Improved version of the hunter,', 'its features are speed', 'and maneuverability.'],\
              ['Shoots 3 bullets scattered.'],\
              ['Armor can be triggered as', 'a quick flash to protect you', 'from all damage.']

upg_text_21 = 'Balanced Hunter #1', ['3 parallel shots'], ['Armor'], \
              ['A balanced tank has a little more', 'speed and maneuverability.'],\
              ['Shoots 3 bullets', 'next to each other.'],\
              ['Armor can be triggered as', 'a quick flash to protect', 'you from all kinds', 'of damage.']

upg_text_22 = 'Balanced Heavy #1', ['3 parallel shots'], ['Bombs'], \
              ['A balanced tank is a bit heavier', 'in armament, but lighter, than', 'a Heavy Tank.'],\
              ['Shoots 3 bullets', 'next to each other.'],\
              ['Mines can be installed and', 'will bring great damage when', 'the enemy passes over them.']

upg_text_23 = 'Heavy #2', ['5 parallel shots'], ['Bombs'], \
              ['Large and slow tank, but well armed.'], ['Shoots regular bullets.'], ['-']

upg_text_30 = 'Sniper #1', ['Drilling shot'], ['Teleport'], \
              ['A smart hunter who', 'shoots ordinary,', 'powerful bubbles.'],\
              ['The drilling shot recharges', 'for a long time, but does a lot',
               'of damage and can pass through', 'several enemies.'],\
              ['Pressing the space bar instantly', 'teleports you to where the mouse', 'cursor is.']

upg_text_31 = 'Hunter #3', ['Improved', 'machine gun'], ['Self-guided', 'bullets'], \
              ['3rd generation hunters.', 'Focused on speed', 'and maneuverability.'],\
              ['The improved machine gun', 'has a very high rate of fire',
               'and deals more damage than', 'a regular machine gun.'],\
              ['Launch 2 bubble-missiles', 'that will track down and', 'follow your enemies.']

upg_text_32 = 'Balanced Hunter #2', ['5 bullets scattered'], ['Deafening', 'explosion'], \
              ['A balanced tank has', 'a little more speed', 'and maneuverability.'],\
              ['Shoots 5 bullets scattered.'],\
              ['The impulse comes from', 'a tank that is stuck',
               'surrounded by enemies, and', 'stuns them for a while.']

upg_text_33 = 'Balanced Heavy #2', ['5 bullets scattered'], ['Powerful explosion'], \
              ['A balanced tank is', 'a bit heavier', 'in armament, but lighter,', 'than a Heavy Tank.'],\
              ['Shoots 5 bullets scattered.'],\
              ['The explosion emanates from', 'the tank and hits all', 'surrounding enemies.']

upg_text_34 = 'Heavy #3', ['2 heavy cannons'], ['Sticky cannon'], \
              ['A large and slow tank,', 'that can be proud of', 'powerful weapons', 'and brute force.'],\
              ['Shoots 2 big bubbles', 'at the same time.'],\
              ['Pressing the space bar', 'triggers sticky bubbles', 'that will make the', 'target motionless.']

upg_text_35 = 'APC #1', ['1 B. Cannons, 2 S. auto'], ['Self-guided', 'bullets'], \
              ['A very large and', 'slow tank that', 'looks for enemies', 'to destroy them.'],\
              ['You control a big gun,', 'while 2 small guns will',
               'search for enemies and', 'shoot automatically.'],\
              ['Launch 4 bubble-missiles', 'that will track down and', 'follow your enemies.']

upg_text_40 = 'Sniper #2', ['Powerful', 'Drilling shot'], ['Improved teleport'], \
              ['A smart hunter who', 'shoots ordinary,', 'powerful bubbles.'],\
              ['The drilling shot recharges', 'for a long time, but does a lot',
               'of damage and can pass through', 'several enemies.'],\
              ['Pressing the space bar instantly', 'teleports you to where the mouse', 'cursor is.']

upg_text_41 = 'Hunter #4', ['2 barreled machine gun'], ['"Exploding star" cannon'], \
              ['Small, fast and', 'maneuverable tank', 'with high', 'rate of fire.'],\
              ['2 small bubbles coming', 'alongside each other in', 'quick succession.'],\
              ['The "explosion-star" cannon', 'fires a projectile that',
               'explodes after a while and', 'scatters debris 360 degrees.']

upg_text_42 = 'Balanced Hunter #3', ['2 S., 1 B. Cannon'], ['Self-guided', 'bullets'], \
              ['A medium sized tank.', 'Fast and powerful.'],\
              ['2 small guns and', '1 big gun shoot at', 'the same time'],\
              ['Launch 3 bubble-missiles', 'that will track down and', 'follow your enemies.']

upg_text_43 = 'Balanced Heavy #3', ['2 big machine guns'], ['Powerful explosion'], \
              ['A balanced tank is', 'a bit heavier', 'in armament, but lighter,', 'than a Heavy Tank.'], \
              ['2 big guns shoot with', 'high rate of fire.'], \
              ['Shoots a large bubble', 'that explodes from contact', 'with the enemy,', 'damaging others.']

upg_text_44 = 'Heavy #4', ['2 B. Cannons, 2 S. auto'], ['Sticky explosion'], \
              ['A large and slow tank,', 'that can be proud of', 'powerful weapons', 'and brute force.'],\
              ['You control 2 big cannons,', 'while 2 small cannons',
               'will search for enemies', 'and shoot automatically.'],\
              ['Many sticky bubbles are', 'launched from the tank in',
               'different directions and', 'make enemies immobile.']

upg_text_45 = 'APC #2', ['2 B. cannons, 3 S. auto'], ['Huge powerful explosion'], \
              ['A very large and slow tank', 'that stuns and kills.'], ['Shoots regular bullets.'], ['-']

upg_text_50 = 'Ghost sniper', ['Exploding drilling shot'], ['Invisibility'], \
              ['A very fast and agile tank,', 'which can disappear', 'and reappear.'],\
              ['Long reload, but very strong', 'damage, explodes on contact', 'and can pass through', 'several targets.'],\
              ['Press space to crash the tank', 'into pieces, becoming invincible,',
               'but then you lose the', 'opportunity to shoot.']

upg_text_51 = 'Super Hunter', ['3 machine guns'], ['Orbital', 'homing shurikens'], \
              ['Small and agile tank, which has', 'a high rate of fire and', 'self-guided bullets.'],\
              ['3 small bubbles coming', 'alongside each other in', 'quick succession.'],\
              ['Shurikens automatically', 'appear and surround you.',
               'They will leave you and harm', 'the enemies that have come.']

upg_text_52 = 'Vampire tank', ['Life suction bubbles'], ['Bubbles-viruses'], \
              ['This tank sucks the life', 'out of enemies and can', 'infect them with a virus.'],\
              ['Shoots regular bullets.'], ['-']

upg_text_53 = 'Drone tank', ['Mitotic', 'self-guided bullets'], ['Drones conversion'], \
              ['This tank is a master ', 'of self-guided bullets.'], ['Shoots regular bullets.'], ['-']

upg_text_54 = 'Super Heavy', ['2 E. C, 6 S. A, 1 BC'], ['Huge cannon'], \
              ['A Hefty Monster bubble-tank.'], ['Shoots regular bullets.'], ['-']

upg_text_55 = 'APC carrier', ['1 B. C, 4 S. A, 1 BC'], ['Summon allies'], \
              ['A giant tank that generates', 'a bunch of hunters.'], ['Shoots regular bullets.'], ['-']

ENG_UPGRADE_TEXT = {(0, 0): upg_text_00,
                    (1, 0): upg_text_10,
                    (1, 1): upg_text_11,
                    (1, 2): upg_text_12,
                    (2, 0): upg_text_20,
                    (2, 1): upg_text_21,
                    (2, 2): upg_text_22,
                    (2, 3): upg_text_23,
                    (3, 0): upg_text_30,
                    (3, 1): upg_text_31,
                    (3, 2): upg_text_32,
                    (3, 3): upg_text_33,
                    (3, 4): upg_text_34,
                    (3, 5): upg_text_35,
                    (4, 0): upg_text_40,
                    (4, 1): upg_text_41,
                    (4, 2): upg_text_42,
                    (4, 3): upg_text_43,
                    (4, 4): upg_text_44,
                    (4, 5): upg_text_45,
                    (5, 0): upg_text_50,
                    (5, 1): upg_text_51,
                    (5, 2): upg_text_52,
                    (5, 3): upg_text_53,
                    (5, 4): upg_text_54,
                    (5, 5): upg_text_55}

ENG_UPGRADEMENU_LABELS = ['Upgrade!', '- Main weapon -', '- Second weapon -']
ENG_UPGRADEMENU_CAPTION = 'Choose your upgrade...'
###############################################################################
# VictoryMenu text data
ENG_VICTORYMENU_CAPTION = 'CONGRATULATIONS!'
ENG_VICTORYMENU_TEXT = 'You passed the game!'
ENG_VICTORYMENU_BUTTON = 'Back to menu'
###############################################################################
# CooldownWindow text data
ENG_WINDOW_COOLDOWN_LABELS = ['M:', 'S:']
###############################################################################
# HealthWindow text data
ENG_TANK_NAMES = {(0, 0): 'Base tank',
                  (1, 0): 'Hunter #1',
                  (1, 1): 'Balanced',
                  (1, 2): 'Heavy #2',
                  (2, 0): 'Hunter #2',
                  (2, 1): 'Balanced Hunter #1',
                  (2, 2): 'Balanced Heavy #1',
                  (2, 3): 'Heavy #2',
                  (3, 0): 'Sniper #1',
                  (3, 1): 'Hunter #3',
                  (3, 2): 'Balanced Hunter #2',
                  (3, 3): 'Balanced Heavy #2',
                  (3, 4): 'Heavy #3',
                  (3, 5): 'APC #1',
                  (4, 0): 'Sniper #2',
                  (4, 1): 'Hunter #4',
                  (4, 2): 'Balanced Hunter #3',
                  (4, 3): 'Balanced Heavy #3',
                  (4, 4): 'Heavy #4',
                  (4, 5): 'APC #2',
                  (5, 0): 'Ghost sniper',
                  (5, 1): 'Super Hunter',
                  (5, 2): 'Vampire tank',
                  (5, 3): 'Drone tank',
                  (5, 4): 'Super Heavy',
                  (5, 5): 'APC carrier'}

ENG_BUBBLES_TEXTS = (' bubbles left', 'Maximum tank')
###############################################################################
