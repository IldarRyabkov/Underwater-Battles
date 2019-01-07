#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi
from colors import WHITE, ORANGE, BLUE, VIOLET, LIGHT_ORANGE


MAX_VEL_00 = 0.7
ACC_00 = 0.002
GUN_TYPE_00 = 'Gun00'
SUPERPOWER_00 = None
MAX_HEALTH_00 = 75
RADIUS_00 = 45
BG_RADIUS_00 = 100
BODY_00 = [[32, 4, BLUE,   0, 0, True,  0.033, 20, 0,   True,  True, 0,  0.00],
           [16, 2, ORANGE, 0, 0, True,  0.03,  18, 0,   True,  True, 0,  0.00],
           [8,  1, ORANGE, 0, 0, True,  0.014, 8,  0,   True,  True, 19, 0.00],
           [10, 1, BLUE,   0, 0, True,  0.015, 9,  0,   False, True, 39, pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 9,  0.3, False, True, 39, 0.8 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 9,  0.7, False, True, 39, -0.8 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 9,  0.5, False, True, 39, 0.6 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 9,  0.2, False, True, 39, -0.6 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 9,  0.9, False, True, 39, 0.4 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 9,  0.6, False, True, 39, -0.4 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 9,  0.3, False, True, 39, 0.75 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 9,  0.7, False, True, 39, -0.75 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.3, False, True, 43, pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, False, True, 39, pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, False, True, 39, 0.75 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, False, True, 39, -0.75 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, False, True, 39, 0.6 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.2, False, True, 39, -0.6 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.9, False, True, 54, 0.68 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.6, False, True, 54, -0.68 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.9, False, True, 39, 0.1 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.6, False, True, 39, -0.1 * pi],
           [6,  1, BLUE,   0, 0, True,  0.01,  6,  0.5, False, True, 49, 0.12 * pi],
           [6,  1, BLUE,   0, 0, True,  0.01,  6,  0.2, False, True, 49, -0.12 * pi],
           [6,  1, BLUE,   0, 0, True,  0.01,  6,  0.7, False, True, 49, 0.18 * pi],
           [6,  1, BLUE,   0, 0, True,  0.01,  6,  0.9, False, True, 49, -0.18 * pi],
           [5,  1, BLUE,   0, 0, True,  0.01,  6,  0.8, False, True, 49, 0.24 * pi],
           [5,  1, BLUE,   0, 0, True,  0.01,  6,  0.4, False, True, 49, -0.24 * pi],
           [6,  1, BLUE,   0, 0, True,  0.01,  6,  0.9, False, True, 53, 0.57 * pi],
           [6,  1, BLUE,   0, 0, True,  0.01,  6,  0.2, False, True, 53, -0.57 * pi],
           [5,  1, BLUE,   0, 0, True,  0.008, 5,  0.1, False, True, 49, 0.3 * pi],
           [5,  1, BLUE,   0, 0, True,  0.008, 5,  0.5, False, True, 49, -0.3 * pi],
           [16, 2, BLUE,   0, 0, True,  0.025, 15, 0.9, False, True, 44, pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, False, True, 39, 0.08 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, False, True, 39, -0.08 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.6, False, True, 55, 0.00],
           [6,  1, BLUE,   0, 0, True,  0.01,  6,  0.0, False, True, 69, 0.63 * pi],
           [6,  1, BLUE,   0, 0, True,  0.01,  6,  0.3, False, True, 69, -0.63 * pi],
           [6,  1, BLUE,   0, 0, True,  0.01,  6,  0.8, False, True, 71, 0.7 * pi],
           [6,  1, BLUE,   0, 0, True,  0.01,  6,  0.1, False, True, 71, -0.7 * pi],
           [11, 2, BLUE,   0, 0, True,  0.017, 10, 0.2, False, True, 39, 0.89 * pi],
           [11, 2, BLUE,   0, 0, True,  0.017, 10, 0.5, False, True, 39, -0.89 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.2, False, True, 41, 0.89 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.5, False, True, 41, -0.89 * pi],

           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_00 = ((75, (3, 14), (20, 28), (30, 33), (40, 42)),
                    (69, (3, 14), (20, 28), (30, 33), (42, 44)),
                    (64, (3, 14), (20, 28), (30, 32), (40, 44)),
                    (63, (3, 14), (20, 28), (30, 32), (38, 44)),
                    (61, (3, 14), (20, 28), (30, 32), (36, 44)),
                    (49, (3, 14), (33, 44)),
                    (43, (3, 14), (32, 44)),
                    (37, (3, 14), (32, 44)),
                    (36, (3, 14), (30, 44)),
                    (34, (3, 14), (28, 44)),
                    (32, (3, 14), (26, 44)),
                    (31, (3, 14), (24, 44)),
                    (30, (3, 13), (24, 44)),
                    (29, (3, 12), (13, 14), (20, 44)),
                    (24, (3, 13), (20, 44)),
                    (18, (3, 6),  (8, 10), (13, 44)),
                    (13, (4, 6),  (8, 10), (12, 44)),
                    (7,  (10, 44)),
                    (6,  (9, 44)),
                    (5,  (8, 44)),
                    (4,  (7, 44)),
                    (3,  (6, 44)),
                    (2,  (5, 44)),
                    (1,  (4, 44)),
                    (0,  (3, 44)))

PARAMS_00 = [MAX_HEALTH_00, HEALTH_STATES_00, RADIUS_00, BODY_00,
             MAX_VEL_00, ACC_00, GUN_TYPE_00, BG_RADIUS_00, SUPERPOWER_00]
###############################################################################
MAX_VEL_10 = 0.7
ACC_10 = 0.0025
GUN_TYPE_10 = 'Gun10'
SUPERPOWER_10 = None
MAX_HEALTH_10 = 125
RADIUS_10 = 70
BG_RADIUS_10 = 120
BODY_10 = [[32, 4, BLUE,   0, 0, True,  0.033, 20, 0,   True,  True, 0,  0.00],
           [16, 2, ORANGE, 0, 0, True,  0.03,  18, 0,   True,  True, 0,  0.00],
           [7,  1, ORANGE, 0, 0, True,  0.009, 5,  0,   True,  True, 19, 0.00],
           [9,  1, ORANGE, 0, 0, True,  0.011, 6,  0.3, True,  True, 22, 0.75 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.011, 6,  0.7, True,  True, 22, -0.75 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.9, True,  True, 39, 0.75 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.6, True,  True, 39, -0.75 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.5, True,  True, 39, 0.6 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.2, True,  True, 39, -0.6 * pi],
           # 9
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.9, True,  True, 54, 0.68 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.6, True,  True, 54, -0.68 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.9, True,  True, 53, 0.57 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.6, True,  True, 53, -0.57 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, True,  True, 39, 0.08 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, True,  True, 39, -0.08 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.6, True,  True, 55, 0.00],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.9, True,  True, 69, 0.63 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.6, True,  True, 69, -0.63 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.9, True,  True, 71, 0.7 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.6, True,  True, 71, -0.7 * pi],
           # 20
           [12, 2, BLUE,   0, 0, True,  0.017, 10, 0.2, True,  True, 41, 0.89 * pi],
           [12, 2, BLUE,   0, 0, True,  0.017, 10, 0.5, True,  True, 41, -0.89 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.2, False, True, 43, 0.89 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.5, False, True, 43, -0.89 * pi],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.2, False, True, 45, 0.89 * pi],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.5, False, True, 45, -0.89 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.9, False, True, 57, 0.56 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.6, False, True, 57, -0.56 * pi],
           # 28
           [18, 2, BLUE,   0, 0, True,  0.022, 13, 0.9, False, True, 58, 0.68 * pi],
           [18, 2, BLUE,   0, 0, True,  0.022, 13, 0.6, False, True, 58, -0.68 * pi],
           [8,  1, BLUE,   0, 0, True,  0.005, 5,  0.9, False, True, 67, 0.79 * pi],
           [8,  1, BLUE,   0, 0, True,  0.005, 5,  0.6, False, True, 67, -0.79 * pi],
           [11, 2, BLUE,   0, 0, True,  0.015, 9,  0.9, False, True, 59, 0.55 * pi],
           [11, 2, BLUE,   0, 0, True,  0.015, 9,  0.6, False, True, 59, -0.55 * pi],
           [11, 2, BLUE,   0, 0, True,  0.015, 9,  0.3, False, True, 67, 0.79 * pi],
           [11, 2, BLUE,   0, 0, True,  0.015, 9,  0.7, False, True, 67, -0.79 * pi],
           # 36
           [8,  1, BLUE,   0, 0, True,  0.014, 8,  0.6, False, True, 39, 0.00],
           [8,  1, BLUE,   0, 0, True,  0.014, 8,  0.6, False, True, 39, 0.2 * pi],
           [8,  1, BLUE,   0, 0, True,  0.014, 8,  0.2, False, True, 39, -0.2 * pi],
           [8,  1, BLUE,   0, 0, True,  0.014, 8,  0.8, False, True, 39, 0.4 * pi],
           [8,  1, BLUE,   0, 0, True,  0.014, 8,  0.1, False, True, 39, -0.4 * pi],
           [13, 2, BLUE,   0, 0, True,  0.017, 10, 0.1, False, True, 40, pi],
           # 42
           [16, 2, BLUE,   0, 0, True,  0.015, 12, 0.1, False, True, 41, pi],
           [18, 2, BLUE,   0, 0, True,  0.022, 13, 0.1, False, True, 43, pi],
           [21, 3, BLUE,   0, 0, True,  0.023, 16, 0.1, False, True, 45, pi],
           [18, 2, BLUE,   0, 0, True,  0.022, 13, 0.1, False, True, 58, 0.00],
           [11, 2, BLUE,   0, 0, True,  0.015, 9,  0.1, False, True, 71, pi],
           [11, 2, BLUE,   0, 0, True,  0.015, 9,  0.1, False, True, 71, 0.95 * pi],
           [11, 2, BLUE,   0, 0, True,  0.015, 9,  0.4, False, True, 72, -0.95 * pi],
           [11, 2, BLUE,   0, 0, True,  0.015, 9,  0.7, False, True, 78, 0.68 * pi],
           [11, 2, BLUE,   0, 0, True,  0.015, 9,  0.9, False, True, 78, -0.68 * pi],
           # 51
           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_10 = ((125, (9, 13), (15, 28), (30, 32), (36, 44), (46, 47)),
                    (119, (9, 13), (15, 28), (30, 32), (36, 44), (46, 47), (49, 51)),
                    (116, (9, 13), (15, 28), (30, 32), (36, 44), (47, 51)),
                    (112, (9, 13), (15, 28), (30, 32), (36, 44), (46, 51)),
                    (106, (9, 13), (15, 28), (30, 32), (36, 44), (44, 45), (46, 51)),
                    (99, (9, 13), (15, 28), (30, 32), (36, 42), (43, 45), (46, 51)),
                    (92, (9, 13), (15, 28), (30, 32), (36, 41), (42, 45), (46, 51)),
                    (85, (9, 13), (15, 28), (30, 32), (36, 45), (46, 51)),
                    (84, (9, 28), (30, 32), (36, 44), (45, 51)),
                    (77, (9, 28), (30, 32), (36, 43), (44, 51)),
                    (70, (9, 28), (30, 32), (36, 42), (43, 51)),
                    (63, (9, 28), (30, 32), (41, 42), (43, 51)),
                    (61, (9, 28), (30, 32), (36, 37), (41, 42), (43, 51)),
                    (59, (9, 28), (30, 32), (39, 42), (43, 51)),
                    (57, (9, 28), (15, 28), (30, 32), (36, 42), (43, 51)),
                    (55, (9, 28), (30, 32), (37, 42), (43, 51)),
                    (53, (9, 28), (30, 32), (36, 42), (43, 51)),
                    (51, (9, 28), (30, 32), (42, 51)),
                    (49, (9, 28), (30, 32), (36, 37), (42, 51)),
                    (47, (9, 28), (30, 32), (39, 41), (42, 51)),
                    (45, (9, 13), (15, 28), (30, 32), (36, 41), (42, 51)),
                    (43, (9, 28), (30, 32), (37, 41), (42, 51)),
                    (41, (9, 28), (30, 32), (36, 41), (42, 51)),
                    (39, (9, 28), (30, 32), (41, 51)),
                    (37, (9, 28), (30, 32), (36, 37), (41, 49)),
                    (35, (9, 28), (30, 32), (39, 49)),
                    (33, (9, 13), (15, 28), (30, 32), (36, 51)),
                    (31, (9, 28), (30, 32), (37, 51)),
                    (29, (9, 28), (30, 32), (36, 51)),
                    (25, (9, 26), (30, 51)),
                    (21, (9, 26), (30, 51)),
                    (19, (20, 24), (26, 51)),
                    (12, (20, 22), (24, 51)),
                    (6,  (22, 51)))

PARAMS_10 = [MAX_HEALTH_10, HEALTH_STATES_10, RADIUS_10, BODY_10,
             MAX_VEL_10, ACC_10, GUN_TYPE_10, BG_RADIUS_10, SUPERPOWER_10]
###############################################################################
MAX_VEL_11 = 0.7
ACC_11 = 0.002
GUN_TYPE_11 = 'Gun11'
SUPERPOWER_11 = None
MAX_HEALTH_11 = 125
RADIUS_11 = 80
BG_RADIUS_11 = 130
BODY_11 = [[32, 4, BLUE,   0, 0, True,  0.033, 20, 0,   True,  True, 0,   0.00],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.9, True,  True, 39,  0.75 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.6, True,  True, 39,  -0.75 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.5, True,  True, 39,  0.6 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.2, True,  True, 39,  -0.6 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.9, True,  True, 54,  0.68 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.6, True,  True, 54,  -0.68 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.9, True,  True, 53,  0.57 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.6, True,  True, 53,  -0.57 * pi],
           [8,  1, BLUE,   0, 0, True,  0.011, 7,  0.3, True,  True, 39,  0.08 * pi],
           # 10
           [8,  1, BLUE,   0, 0, True,  0.011, 7,  0.7, True,  True, 39,  -0.08 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.6, True,  True, 53,  0.00],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.9, True,  True, 69,  0.63 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.6, True,  True, 69,  -0.63 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.9, True,  True, 71,  0.7 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.6, True,  True, 71,  -0.7 * pi],
           [12, 1, BLUE,   0, 0, True,  0.016, 10, 0.2, True,  True, 41,  0.91 * pi],
           [12, 1, BLUE,   0, 0, True,  0.016, 10, 0.5, True,  True, 41,  -0.91 * pi],
           [16, 2, BLUE,   0, 0, True,  0.02,  12, 0.2, False, True, 46,  0.9 * pi],
           [16, 2, BLUE,   0, 0, True,  0.02,  12, 0.5, False, True, 46,  -0.9 * pi],
           # 20
           [21, 2, BLUE,   0, 0, True,  0.025, 15, 0.2, False, True, 52,  0.89 * pi],
           [21, 2, BLUE,   0, 0, True,  0.025, 15, 0.5, False, True, 52,  -0.89 * pi],
           [12, 1, BLUE,   0, 0, True,  0.02,  12, 0.2, False, True, 42,  0.14 * pi],
           [12, 1, BLUE,   0, 0, True,  0.02,  12, 0.5, False, True, 42,  -0.14 * pi],
           [12, 1, BLUE,   0, 0, True,  0.02,  12, 0.4, False, True, 42,  0.3 * pi],
           [12, 1, BLUE,   0, 0, True,  0.02,  12, 0.0, False, True, 42,  -0.3 * pi],
           [12, 2, BLUE,   0, 0, True,  0.02,  12, 0.2, False, True, 42,  0.8 * pi],
           [12, 2, BLUE,   0, 0, True,  0.02,  12, 0.5, False, True, 42,  -0.8 * pi],
           [12, 2, BLUE,   0, 0, True,  0.02,  12, 0.4, False, True, 42,  0.64 * pi],
           [12, 2, BLUE,   0, 0, True,  0.02,  12, 0.0, False, True, 42,  -0.64 * pi],
           # 30
           [12, 1, BLUE,   0, 0, True,  0.02,  12, 0.7, False, True, 60,  0.22 * pi],
           [12, 1, BLUE,   0, 0, True,  0.02,  12, 0.9, False, True, 60,  -0.22 * pi],
           [12, 1, BLUE,   0, 0, True,  0.02,  12, 0.4, False, True, 60,  0.72 * pi],
           [12, 1, BLUE,   0, 0, True,  0.02,  12, 0.2, False, True, 60,  -0.72 * pi],
           [15, 2, BLUE,   0, 0, True,  0.025, 15, 0.6, False, True, 62,  0.22 * pi],
           [15, 2, BLUE,   0, 0, True,  0.025, 15, 0.9, False, True, 62,  -0.22 * pi],
           [15, 2, BLUE,   0, 0, True,  0.025, 15, 0.4, False, True, 62,  0.72 * pi],
           [15, 2, BLUE,   0, 0, True,  0.025, 15, 0.1, False, True, 62,  -0.72 * pi],
           [18, 2, BLUE,   0, 0, True,  0.027, 16, 0.7, False, True, 65,  0.22 * pi],
           [18, 2, BLUE,   0, 0, True,  0.027, 16, 0.9, False, True, 65,  -0.22 * pi],
           # 40
           [18, 2, BLUE,   0, 0, True,  0.027, 16, 0.4, False, True, 65,  0.72 * pi],
           [18, 2, BLUE,   0, 0, True,  0.027, 16, 0.1, False, True, 65,  -0.72 * pi],
           [21, 3, BLUE,   0, 0, True,  0.03,  18, 0.7, False, True, 68,  0.22 * pi],
           [21, 3, BLUE,   0, 0, True,  0.03,  18, 0.3, False, True, 68,  -0.22 * pi],
           [21, 3, BLUE,   0, 0, True,  0.03,  18, 0.4, False, True, 68,  0.72 * pi],
           [21, 3, BLUE,   0, 0, True,  0.03,  18, 0.1, False, True, 68,  -0.72 * pi],
           [24, 3, BLUE,   0, 0, True,  0.033, 20, 0.7, False, True, 71,  0.22 * pi],
           [24, 3, BLUE,   0, 0, True,  0.033, 20, 0.3, False, True, 71,  -0.22 * pi],
           [24, 3, BLUE,   0, 0, True,  0.033, 20, 0.4, False, True, 71,  0.72 * pi],
           [24, 3, BLUE,   0, 0, True,  0.033, 20, 0.1, False, True, 71,  -0.72 * pi],
           # 50
           [12, 1, BLUE,   0, 0, True,  0.016, 10, 0.0, False, True, 42,  pi],
           [17, 2, BLUE,   0, 0, True,  0.024, 14, 0.0, False, True, 46,  pi],
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.7, False, True, 98,  0.22 * pi],
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.9, False, True, 98,  -0.22 * pi],
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.4, False, True, 98,  0.72 * pi],
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.2, False, True, 98,  -0.72 * pi],
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.7, False, True, 98,  0.16 * pi],
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.9, False, True, 98,  -0.16 * pi],
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.3, False, True, 98,  0.28 * pi],
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.8, False, True, 98,  -0.28 * pi],
           # 60
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.1, False, True, 98,  0.66 * pi],
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.5, False, True, 98,  -0.66 * pi],
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.4, False, True, 98,  0.78 * pi],
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.2, False, True, 98,  -0.78 * pi],
           [22, 3, BLUE,   0, 0, True,  0.027, 16, 0.0, False, True, 51,  pi],
           [27, 3, BLUE,   0, 0, True,  0.021, 19, 0.0, False, True, 56,  pi],
           [32, 4, BLUE,   0, 0, True,  0.033, 22, 0.0, False, True, 61,  pi],
           [37, 5, BLUE,   0, 0, True,  0.038, 25, 0.0, False, True, 66,  pi],
           [42, 2, BLUE,   0, 0, True,  0.03,  18, 0.0, False, True, 66,  pi],
           [20, 2, BLUE,   0, 0, True,  0.03,  18, 0.7, False, True, 68,  0.28 * pi],
           [20, 2, BLUE,   0, 0, True,  0.03,  18, 0.3, False, True, 68,  -0.28 * pi],
           # 71
           [12, 1, BLUE,   0, 0, True,  0.02,  12, 0.2, False, True, 42,  0.2 * pi],
           [12, 1, BLUE,   0, 0, True,  0.02,  12, 0.5, False, True, 42,  -0.2 * pi],
           [12, 1, BLUE,   0, 0, True,  0.02,  12, 0.4, False, True, 42,  0.36 * pi],
           [12, 1, BLUE,   0, 0, True,  0.02,  12, 0.0, False, True, 42,  -0.36 * pi],
           [11, 1, BLUE,   0, 0, True,  0.02,  12, 0.8, False, True, 42,  0.00],
           [11, 1, BLUE,   0, 0, True,  0.02,  12, 0.1, False, True, 114, pi],
           [11, 1, BLUE,   0, 0, True,  0.02,  12, 0.3, False, True, 110, 0.92 * pi],
           [11, 1, BLUE,   0, 0, True,  0.02,  12, 0.7, False, True, 110, -0.92 * pi],
           # 79
           [16, 2, ORANGE, 0, 0, True,  0.025, 15, 0,   True,  True, 0,   0.00],
           [7,  1, ORANGE, 0, 0, True,  0.01,  6,  0,   True,  True, 20,  0.1 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.01,  6,  0.3, True,  True, 20,  -0.1 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.3, True,  True, 22,  0.75 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.7, True,  True, 22,  -0.75 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.9, True,  True, 22,  pi],
           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25,  0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23,  0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26,  -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27,  pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17,  -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29,  0.25 * pi]]

HEALTH_STATES_11 = ((125, (1, 26), (30, 48), (50, 60), (64, 68)),
                    (122, (1, 26), (30, 48), (50, 60), (64, 68), (76, 77)),
                    (120, (1, 26), (30, 48), (50, 60), (64, 68), (77, 79)),
                    (118, (1, 26), (30, 48), (50, 60), (64, 68), (76, 79)),
                    (116, (1, 26), (30, 48), (50, 60), (64, 68), (75, 79)),
                    (114, (1, 22), (30, 46), (50, 56), (64, 67), (68, 79)),
                    (109, (1, 22), (30, 46), (50, 56), (64, 66), (67, 79)),
                    (104, (1, 22), (30, 46), (50, 56), (64, 65), (66, 79)),
                    (99, (1, 22), (30, 46), (50, 56), (65, 79)),
                    (94, (1, 22), (30, 46), (50, 51), (52, 56), (64, 79)),
                    (89, (1, 22), (30, 46), (51, 56), (64, 79)),
                    (85, (1, 22), (30, 46), (50, 56), (64, 79)),
                    (83, (1, 22), (30, 46), (50, 51), (56, 79)),
                    (80, (1, 22), (30, 46), (51, 52), (56, 79)),
                    (77, (1, 22), (30, 46), (50, 52), (56, 79)),
                    (75, (1, 22), (30, 46), (50, 51), (52, 79)),
                    (72, (1, 22), (30, 46), (51, 79)),
                    (69, (1, 22), (30, 46), (50, 79)),
                    (59, (1, 22), (30, 42), (46, 79)),
                    (49, (1, 22), (30, 38), (42, 79)),
                    (39, (1, 22), (30, 34), (38, 79)),
                    (29, (1, 22), (34, 79)),
                    (19, (16, 20), (22, 79)),
                    (12, (16, 18), (20, 79)),
                    (6, (18, 79)))

PARAMS_11 = [MAX_HEALTH_11, HEALTH_STATES_11, RADIUS_11, BODY_11, MAX_VEL_11,
             ACC_11, GUN_TYPE_11, BG_RADIUS_11, SUPERPOWER_11]
###############################################################################

MAX_VEL_12 = 0.5
ACC_12 = 0.001
GUN_TYPE_12 = 'Gun12'
SUPERPOWER_12 = None
MAX_HEALTH_12 = 125
RADIUS_12 = 70
BG_RADIUS_12 = 130
BODY_12 = [[32, 2, BLUE,   0, 0, True,  0.026, 16, 0,   True,  True, 0,  0.00],
           [43, 2, BLUE,   0, 0, True,  0.029, 17, 0,   False, True, 0,  0.00],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.9, True,  True, 39, 0.73 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.6, True,  True, 39, -0.73 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.5, True,  True, 39, 0.62 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.2, True,  True, 39, -0.62 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02, 12, 0.9, True,  True, 54, 0.68 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.6, True,  True, 54, -0.68 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.2, True,  True, 40, 0.9 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.5, True,  True, 40, -0.9 * pi],
           # 10
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.9, True,  True, 53, 0.57 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.6, True,  True, 53, -0.57 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.4, True,  True, 69, 0.63 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.1, True,  True, 69, -0.63 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.5, True,  True, 71, 0.7 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.3, True,  True, 71, -0.7 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.9, False, True, 64, 0.68 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.6, False, True, 64, -0.68 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.9, False, True, 47, 0.73 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.6, False, True, 47, -0.73 * pi],
           # 20
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.5, False, True, 47, 0.62 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.2, False, True, 47, -0.62 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.1, False, True, 67, 0.32 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.3, False, True, 67, -0.32 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.9, False, True, 47, 0.27 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.6, False, True, 47, -0.27 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.5, False, True, 47, 0.38 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.2, False, True, 47, -0.38 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.8, False, True, 62, 0.59 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.1, False, True, 62, -0.59 * pi],
           # 30
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.8, False, True, 60, 0.58 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, False, True, 60, -0.58 * pi],
           [12, 2, BLUE,   0, 0, True,  0.014, 8,  0.8, False, True, 58, 0.57 * pi],
           [12, 2, BLUE,   0, 0, True,  0.014, 8,  0.1, False, True, 58, -0.57 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, False, True, 58, 0.47 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, False, True, 58, -0.47 * pi],
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.4, False, True, 58, 0.46 * pi],
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.7, False, True, 58, -0.46 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.2, False, True, 58, 0.44 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.8, False, True, 58, -0.44 * pi],
           # 40
           [11, 1, BLUE,   0, 0, True,  0.016, 10, 0.1, False, True, 48, pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.1, False, True, 49, pi],
           [18, 2, BLUE,   0, 0, True,  0.022, 13, 0.1, False, True, 51, pi],
           [22, 3, BLUE,   0, 0, True,  0.027, 16, 0.1, False, True, 52, pi],
           [26, 4, BLUE,   0, 0, True,  0.033, 20, 0.3, False, True, 54, pi],
           [13, 2, BLUE,   0, 0, True,  0.018, 11, 0.5, False, True, 60, 0.85 * pi],
           [13, 2, BLUE,   0, 0, True,  0.018, 11, 0.2, False, True, 60, -0.85 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.8, False, True, 62, 0.77 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.0, False, True, 62, -0.77 * pi],
           [27, 2, BLUE,   0, 0, True,  0.025, 15, 0.3, False, True, 54, pi],
           # 50
           [12, 2, BLUE,   0, 0, True,  0.014, 8,  0.8, False, True, 66, 0.57 * pi],
           [12, 2, BLUE,   0, 0, True,  0.014, 8,  0.1, False, True, 66, -0.57 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.9, False, True, 47, 0.22 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.6, False, True, 47, -0.22 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.5, False, True, 47, 0.33 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.2, False, True, 47, -0.33 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.1, False, True, 67, 0.27 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.3, False, True, 67, -0.27 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.9, False, True, 47, 0.17 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.6, False, True, 47, -0.17 * pi],
           # 60
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.5, False, True, 47, 0.28 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.2, False, True, 47, -0.28 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.1, False, True, 67, 0.22 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.3, False, True, 67, -0.22 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.9, False, True, 47, 0.13 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.6, False, True, 47, -0.13 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.5, False, True, 47, 0.24 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.2, False, True, 47, -0.24 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.1, False, True, 67, 0.18 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.3, False, True, 67, -0.18 * pi],
           # 70
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.9, False, True, 64, 0.58 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.6, False, True, 64, -0.58 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.9, False, True, 47, 0.63 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.6, False, True, 47, -0.63 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.5, False, True, 47, 0.52 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  5,  0.2, False, True, 47, -0.52 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.8, False, True, 62, 0.67 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.0, False, True, 62, -0.67 * pi],
           [12, 2, BLUE,   0, 0, True,  0.014, 8,  0.8, False, True, 66, 0.47 * pi],
           [12, 2, BLUE,   0, 0, True,  0.014, 8,  0.1, False, True, 66, -0.47 * pi],
           # 80
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.9, False, True, 47, 0.07 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.6, False, True, 47, -0.07 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.5, False, True, 47, 0.18 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.2, False, True, 47, -0.18 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.1, False, True, 67, 0.12 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.3, False, True, 67, -0.12 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.5, False, True, 47, 0.12 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.2, False, True, 47, -0.12 * pi],
           [11, 1, BLUE,   0, 0, True,  0.009, 5,  0.5, False, True, 47, 0.00],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.1, False, True, 69, 0.07 * pi],
           # 90
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.3, False, True, 69, -0.07 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.1, False, True, 69, 0.04 * pi],
           [15, 2, BLUE,   0, 0, True,  0.02,  12, 0.3, False, True, 69, -0.04 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.5, False, True, 69, 0.14 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.2, False, True, 69, -0.14 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.7, False, True, 81, pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.2, False, True, 78, 0.92 * pi],
           [8,  1, BLUE,   0, 0, True,  0.009, 5,  0.2, False, True, 78, -0.92 * pi],
           # 98
           [10, 1, ORANGE, 0, 0, True,  0.011, 7,  0,   True,  True, 26, 0.22 * pi],
           [10, 1, ORANGE, 0, 0, True,  0.011, 7,  0.4, True,  True, 26, -0.22 * pi],
           [10, 1, ORANGE, 0, 0, True,  0.011, 7,  0.7, True,  True, 41, 0.14 * pi],
           [10, 1, ORANGE, 0, 0, True,  0.011, 7,  0.2, True,  True, 41, -0.14 * pi],
           [25, 4, ORANGE, 0, 0, True,  0.033, 20, 0,   True,  True, 0,  0.00],
           [10, 1, ORANGE, 0, 0, True,  0.011, 7,  0,   True,  True, 32, 0.79 * pi],
           [10, 1, ORANGE, 0, 0, True,  0.011, 7,  0.4, True,  True, 32, -0.79 * pi],

           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_12 = ((125, (0, 1), (2, 45), (47, 49), (50, 70), (80, 86), (89, 91)),
                    (122, (0, 1), (2, 45), (47, 49), (50, 70), (80, 86), (89, 91), (95, 96)),
                    (118, (0, 1), (2, 45), (47, 49), (50, 70), (80, 86), (89, 91), (96, 98)),
                    (113, (0, 1), (2, 45), (47, 49), (50, 70), (80, 86), (89, 91), (95, 98)),
                    (109, (0, 1), (2, 45), (47, 49), (50, 70), (80, 86), (89, 91), (93, 98)),
                    (103, (0, 1), (2, 45), (47, 49), (50, 70), (80, 86), (91, 98)),
                    (97, (0, 1), (2, 45), (47, 49), (50, 70), (86, 98)),
                    (91, (0, 1), (2, 16), (22, 45), (51, 64), (70, 98)),
                    (86, (0, 1), (2, 16), (22, 45), (52, 58), (64, 98)),
                    (81, (0, 1), (4, 16), (22, 45), (58, 97)),
                    (75, (0, 1), (2, 16), (28, 45), (52, 97)),
                    (70, (0, 1), (2, 16), (28, 45), (50, 97)),
                    (65, (0, 1), (2, 16), (28, 32), (34, 47), (50, 98)),
                    (61, (0, 1), (2, 16), (28, 32), (34, 38), (40, 44), (45, 98)),
                    (55, (0, 1), (2, 16), (28, 32), (34, 38), (40, 43), (44, 98)),
                    (50, (0, 1), (2, 16), (28, 32), (34, 38), (40, 42), (43, 98)),
                    (45, (0, 1), (2, 16), (28, 32), (34, 38), (40, 41), (42, 98)),
                    (40, (0, 1), (2, 16), (28, 32), (34, 38), (41, 98)),
                    (35, (0, 1), (2, 16), (28, 32), (34, 38), (40, 98)),
                    (31, (0, 1), (2, 16), (28, 32), (34, 36), (38, 98)),
                    (27, (0, 1), (2, 16), (28, 32), (36, 98)),
                    (24, (0, 1), (2, 16), (28, 32), (34, 98)),
                    (21, (0, 1), (2, 16), (28, 30), (32, 98)),
                    (18, (0, 1), (2, 16), (30, 98)),
                    (15, (0, 1), (2, 16), (28, 98)),
                    (14, (0, 1), (2, 8), (10, 16), (22, 98)),
                    (7, (1, 2), (10, 98)),
                    (1, (1, 2), (16, 98)))

PARAMS_12 = [MAX_HEALTH_12, HEALTH_STATES_12, RADIUS_12, BODY_12, MAX_VEL_12,
             ACC_12, GUN_TYPE_12, BG_RADIUS_12, SUPERPOWER_12]
###############################################################################

MAX_VEL_20 = 0.7
ACC_20 = 0.003
GUN_TYPE_20 = 'Gun20'
SUPERPOWER_20 = 'Armor'
MAX_HEALTH_20 = 200
RADIUS_20 = 50
BG_RADIUS_20 = 100
BODY_20 = [[32, 4, BLUE,   0, 0, True,  0.036, 24, 0,   True,  True, 0,  0.00],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, True,  True, 41, 0.84 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, True,  True, 41, -0.84 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, True,  True, 41, 0.72 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, True,  True, 41, -0.72 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.2, True,  True, 41, 0.34 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.9, True,  True, 41, -0.34 * pi],
           [16, 2, BLUE,   0, 0, True,  0.02,  13, 0.9, True,  True, 59, 0.8 * pi],
           [16, 2, BLUE,   0, 0, True,  0.02,  13, 0.6, True,  True, 59, -0.8 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 8,  0.2, False, True, 41, 0.34 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 8,  0.9, False, True, 41, -0.34 * pi],
           # 11
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.8, False, True, 41, 0.46 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, False, True, 41, -0.46 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.0, False, True, 41, 0.00],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.6, False, True, 54, 0.42 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.2, False, True, 54, -0.42 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.6, False, True, 55, 0.42 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.2, False, True, 55, -0.42 * pi],
           [12, 1, BLUE,   0, 0, True,  0.016, 9,  0.6, False, True, 58, 0.4 * pi],
           [12, 1, BLUE,   0, 0, True,  0.016, 9,  0.2, False, True, 58, -0.4 * pi],
           # 20
           [14, 2, BLUE,   0, 0, True,  0.018, 11, 0.6, False, True, 60, 0.39 * pi],
           [14, 2, BLUE,   0, 0, True,  0.018, 11, 0.2, False, True, 60, -0.39 * pi],
           [16, 2, BLUE,   0, 0, True,  0.02,  13, 0.4, False, True, 62, 0.39 * pi],
           [16, 2, BLUE,   0, 0, True,  0.02,  13, 0.1, False, True, 62, -0.39 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, False, True, 41, 0.12 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, False, True, 41, -0.12 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.0, False, True, 80, 0.8 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, False, True, 80, -0.8 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.2, False, True, 56, 0.68 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.6, False, True, 56, -0.68 * pi],
           # 30
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, False, True, 78, 0.34 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, False, True, 78, -0.34 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, False, True, 68, 0.49 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.8, False, True, 68, -0.49 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.0, False, True, 38, 0.00],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.3, False, True, 38, 0.11 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.7, False, True, 38, -0.11 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.3, False, True, 38, 0.15 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.7, False, True, 38, -0.15 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, False, True, 41, 0.93 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, False, True, 41, -0.93 * pi],
           # 41
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, False, True, 41, 0.81 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, False, True, 41, -0.81 * pi],
           [16, 2, BLUE,   0, 0, True,  0.02,  13, 0.9, False, True, 59, 0.89 * pi],
           [16, 2, BLUE,   0, 0, True,  0.02,  13, 0.6, False, True, 59, -0.89 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.0, False, True, 80, 0.89 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, False, True, 80, -0.89 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.2, False, True, 56, 0.77 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.6, False, True, 56, -0.77 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 8,  0.2, False, True, 41, 0.43 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 8,  0.9, False, True, 41, -0.43 * pi],
           # 51
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.8, False, True, 41, 0.55 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, False, True, 41, -0.55 * pi],
           [16, 2, BLUE,   0, 0, True,  0.02,  13, 0.4, False, True, 62, 0.48 * pi],
           [16, 2, BLUE,   0, 0, True,  0.02,  13, 0.1, False, True, 62, -0.48 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, False, True, 72, 0.4 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, False, True, 72, -0.4 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, False, True, 68, 0.58 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.8, False, True, 68, -0.58 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, False, True, 41, 0.87 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, False, True, 41, -0.87 * pi],
           # 61
           [16, 2, BLUE,   0, 0, True,  0.02,  13, 0.9, False, True, 59, 0.93 * pi],
           [16, 2, BLUE,   0, 0, True,  0.02,  13, 0.6, False, True, 59, -0.93 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, False, True, 55, 0.82 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, False, True, 55, -0.82 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.0, False, True, 80, 0.93 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, False, True, 80, -0.93 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, False, True, 41, pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 8,  0.1, False, True, 41, pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 8,  0.8, False, True, 41, 0.55 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 8,  0.4, False, True, 41, -0.55 * pi],
           # 71
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.1, False, True, 41, pi],
           [12, 1, BLUE,   0, 0, True,  0.017, 10, 0.1, False, True, 41, pi],
           [13, 1, BLUE,   0, 0, True,  0.017, 10, 0.1, False, True, 42, pi],
           [14, 2, BLUE,   0, 0, True,  0.018, 11, 0.1, False, True, 42, pi],
           [15, 2, BLUE,   0, 0, True,  0.019, 12, 0.1, False, True, 43, pi],
           [16, 2, BLUE,   0, 0, True,  0.02,  13, 0.3, False, True, 43, pi],
           [17, 2, BLUE,   0, 0, True,  0.02,  13, 0.3, False, True, 43, pi],
           [18, 2, BLUE,   0, 0, True,  0.022, 14, 0.3, False, True, 43, pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.3, False, True, 38, 0.22 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.7, False, True, 38, -0.22 * pi],
           # 81
           [16, 2, ORANGE, 0, 0, True,  0.024, 15, 0,   True,  True, 0,  0.00],
           [7,  1, ORANGE, 0, 0, True,  0.007, 5,  0,   True,  True, 18, 0.00],
           [7,  1, ORANGE, 0, 0, True,  0.007, 5,  0.3, True,  True, 19, 0.23 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.007, 5,  0.7, True,  True, 19, -0.23 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.3, True,  True, 21, 0.76 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.7, True,  True, 21, -0.76 * pi],
           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_20 = ((200, (1, 34), (35, 49), (59, 61), (67, 78)),
                    (183, (1, 35), (37, 49), (59, 61), (67, 78), (79, 81)),
                    (178, (1, 34), (35, 49), (59, 61), (67, 78), (79, 81)),
                    (173, (1, 34), (35, 49), (59, 61), (67, 77), (78, 81)),
                    (168, (1, 34), (35, 49), (59, 61), (67, 76), (77, 81)),
                    (163, (1, 34), (35, 49), (59, 61), (67, 75), (76, 81)),
                    (158, (1, 34), (35, 49), (59, 61), (67, 74), (75, 81)),
                    (153, (1, 34), (35, 49), (59, 61), (67, 73), (74, 81)),
                    (148, (1, 34), (35, 49), (59, 61), (67, 72), (73, 81)),
                    (143, (1, 34), (35, 49), (59, 61), (67, 71), (72, 79)),
                    (138, (1, 34), (35, 49), (51, 53), (59, 61), (67, 68), (71, 81)),
                    (133, (1, 34), (35, 49), (59, 61), (67, 68), (69, 81)),
                    (128, (1, 34), (35, 49), (59, 61), (68, 81)),
                    (123, (1, 34), (35, 37), (39, 49), (67, 81)),
                    (118, (1, 34), (35, 37), (59, 81)),
                    (113, (1, 9), (13, 22), (24, 30), (35, 37), (49, 81)),
                    (108, (5, 7), (13, 22), (24, 26), (35, 37), (39, 81)),
                    (103, (5, 7), (13, 22), (24, 26), (34, 35), (37, 81)),
                    (98, (5, 7), (13, 22), (24, 26), (35, 81)),
                    (93, (5, 7), (13, 22), (24, 26), (34, 81)),
                    (88, (5, 7), (13, 22), (32, 81)),
                    (83, (5, 7), (14, 22), (24, 26), (32, 81)),
                    (78, (5, 7), (13, 22), (24, 26), (32, 81)),
                    (73, (5, 7), (13, 22), (30, 81)),
                    (68, (5, 7), (14, 22), (24, 26), (30, 81)),
                    (63, (5, 7), (13, 22), (24, 26), (30, 81)),
                    (58, (5, 7), (14, 22), (24, 26), (28, 81)),
                    (53, (5, 7), (13, 22), (24, 26), (28, 81)),
                    (49, (5, 7), (13, 22), (24, 81)),
                    (48, (5, 7), (13, 22), (26, 81)),
                    (44, (5, 7), (14, 22), (24, 81)),
                    (37, (5, 7), (14, 20), (22, 81)),
                    (30, (5, 7), (14, 18), (20, 81)),
                    (24, (5, 7), (14, 16), (18, 81)),
                    (18, (5, 7), (16, 81)),
                    (12, (5, 7), (14, 81)),
                    (9, (5, 7), (13, 81)),
                    (6, (5, 7), (11, 81)),
                    (3, (9, 81)))

PARAMS_20 = [MAX_HEALTH_20, HEALTH_STATES_20, RADIUS_20, BODY_20, MAX_VEL_20,
             ACC_20, GUN_TYPE_20, BG_RADIUS_20, SUPERPOWER_20]
###############################################################################

MAX_VEL_21 = 0.65
ACC_21 = 0.003
GUN_TYPE_21 = 'Gun21'
SUPERPOWER_21 = 'Armor'
MAX_HEALTH_21 = 200
RADIUS_21 = 70
BG_RADIUS_21 = 100
BODY_21 = [[10, 1, BLUE,   0, 0, True,  0.014, 8,  0.1, True,  True, 47, 0.06 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.4, True,  True, 47, -0.06 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.7, True,  True, 47, 0.94 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.2, True,  True, 47, -0.94 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.1, False, True, 47, 0.09 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.4, False, True, 47, -0.09 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.1, False, True, 47, 0.12 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.4, False, True, 47, -0.12 * pi],
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.1, False, True, 47, 0.14 * pi],
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.4, False, True, 47, -0.14 * pi],
           # 10
           [12, 1, BLUE,   0, 0, True,  0.016, 10, 0.1, False, True, 47, 0.16 * pi],
           [12, 1, BLUE,   0, 0, True,  0.016, 10, 0.4, False, True, 47, -0.16 * pi],
           [13, 2, BLUE,   0, 0, True,  0.017, 11, 0.1, False, True, 47, 0.18 * pi],
           [13, 2, BLUE,   0, 0, True,  0.017, 11, 0.4, False, True, 47, -0.18 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.1, False, True, 47, 0.21 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.4, False, True, 47, -0.21 * pi],
           [28, 1, BLUE,   0, 0, True,  0.018, 10, 0.8, False, True, 58, 0.00],
           [6,  1, BLUE,   0, 0, True,  0.006, 4,  0.4, True,  True, 57, 0.00],
           [41, 2, BLUE,   0, 0, True,  0.028, 17, 0,   True,  True, 0,  0.00],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.5, True,  True, 51, 0.76 * pi],
           # 20
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.2, True,  True, 51, -0.76 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.5, True,  True, 72, 0.76 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.9, True,  True, 72, -0.76 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.3, False, True, 59, 0.00],
           [12, 1, BLUE,   0, 0, True,  0.016, 9,  0.3, False, True, 61, 0.00],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.8, False, True, 63, 0.00],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.8, False, True, 64, 0.00],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.3, False, True, 59, pi],
           [12, 1, BLUE,   0, 0, True,  0.016, 9,  0.7, False, True, 59, pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.3, False, True, 59, pi],
           # 30
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.3, False, True, 59, pi],
           [20, 1, BLUE,   0, 0, True,  0.018, 10, 0.3, False, True, 60, pi],
           [22, 1, BLUE,   0, 0, True,  0.018, 10, 0.3, False, True, 60, pi],
           [24, 1, BLUE,   0, 0, True,  0.018, 10, 0.3, False, True, 60, pi],
           [26, 1, BLUE,   0, 0, True,  0.018, 10, 0.3, False, True, 60, pi],
           [28, 1, BLUE,   0, 0, True,  0.018, 10, 0.3, False, True, 60, pi],
           [30, 1, BLUE,   0, 0, True,  0.018, 10, 0.3, False, True, 60, pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.2, False, True, 70, 0.825 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.6, False, True, 70, -0.825 * pi],
           [31, 1, BLUE,   0, 0, True,  0.018, 10, 0.3, False, True, 60, pi],
           # 40
           [32, 1, BLUE,   0, 0, True,  0.018, 10, 0.3, False, True, 60, pi],
           [20, 1, BLUE,   0, 0, True,  0.015, 8,  0.8, False, True, 66, 0.00],
           [22, 1, BLUE,   0, 0, True,  0.017, 9,  0.8, False, True, 66, 0.00],
           [24, 1, BLUE,   0, 0, True,  0.018, 10, 0.8, False, True, 67, 0.00],
           [26, 1, BLUE,   0, 0, True,  0.018, 10, 0.8, False, True, 68, 0.00],
           [28, 1, BLUE,   0, 0, True,  0.018, 10, 0.8, False, True, 68, 0.00],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.3, False, True, 87, 0.00],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.3, False, True, 80, 0.085 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.6, False, True, 80, -0.085 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.3, False, True, 74, 0.11 * pi],
           # 50
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.6, False, True, 74, -0.11 * pi],
           [8,  1, BLUE,   0, 0, True,  0.011, 6,  0.7, False, True, 44, 0.39 * pi],
           [8,  1, BLUE,   0, 0, True,  0.011, 6,  0.2, False, True, 44, -0.39 * pi],
           [8,  1, BLUE,   0, 0, True,  0.011, 6,  0.4, False, True, 46, 0.56 * pi],
           [8,  1, BLUE,   0, 0, True,  0.011, 6,  0.9, False, True, 46, -0.56 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.0, False, True, 92, pi],
           # 56
           [20, 3, ORANGE, 0, 0, True,  0.025, 15, 0.0, True,  True, 0,  0.00],
           [10, 1, ORANGE, 0, 0, True,  0.014, 8,  0.7, True,  True, 26, pi],
           [10, 1, ORANGE, 0, 0, True,  0.014, 8,  0.1, True,  True, 26, 0.73 * pi],
           [10, 1, ORANGE, 0, 0, True,  0.014, 8,  0.4, True,  True, 26, -0.73 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.9, True,  True, 18, 0.00],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.6, True,  True, 27, 0.00],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.9, True,  True, 23, 0.23 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.9, True,  True, 23, -0.23 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.6, True,  True, 31, 0.17 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.6, True,  True, 31, -0.17 * pi],
           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_21 = ((200, (0, 2), (4, 14), (17, 18), (21, 37), (39, 40), (41, 51)),
                    (195, (0, 2), (4, 14), (17, 18), (21, 37), (39, 40), (41, 51), (55, 56)),
                    (188, (0, 2), (4, 14), (17, 18), (21, 37), (39, 40), (41, 46), (47, 49), (51, 56)),
                    (183, (0, 2), (4, 14), (17, 18), (21, 37), (39, 40), (41, 47), (49, 56)),
                    (178, (0, 2), (4, 14), (17, 18), (21, 37), (39, 40), (41, 46), (47, 56)),
                    (173, (0, 2), (4, 14), (16, 18), (21, 37), (39, 40), (41, 45), (46, 56)),
                    (161, (0, 2), (4, 12), (14, 18), (21, 37), (39, 40), (41, 45), (46, 56)),
                    (150, (0, 2), (4, 10), (12, 18), (21, 37), (39, 40), (41, 45), (46, 56)),
                    (139, (0, 2), (4, 8), (10, 18), (21, 37), (39, 40), (41, 45), (46, 56)),
                    (128, (0, 2), (4, 6), (8, 18), (21, 37), (39, 40), (41, 45), (46, 56)),
                    (118, (0, 2), (4, 6), (8, 18), (21, 37), (39, 40), (41, 44), (45, 56)),
                    (108, (0, 2), (4, 6), (8, 18), (21, 37), (39, 40), (41, 43), (44, 56)),
                    (98, (0, 2), (4, 6), (8, 18), (21, 37), (39, 40), (41, 42), (43, 56)),
                    (93, (0, 2), (6, 18), (21, 37), (39, 40), (42, 56)),
                    (88, (0, 2), (6, 18), (21, 26), (27, 36), (39, 40), (41, 56)),
                    (78, (4, 18), (21, 26), (27, 37), (39, 40), (41, 56)),
                    (73, (4, 18), (21, 26), (27, 37), (40, 56)),
                    (68, (4, 18), (21, 26), (27, 36), (39, 56)),
                    (63, (4, 18), (23, 26), (27, 36), (37, 56)),
                    (59, (4, 18), (23, 26), (27, 35), (36, 56)),
                    (54, (4, 18), (23, 26), (27, 34), (35, 56)),
                    (49, (4, 18), (23, 26), (27, 33), (34, 56)),
                    (44, (4, 18), (23, 26), (27, 32), (33, 56)),
                    (39, (4, 18), (23, 26), (27, 31), (32, 56)),
                    (34, (4, 18), (23, 26), (27, 30), (31, 56)),
                    (30, (4, 18), (23, 26), (27, 29), (30, 56)),
                    (25, (4, 18), (23, 26), (27, 28), (29, 56)),
                    (20, (4, 18), (23, 26), (28, 56)),
                    (18, (4, 18), (23, 26), (27, 56)),
                    (16, (4, 18), (23, 25), (26, 56)),
                    (12, (4, 18), (23, 24), (25, 56)),
                    (8, (4, 18), (24, 56)),
                    (4, (4, 17), (23, 56)))

PARAMS_21 = [MAX_HEALTH_21, HEALTH_STATES_21, RADIUS_21, BODY_21, MAX_VEL_21,
             ACC_21, GUN_TYPE_21, BG_RADIUS_21, SUPERPOWER_21]
###############################################################################

MAX_VEL_22 = 0.5
ACC_22 = 0.002
GUN_TYPE_22 = 'Gun22'
SUPERPOWER_22 = 'Bombs'
MAX_HEALTH_22 = 200
RADIUS_22 = 70
BG_RADIUS_22 = 115
BODY_22 = [[9,  1, BLUE,         0, 0, True,  0.012, 7,  0.1, True,  True, 75, 0.04 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.4, True,  True, 75, -0.04 * pi],
           [6,  1, BLUE,         0, 0, True,  0.01,  6,  0.4, True,  True, 84, 0.00],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.4, False, True, 84, 0.00],
           [12, 2, BLUE,         0, 0, True,  0.014, 8,  0.4, False, True, 84, 0.00],
           [16, 2, BLUE,         0, 0, True,  0.02,  12, 0.4, False, True, 84, 0.00],
           [20, 3, BLUE,         0, 0, True,  0.026, 15, 0.4, False, True, 84, 0.00],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.5, False, True, 58, 0.3 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.9, False, True, 58, -0.3 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.0, False, True, 51, 0.37 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.4, False, True, 51, -0.37 * pi],
           # 11
           [14, 1, BLUE,         0, 0, True,  0.012, 7,  0.5, False, True, 28, 0.74 * pi],
           [14, 1, BLUE,         0, 0, True,  0.012, 7,  0.2, False, True, 28, -0.74 * pi],
           [17, 1, BLUE,         0, 0, True,  0.015, 9,  0.5, False, True, 31, 0.73 * pi],
           [17, 1, BLUE,         0, 0, True,  0.015, 9,  0.2, False, True, 31, -0.73 * pi],
           [20, 1, BLUE,         0, 0, True,  0.016, 10, 0.5, False, True, 34, 0.72 * pi],
           [20, 1, BLUE,         0, 0, True,  0.016, 10, 0.2, False, True, 34, -0.72 * pi],
           [24, 1, BLUE,         0, 0, True,  0.018, 11, 0.5, False, True, 37, 0.71 * pi],
           [24, 1, BLUE,         0, 0, True,  0.018, 11, 0.2, False, True, 37, -0.71 * pi],
           [28, 1, BLUE,         0, 0, True,  0.02,  12, 0.5, False, True, 42, 0.68 * pi],
           [28, 1, BLUE,         0, 0, True,  0.02,  12, 0.2, False, True, 42, -0.68 * pi],
           # 21
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.5, False, True, 64, 0.25 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.9, False, True, 64, -0.25 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.0, False, True, 56, 0.33 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.4, False, True, 56, -0.33 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.5, False, True, 66, 0.21 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.9, False, True, 66, -0.21 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.0, False, True, 60, 0.29 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.4, False, True, 60, -0.29 * pi],
           [18, 2, BLUE,         0, 0, True,  0.022, 13, 0.1, False, True, 48, 0.47 * pi],
           [18, 2, BLUE,         0, 0, True,  0.022, 13, 0.6, False, True, 48, -0.47 * pi],
           # 31
           [43, 2, BLUE,         0, 0, True,  0.028, 17, 0,   True,  True, 26, 0.00],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.5, True,  True, 28, 0.74 * pi],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.2, True,  True, 28, -0.74 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.1, True,  True, 46, 0.78 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.4, True,  True, 46, -0.78 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.3, False, True, 73, 0.08 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.7, False, True, 73, -0.08 * pi],
           [6,  1, BLUE,         0, 0, True,  0.006, 4,  0.4, False, True, 65, 0.36 * pi],
           [6,  1, BLUE,         0, 0, True,  0.006, 4,  0.8, False, True, 65, -0.36 * pi],
           [8,  1, BLUE,         0, 0, True,  0.01,  6,  0.4, False, True, 65, 0.36 * pi],
           # 41
           [8,  1, BLUE,         0, 0, True,  0.01,  6,  0.8, False, True, 65, -0.36 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.4, False, True, 67, 0.365 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.8, False, True, 67, -0.365 * pi],
           [12, 1, BLUE,         0, 0, True,  0.016, 9,  0.4, False, True, 68, 0.37 * pi],
           [12, 1, BLUE,         0, 0, True,  0.016, 9,  0.8, False, True, 68, -0.37 * pi],
           [15, 2, BLUE,         0, 0, True,  0.019, 11, 0.4, False, True, 69, 0.375 * pi],
           [15, 2, BLUE,         0, 0, True,  0.019, 11, 0.8, False, True, 69, -0.375 * pi],
           [18, 2, BLUE,         0, 0, True,  0.022, 13, 0.4, False, True, 71, 0.377 * pi],
           [18, 2, BLUE,         0, 0, True,  0.022, 13, 0.8, False, True, 71, -0.377 * pi],
           [10, 1, BLUE,         0, 0, True,  0.012, 7,  0.1, False, True, 29, 0.76 * pi],
           # 51
           [10, 1, BLUE,         0, 0, True,  0.012, 7,  0.6, False, True, 29, -0.76 * pi],
           [12, 2, BLUE,         0, 0, True,  0.016, 8,  0.2, False, True, 60, 0.84 * pi],
           [12, 2, BLUE,         0, 0, True,  0.016, 8,  0.9, False, True, 60, -0.84 * pi],
           [18, 2, BLUE,         0, 0, True,  0.022, 13, 0.4, False, True, 77, 0.32 * pi],
           [18, 2, BLUE,         0, 0, True,  0.022, 13, 0.8, False, True, 77, -0.32 * pi],
           [18, 2, BLUE,         0, 0, True,  0.022, 13, 0.4, False, True, 81, 0.28 * pi],
           [18, 2, BLUE,         0, 0, True,  0.022, 13, 0.8, False, True, 81, -0.28 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.2, False, True, 54, 0.5 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.6, False, True, 54, -0.5 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.0, False, True, 68, 0.6 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.8, False, True, 68, -0.6 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.0, False, True, 72, 0.715 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.8, False, True, 72, -0.715 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.2, False, True, 48, 0.47 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.6, False, True, 48, -0.47 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.0, False, True, 64, 0.55 * pi],
           [9,  1, BLUE,         0, 0, True,  0.012, 7,  0.8, False, True, 64, -0.55 * pi],
           [20, 3, ORANGE,       0, 0, True,  0.025, 15, 0.0, True,  True, 26, 0.00],
           [10, 1, ORANGE,       0, 0, True,  0.014, 8,  0,   True,  True, 24, 0.36 * pi],
           [10, 1, ORANGE,       0, 0, True,  0.014, 8,  0.4, True,  True, 24, -0.36 * pi],
           [10, 1, ORANGE,       0, 0, True,  0.014, 8,  0.7, True,  True, 0,  0.00],
           [6,  1, ORANGE,       0, 0, True,  0.01,  6,  0.9, True,  True, 43, 0.00],
           [6,  1, ORANGE,       0, 0, True,  0.01,  6,  0.6, True,  True, 52, 0.00],
           [6,  1, ORANGE,       0, 0, True,  0.01,  6,  0.2, True,  True, 45, 0.118 * pi],
           [6,  1, ORANGE,       0, 0, True,  0.01,  6,  0.4, True,  True, 54, 0.098 * pi],
           [6,  1, ORANGE,       0, 0, True,  0.01,  6,  0.6, True,  True, 45, -0.118 * pi],
           [6,  1, ORANGE,       0, 0, True,  0.01,  6,  0.8, True,  True, 54, -0.098 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.9, True,  True, 33, 0.85 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.6, True,  True, 33, -0.85 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.7, True,  True, 43, 0.888 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.4, True,  True, 43, -0.888 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.5, True,  True, 54, 0.91 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.2, True,  True, 54, -0.91 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.3, True,  True, 65, 0.925 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.0, True,  True, 65, -0.925 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.1, True,  True, 76, 0.935 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.8, True,  True, 76, -0.935 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.9, True,  True, 87, 0.944 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.6, True,  True, 87, -0.944 * pi],
           [13, 2, LIGHT_ORANGE, 0, 0, False, 0,     0,  0,   True,  True, 33, 0.85 * pi,   True, pi],
           [13, 2, LIGHT_ORANGE, 0, 0, False, 0,     0,  0,   True,  True, 33, -0.85 * pi,  True, pi],
           [14, 2, ORANGE,       0, 0, True,  0.02,  12, 0,   True,  True, 30, pi],
           [17, 1, VIOLET,       0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET,       0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET,       0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET,       0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET,       0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET,       0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_22 = ((200, (0, 6), (7, 19), (21, 25), (32, 36), (38, 50), (54, 56), (58, 66)),
                    (168, (0, 6), (7, 19), (21, 25), (32, 36), (38, 50), (54, 56), (58, 62), (64, 66)),
                    (158, (0, 6), (7, 19), (21, 25), (32, 36), (38, 50), (54, 56), (58, 60), (64, 68)),
                    (143, (0, 6), (7, 19), (21, 25), (29, 31), (32, 36), (38, 50), (54, 56), (58, 60), (66, 68)),
                    (128, (0, 6), (7, 19), (21, 25), (29, 31), (32, 36), (38, 50), (54, 56), (64, 68)),
                    (118, (0, 6), (7, 19), (21, 25), (29, 31), (32, 36), (38, 50), (54, 56), (62, 68)),
                    (108, (0, 6), (7, 19), (21, 25), (29, 31), (32, 36), (38, 50), (54, 56), (60, 68)),
                    (98, (0, 6), (7, 19), (21, 25), (29, 31), (32, 36), (38, 50), (54, 56), (58, 68)),
                    (88, (0, 6), (7, 19), (25, 31), (32, 36), (38, 50), (56, 68)),
                    (83, (0, 6), (11, 19), (21, 31), (32, 36), (38, 48), (54, 68)),
                    (78, (0, 6), (11, 19), (21, 31), (32, 34), (38, 48), (50, 68)),
                    (73, (0, 6), (11, 17), (19, 31), (32, 34), (38, 48), (50, 68)),
                    (68, (0, 6), (11, 15), (17, 31), (32, 34), (38, 48), (50, 68)),
                    (63, (0, 6), (11, 13), (15, 31), (32, 34), (38, 48), (50, 68)),
                    (58, (0, 6), (13, 31), (32, 34), (38, 48), (50, 68)),
                    (53, (0, 6), (11, 31), (38, 48), (50, 68)),
                    (48, (0, 6), (11, 31), (38, 46), (48, 68)),
                    (44, (0, 6), (11, 31), (38, 44), (46, 68)),
                    (40, (0, 6), (11, 31), (38, 42), (44, 68)),
                    (36, (0, 6), (11, 31), (38, 40), (42, 68)),
                    (32, (0, 6), (11, 31), (40, 68)),
                    (28, (0, 6), (11, 31), (38, 68)),
                    (23, (0, 6), (9, 31), (38, 68)),
                    (18, (0, 6), (7, 31), (38, 68)),
                    (14, (2, 6), (7, 31), (36, 68)),
                    (11, (2, 5), (6, 31), (36, 68)),
                    (8, (2, 4), (5, 31), (36, 68)),
                    (5, (2, 3), (4, 31), (36, 68)),
                    (2, (3, 31), (36, 68)))

PARAMS_22 = [MAX_HEALTH_22, HEALTH_STATES_22, RADIUS_22, BODY_22, MAX_VEL_22,
             ACC_22, GUN_TYPE_22, BG_RADIUS_22, SUPERPOWER_22]
###############################################################################
MAX_VEL_23 = 0.4
ACC_23 = 0.001
GUN_TYPE_23 = 'Gun23'
SUPERPOWER_23 = 'Bombs'
MAX_HEALTH_23 = 200
RADIUS_23 = 70
BG_RADIUS_23 = 125
BODY_23 = [[14, 2, BLUE,         0, 0, True,  0.02,  12, 0.6, False, True, 56,  0.38 * pi],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.0, False, True, 56,  -0.38 * pi],
           [18, 2, BLUE,         0, 0, True,  0.027, 16, 0.6, False, True, 59,  0.38 * pi],
           [18, 2, BLUE,         0, 0, True,  0.027, 16, 0.0, False, True, 59,  -0.38 * pi],
           [22, 3, BLUE,         0, 0, True,  0.03,  18, 0.6, False, True, 65,  0.36 * pi],
           [22, 3, BLUE,         0, 0, True,  0.03,  18, 0.0, False, True, 65,  -0.36 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.1, False, True, 74,  0.14 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.4, False, True, 74,  -0.14 * pi],
           [22, 3, BLUE,         0, 0, True,  0.023, 14, 0.2, False, True, 104, 0.755 * pi],
           [22, 3, BLUE,         0, 0, True,  0.023, 14, 0.7, False, True, 104, -0.755 * pi],
           # 10
           [28, 2, BLUE,         0, 0, True,  0.02,  11, 0.4, False, True, 108, -0.755 * pi],
           [28, 2, BLUE,         0, 0, True,  0.02,  11, 0,   False, True, 108, 0.755 * pi],
           [22, 3, BLUE,         0, 0, True,  0.03,  18, 0.1, False, True, 52,  0.51 * pi],
           [22, 3, BLUE,         0, 0, True,  0.03,  18, 0.9, False, True, 52,  -0.51 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.9, True,  True, 70,  0.17 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.6, True,  True, 70,  -0.17 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.6, True,  True, 66,  0.25 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.3, True,  True, 66,  -0.25 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.1, True,  True, 75,  0.04 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.4, True,  True, 75,  -0.04 * pi],
           # 20
           [6,  1, BLUE,         0, 0, True,  0.009, 5,  0.4, True,  True, 84,  0.00],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.3, False, True, 66,  0.17 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.7, False, True, 66,  -0.17 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.9, False, True, 61,  0.25 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.2, False, True, 61,  -0.25 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.1, False, True, 71,  0.04 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.4, False, True, 71,  -0.04 * pi],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.3, False, True, 84,  0.00],
           [17, 2, BLUE,         0, 0, True,  0.023, 14, 0.1, False, True, 52,  0.51 * pi],
           [17, 2, BLUE,         0, 0, True,  0.023, 14, 0.8, False, True, 52,  -0.51 * pi],
           # 30
           [43, 2, BLUE,         0, 0, True,  0.028, 17, 0,   True,  True, 26,  0.00],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.5, True,  True, 28,  0.74 * pi],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.2, True,  True, 28,  -0.74 * pi],
           [11, 1, BLUE,         0, 0, True,  0.016, 9,  0.9, True,  True, 86,  0.89 * pi],
           [11, 1, BLUE,         0, 0, True,  0.016, 9,  0.6, True,  True, 86,  -0.89 * pi],
           [32, 2, BLUE,         0, 0, True,  0.02,  12, 0.4, True,  True, 67,  0.755 * pi],
           [32, 2, BLUE,         0, 0, True,  0.02,  12, 0,   True,  True, 67,  -0.755 * pi],
           [11, 1, BLUE,         0, 0, True,  0.015, 9,  0.1, False, True, 52,  0.54 * pi],
           [11, 1, BLUE,         0, 0, True,  0.015, 9,  0.8, False, True, 52,  -0.54 * pi],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.9, True,  True, 40,  0.57 * pi],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.6, True,  True, 40,  -0.57 * pi],
           # 41
           [11, 1, BLUE,         0, 0, True,  0.015, 9,  0.4, False, True, 103, 0.79 * pi],
           [11, 1, BLUE,         0, 0, True,  0.015, 9,  0.7, False, True, 103, -0.79 * pi],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.0, False, True, 80,  -0.23 * pi],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.5, False, True, 80,  0.23 * pi],
           [11, 1, BLUE,         0, 0, True,  0.015, 9,  0.4, False, True, 97,  0.66 * pi],
           [11, 1, BLUE,         0, 0, True,  0.015, 9,  0.7, False, True, 97,  -0.66 * pi],
           [17, 2, BLUE,         0, 0, True,  0.023, 14, 0.3, False, True, 84,  0.00],
           [17, 2, BLUE,         0, 0, True,  0.023, 14, 0.0, False, True, 80,  -0.23 * pi],
           [17, 2, BLUE,         0, 0, True,  0.023, 14, 0.5, False, True, 80,  0.23 * pi],
           # 50
           [19, 2, BLUE,         0, 0, True,  0.032, 19, 0.0, False, True, 83,  -0.23 * pi],
           [19, 2, BLUE,         0, 0, True,  0.032, 19, 0.5, False, True, 83,  0.23 * pi],
           [28, 2, BLUE,         0, 0, True,  0.02,  12, 0.4, False, True, 95,  -0.23 * pi],
           [28, 2, BLUE,         0, 0, True,  0.02,  12, 0,   False, True, 95,  0.23 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.6, False, True, 53,  0.38 * pi],
           [10, 1, BLUE,         0, 0, True,  0.014, 8,  0.0, False, True, 53,  -0.38 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.2, False, True, 120, 0.3 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.7, False, True, 120, -0.3 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.5, False, True, 123, 0.19 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.0, False, True, 123, -0.19 * pi],
           # 60
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.5, False, True, 126, 0.82 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.9, False, True, 126, -0.82 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.2, False, True, 141, 0.74 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.7, False, True, 141, -0.74 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.2, False, True, 88,  0.085 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.0, False, True, 88,  -0.085 * pi],
           [28, 2, BLUE,         0, 0, True,  0.02,  12, 0.2, False, True, 107, -0.185 * pi],
           [28, 2, BLUE,         0, 0, True,  0.02,  12, 0.6, False, True, 107, 0.185 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.1, False, True, 130, 0.25 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.6, False, True, 130, -0.25 * pi],
           # 70
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.4, False, True, 137, 0.15 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.8, False, True, 137, -0.15 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.7, False, True, 141, 0.21 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.4, False, True, 141, -0.21 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.5, False, True, 110, 0.285 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.9, False, True, 110, -0.285 * pi],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.6, False, True, 138, 0.76 * pi],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.2, False, True, 138, -0.76 * pi],
           [28, 2, BLUE,         0, 0, True,  0.019, 11, 0.2, False, True, 95,  -0.13 * pi],
           [28, 2, BLUE,         0, 0, True,  0.019, 11, 0.8, False, True, 95,  0.13 * pi],
           # 80
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.7, False, True, 118, 0.2 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.4, False, True, 118, -0.2 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.5, False, True, 85,  0.245 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.9, False, True, 85,  -0.245 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.1, False, True, 57,  0.35 * pi],
           [11, 1, BLUE,         0, 0, True,  0.014, 8,  0.6, False, True, 57,  -0.35 * pi],
           [28, 2, BLUE,         0, 0, True,  0.02,  12, 0.2, False, True, 104, -0.23 * pi],
           [28, 2, BLUE,         0, 0, True,  0.02,  12, 0.6, False, True, 104, 0.23 * pi],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.3, False, True, 71,  0.25 * pi],
           [14, 2, BLUE,         0, 0, True,  0.02,  12, 0.7, False, True, 71,  -0.25 * pi],
           # 90
           [20, 3, ORANGE,       0, 0, True,  0.025, 15, 0,   True,  True, 26,  0.00],
           [10, 1, ORANGE,       0, 0, True,  0.014, 8,  0,   True,  True, 36,  0.23 * pi],
           [10, 1, ORANGE,       0, 0, True,  0.014, 8,  0.4, True,  True, 36,  -0.23 * pi],
           [10, 1, ORANGE,       0, 0, True,  0.014, 8,  0.7, True,  True, 0,   0.00],
           [6,  1, ORANGE,       0, 0, True,  0.009, 5,  0.9, True,  True, 43,  0.00],
           [6,  1, ORANGE,       0, 0, True,  0.009, 5,  0.6, True,  True, 52,  0.00],
           [6,  1, ORANGE,       0, 0, True,  0.009, 5,  0.2, True,  True, 45,  0.118 * pi],
           [6,  1, ORANGE,       0, 0, True,  0.009, 5,  0.4, True,  True, 54,  0.098 * pi],
           [6,  1, ORANGE,       0, 0, True,  0.009, 5,  0.2, True,  True, 45,  -0.118 * pi],
           [6,  1, ORANGE,       0, 0, True,  0.009, 5,  0.4, True,  True, 54,  -0.098 * pi],
           [6,  1, ORANGE,       0, 0, True,  0.009, 5,  0.7, True,  True, 49,  0.22 * pi],
           [6,  1, ORANGE,       0, 0, True,  0.009, 5,  0.1, True,  True, 57,  0.185 * pi],
           [6,  1, ORANGE,       0, 0, True,  0.009, 5,  0.7, True,  True, 49,  -0.22 * pi],
           [6,  1, ORANGE,       0, 0, True,  0.009, 5,  0.1, True,  True, 57,  -0.185 * pi],
           [7,  1, ORANGE,       0, 0, True,  0.01,  6,  0.9, True,  True, 33,  0.85 * pi],
           [7,  1, ORANGE,       0, 0, True,  0.01,  6,  0.6, True,  True, 33,  -0.85 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.7, True,  True, 43,  0.888 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.4, True,  True, 43,  -0.888 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.5, True,  True, 54,  0.91 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.2, True,  True, 54,  -0.91 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.3, True,  True, 65,  0.925 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.0, True,  True, 65,  -0.925 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.1, True,  True, 76,  0.935 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.8, True,  True, 76,  -0.935 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.9, True,  True, 87,  0.944 * pi],
           [8,  1, ORANGE,       0, 0, True,  0.012, 7,  0.6, True,  True, 87,  -0.944 * pi],
           [13, 2, LIGHT_ORANGE, 0, 0, False, 0,     0,  0,   True,  True, 33,  0.85 * pi,    True, pi],
           [13, 2, LIGHT_ORANGE, 0, 0, False, 0,     0,  0,   True,  True, 33,  -0.85 * pi,   True, pi],
           [14, 2, ORANGE,       0, 0, True,  0.02,  12, 0,   True,  True, 30,  pi],

           [17, 1, VIOLET,       0, 0, False, 0,     0,  0,   False, True, 25,  0.8 * pi],
           [8,  1, VIOLET,       0, 0, False, 0,     0,  0,   False, True, 23,  0.55 * pi],
           [8,  1, VIOLET,       0, 0, False, 0,     0,  0,   False, True, 26,  -0.45 * pi],
           [8,  1, VIOLET,       0, 0, False, 0,     0,  0,   False, True, 27,  pi],
           [8,  1, VIOLET,       0, 0, False, 0,     0,  0,   False, True, 17,  -0.9 * pi],
           [10, 1, VIOLET,       0, 0, False, 0,     0,  0,   False, True, 29,  0.25 * pi]]

HEALTH_STATES_23 = ((200, (0, 10), (14, 30), (37, 39), (41, 47), (48, 76), (78, 84)),
                    (188, (0, 10), (14, 25), (27, 30), (37, 39), (41, 47), (48, 76), (84, 90)),
                    (178, (0, 10), (14, 25), (27, 30), (37, 39), (41, 47), (48, 64), (68, 72), (78, 90)),
                    (168, (0, 10), (14, 25), (27, 30), (37, 39), (41, 47), (48, 60), (68, 72), (76, 90)),
                    (158, (0, 6), (8, 10), (14, 25), (27, 30), (37, 39), (41, 47), (48, 60), (64, 66), (72, 90)),
                    (148, (0, 4), (8, 10), (12, 25), (27, 28), (37, 39), (41, 47), (48, 52), (54, 56), (64, 90)),
                    (138, (0, 4), (8, 10), (12, 25), (27, 28), (37, 39), (41, 47), (48, 52), (54, 56), (62, 90)),
                    (128, (0, 4), (8, 10), (12, 25), (27, 28), (37, 39), (41, 47), (48, 52), (54, 56), (60, 90)),
                    (118, (0, 4), (10, 25), (27, 28), (37, 39), (41, 47), (48, 52), (54, 56), (60, 90)),
                    (108, (0, 4), (8, 25),  (27, 28), (37, 39), (41, 47), (48, 52), (54, 56), (60, 90)),
                    (98, (0, 4),  (8, 25),  (27, 28), (37, 39), (43, 45), (48, 52), (54, 90)),
                    (88, (0, 4),  (6, 21),  (27, 28), (37, 39), (43, 45), (48, 52), (54, 90)),
                    (81, (0, 2),  (4, 21),  (27, 28), (37, 39), (43, 45), (48, 52), (54, 90)),
                    (74, (2, 21), (27, 28), (37, 39), (43, 45), (48, 52), (54, 90)),
                    (68, (0, 21), (27, 28), (37, 39), (43, 45), (48, 52), (54, 90)),
                    (60, (0, 21), (27, 28), (37, 39), (43, 45), (48, 52), (54, 90)),
                    (53, (0, 21), (27, 30), (43, 45), (48, 52), (54, 90)),
                    (43, (0, 21), (27, 30), (37, 39), (43, 45), (48, 50), (52, 90)),
                    (38, (0, 21), (27, 30), (37, 39), (43, 45), (50, 90)),
                    (33, (0, 21), (28, 30), (37, 39), (47, 90)),
                    (23, (0, 14), (18, 20), (21, 25), (28, 30), (37, 39), (41, 90)),
                    (15, (0, 14), (18, 20), (21, 25), (28, 30), (37, 39), (41, 90)),
                    (10, (0, 14), (21, 30), (37, 39), (41, 90)))

PARAMS_23 = [MAX_HEALTH_23, HEALTH_STATES_23, RADIUS_23, BODY_23, MAX_VEL_23,
             ACC_00, GUN_TYPE_23, BG_RADIUS_23, SUPERPOWER_23]
###############################################################################
MAX_VEL_30 = 0.7
ACC_30 = 0.003
GUN_TYPE_30 = 'Gun30'
SUPERPOWER_30 = 'Teleportation'
MAX_HEALTH_30 = 400
RADIUS_30 = 60
BG_RADIUS_30 = 100
BODY_30 = [[32, 4, BLUE,   0, 0, True,  0.043, 26, 0,   True,  True, 0,  0.00],
           [10, 1, BLUE,   0, 0, True,  0.015, 8,  0.2, True,  True, 41, 0.43 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 8,  0.9, True,  True, 41, -0.43 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.8, True,  True, 41, 0.55 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, True,  True, 41, -0.55 * pi],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.4, True,  True, 62, 0.48 * pi],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.1, True,  True, 62, -0.48 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, True,  True, 72, 0.4 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, True,  True, 72, -0.4 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, True,  True, 68, 0.58 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.8, True,  True, 68, -0.58 * pi],
           # 11
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.9, True,  True, 59, 0.93 * pi],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.6, True,  True, 59, -0.93 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, True,  True, 55, 0.82 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, True,  True, 55, -0.82 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.0, True,  True, 80, 0.93 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, True,  True, 80, -0.93 * pi],
           [18, 2, BLUE,   0, 0, True,  0.022, 14, 0.3, True,  True, 43, pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.3, True,  True, 38, 0.22 * pi],
           [6,  1, BLUE,   0, 0, True,  0.009, 5,  0.7, True,  True, 38, -0.22 * pi],
           # 20
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.2, False, True, 39, 0.22 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.8, False, True, 39, -0.22 * pi],
           [8, 1,  BLUE,   0, 0, True,  0.01,  6,  0.2, False, True, 34, 0.36 * pi],
           [8, 1,  BLUE,   0, 0, True,  0.01,  6,  0.8, False, True, 34, -0.36 * pi],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.9, False, True, 48, 0.77 * pi],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.6, False, True, 48, -0.77 * pi],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.2, False, True, 54, 0.36 * pi],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.4, False, True, 54, -0.36 * pi],
           [8, 1,  BLUE,   0, 0, True,  0.01,  6,  0.3, False, True, 62, 0.46 * pi],
           [8, 1,  BLUE,   0, 0, True,  0.01,  6,  0.6, False, True, 62, -0.46 * pi],
           # 30
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.9, False, True, 44, 0.72 * pi],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.6, False, True, 44, -0.72 * pi],
           [18, 2, BLUE,   0, 0, True,  0.025, 15, 0.2, False, True, 54, 0.38 * pi],
           [18, 2, BLUE,   0, 0, True,  0.025, 15, 0.4, False, True, 54, -0.38 * pi],
           [8, 1,  BLUE,   0, 0, True,  0.01,  6,  0.3, False, True, 71, 0.445 * pi],
           [8, 1,  BLUE,   0, 0, True,  0.01,  6,  0.6, False, True, 71, -0.445 * pi],
           [8, 1,  BLUE,   0, 0, True,  0.01,  6,  0.8, False, True, 67, 0.74 * pi],
           [8, 1,  BLUE,   0, 0, True,  0.01,  6,  0.1, False, True, 67, -0.74 * pi],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.3, False, True, 44, pi],
           # 39
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.2, False, True, 39, 0.36 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.8, False, True, 39, -0.36 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.2, False, True, 35, 0.22 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.8, False, True, 35, -0.22 * pi],
           [18, 2, BLUE,   0, 0, True,  0.025, 15, 0.2, False, True, 58, 0.25 * pi],
           [18, 2, BLUE,   0, 0, True,  0.025, 15, 0.4, False, True, 58, -0.25 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.5, False, True, 80, 0.22 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.0, False, True, 80, -0.22 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.5, False, True, 75, 0.17 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.0, False, True, 75, -0.17 * pi],
           [17, 1, BLUE,   0, 0, True,  0.012, 7,  0.3, False, True, 44, pi],
           # 50
           [9,  1, BLUE,   0, 0, True,  0.009, 5,  0.7, False, True, 37, pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.2, False, True, 42, 0.67 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.8, False, True, 42, -0.67 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.2, False, True, 38, 0.8 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.8, False, True, 38, -0.8 * pi],
           [18, 2, BLUE,   0, 0, True,  0.025, 15, 0.2, False, True, 61, 0.77 * pi],
           [18, 2, BLUE,   0, 0, True,  0.025, 15, 0.4, False, True, 61, -0.77 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.5, False, True, 77, 0.85 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.0, False, True, 77, -0.85 * pi],
           [13, 1, BLUE,   0, 0, True,  0.01,  6,  0.7, False, True, 39, pi],
           # 60
           [19, 1, BLUE,   0, 0, True,  0.015, 9,  0.3, False, True, 45, pi],
           [21, 1, BLUE,   0, 0, True,  0.016, 10, 0.3, False, True, 45, pi],
           [23, 1, BLUE,   0, 0, True,  0.018, 11, 0.3, False, True, 46, pi],
           [25, 1, BLUE,   0, 0, True,  0.02,  12, 0.3, False, True, 47, pi],
           [27, 1, BLUE,   0, 0, True,  0.02,  12, 0.3, False, True, 48, pi],
           [29, 1, BLUE,   0, 0, True,  0.022, 13, 0.3, False, True, 51, pi],
           [31, 1, BLUE,   0, 0, True,  0.022, 13, 0.3, False, True, 53, pi],
           [33, 1, BLUE,   0, 0, True,  0.024, 14, 0.3, False, True, 55, pi],
           [35, 1, BLUE,   0, 0, True,  0.024, 14, 0.3, False, True, 57, pi],
           [37, 1, BLUE,   0, 0, True,  0.024, 14, 0.3, False, True, 59, pi],
           [39, 1, BLUE,   0, 0, True,  0.025, 15, 0.3, False, True, 60, pi],
           [41, 1, BLUE,   0, 0, True,  0.025, 15, 0.3, False, True, 62, pi],
           # 72
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.6, False, True, 91, pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.2, False, True, 88, 0.93 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.9, False, True, 88, -0.93 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.2, False, True, 84, 0.91 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.9, False, True, 84, -0.91 * pi],
           # 77
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.2, False, True, 23, 0],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.6, False, True, 23,  0.00],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.2, False, True, 24, 0.69 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.7, False, True, 24, -0.69 * pi],
           [16, 2, BLUE,   0, 0, True,  0.022, 13, 0.6, False, True, 3,  0.00],
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.7, False, True, 27, 0.27 * pi],
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.3, False, True, 27, -0.27 * pi],
           [18, 2, BLUE,   0, 0, True,  0.025, 15, 0.1, False, True, 49, 0.68 * pi],
           [18, 2, BLUE,   0, 0, True,  0.025, 15, 0.4, False, True, 49, -0.68 * pi],
           [18, 2, BLUE,   0, 0, True,  0.025, 15, 0.6, False, True, 51, 0.18 * pi],
           [18, 2, BLUE,   0, 0, True,  0.025, 15, 0.9, False, True, 51, -0.18 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, False, True, 60, 0.79 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, False, True, 60, -0.79 * pi],
           [32, 1, BLUE,   0, 0, True,  0.024, 14, 0,   False, True, 40,  pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.4, False, True, 70, 0.1 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.9, False, True, 70, -0.1 * pi],

           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.1, False, True, 78, pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.3, False, True, 75, 0.9 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.8, False, True, 75, -0.9 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.3, False, True, 72, 0.68 * pi],
           [8,  1, BLUE,   0, 0, True,  0.01,  6,  0.8, False, True, 72, -0.68 * pi],
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.1, False, True, 74, 0.68 * pi],
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.5, False, True, 74, -0.68 * pi],
           # 100
           [16, 2, ORANGE, 0, 0, True,  0.024, 15, 0,   True,  True, 0,  0.00],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.5, True,  True, 21, pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.7, True,  True, 20, 0.00],
           [8,  1, ORANGE, 0, 0, True,  0.01,  6,  0.5, True,  True, 31, 0.00],
           [8,  1, ORANGE, 0, 0, True,  0.01,  6,  0.9, True,  True, 41, 0.00],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.1, True,  True, 21, 0.72 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.3, True,  True, 21, -0.72 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.008, 5,  0.1, True,  True, 33, 0.71 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.008, 5,  0.7, True,  True, 33, -0.71 * pi],
           # 109
           [16, 2, ORANGE, 0, 0, True,  0.024, 15, 0,   False, True, 36, pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.5, False, True, 57, pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.7, False, True, 17, pi],
           [8,  1, ORANGE, 0, 0, True,  0.01,  6,  0.5, False, True, 6,  pi],
           [8,  1, ORANGE, 0, 0, True,  0.01,  6,  0.9, False, True, 5,  0.00],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.1, False, True, 47, 0.86 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.3, False, True, 47, -0.86 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.008, 5,  0.1, False, True, 60, 0.84 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.008, 5,  0.7, False, True, 60, -0.84 * pi],

           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_30 = ((400, (0, 78), (94, 98), (100, 109)),
                    (388, (0, 78), (93, 98), (100, 109)),
                    (378, (0, 78), (93, 96), (98, 109)),
                    (368, (0, 78), (96, 109)),
                    (358, (0, 78), (93, 94), (96, 109)),
                    (348, (0, 78), (94, 109)),
                    (338, (0, 78), (93, 109)),
                    (328, (0, 77), (78, 79), (93, 109)),
                    (318, (0, 79), (93, 109)),
                    (308, (1, 32), (32, 39), (45, 47), (49, 51), (59, 67), (68, 72), (73, 75), (77, 100), (109, 118)),
                    (298, (1, 32), (32, 39), (45, 47), (49, 51), (59, 67), (68, 73), (75, 100), (109, 118)),
                    (288, (1, 32), (32, 39), (45, 47), (49, 51), (59, 67), (68, 72), (73, 100), (109, 118)),
                    (278, (1, 32), (32, 39), (45, 47), (49, 51), (59, 67), (68, 100), (109, 118)),
                    (268, (1, 32), (32, 39), (45, 47), (49, 51), (59, 66), (67, 100), (109, 118)),
                    (258, (1, 32), (32, 39), (45, 47), (49, 51), (59, 65), (66, 100), (109, 118)),
                    (248, (1, 32), (32, 39), (45, 47), (49, 51), (59, 60), (61, 100), (109, 118)),
                    (238, (1, 32), (32, 39), (45, 47), (50, 51), (59, 100), (109, 118)),
                    (228, (1, 32), (32, 39), (45, 47), (49, 51), (60, 100), (109, 118)),
                    (218, (1, 32), (32, 39), (45, 47), (49, 50), (59, 100), (109, 118)),
                    (208, (1, 30), (32, 39), (45, 47), (49, 71), (72, 100), (109, 118)),
                    (198, (1, 30), (32, 39), (45, 47), (49, 70), (71, 100), (109, 118)),
                    (188, (1, 30), (32, 39), (45, 47), (49, 69), (70, 100), (109, 118)),
                    (178, (1, 30), (32, 39), (45, 47), (49, 68), (69, 100), (109, 118)),
                    (168, (1, 30), (32, 39), (45, 47), (49, 67), (68, 100), (109, 118)),
                    (158, (1, 30), (32, 39), (45, 47), (49, 66), (67, 100), (109, 118)),
                    (148, (1, 30), (32, 39), (45, 47), (49, 65), (66, 100), (109, 118)),
                    (138, (1, 30), (32, 39), (45, 47), (49, 64), (65, 100), (109, 118)),
                    (118, (1, 30), (32, 39), (45, 47), (49, 63), (64, 100), (109, 118)),
                    (108, (1, 30), (32, 39), (45, 47), (49, 62), (63, 100), (109, 118)),
                    (98,  (1, 30), (32, 39), (45, 47), (49, 61), (62, 100), (109, 118)),
                    (88,  (1, 30), (32, 39), (45, 47), (49, 60), (61, 100), (109, 118)),
                    (78,  (1, 30), (32, 39), (45, 47), (50, 100), (109, 118)),
                    (68,  (1, 30), (32, 38), (45, 47), (49, 100), (109, 118)),
                    (58,  (1, 30), (32, 38), (47, 100), (109, 118)),
                    (48,  (1, 20), (24, 30), (36, 38), (39, 100), (109, 118)),
                    (38,  (1, 20), (24, 30), (38, 100), (109, 118)),
                    (28,  (1, 20), (24, 30), (36, 100), (109, 118)),
                    (18,  (1, 20), (30, 100), (109, 118)),
                    (8,  (20, 100), (109, 118)))

PARAMS_30 = [MAX_HEALTH_30, HEALTH_STATES_30, RADIUS_30, BODY_30, MAX_VEL_30,
             ACC_30, GUN_TYPE_30, BG_RADIUS_30, SUPERPOWER_30]
###############################################################################
MAX_VEL_31 = 0.65
ACC_31 = 0.0025
GUN_TYPE_31 = 'Gun31'
SUPERPOWER_31 = 'TwoHomingMissiles'
MAX_HEALTH_31 = 400
RADIUS_31 = 90
BG_RADIUS_31 = 110
BODY_31 = [[30, 4, BLUE,   0, 0, True,  0.046, 28, 0,   True,  True, 0,  0.00],
           [20, 3, BLUE,   0, 0, True,  0.03,  18, 0,   True,  True, 64, 0.54 * pi],
           [20, 3, BLUE,   0, 0, True,  0.03,  18, 0.3, True,  True, 64, -0.54 * pi],
           [20, 3, BLUE,   0, 0, True,  0.031, 18, 0.6, True,  True, 63, 0.72 * pi],
           [20, 3, BLUE,   0, 0, True,  0.031, 18, 0.8, True,  True, 63, -0.72 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, True,  True, 38, 0.7 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, True,  True, 38, -0.7 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, True,  True, 40, 0.83 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, True,  True, 40, -0.83 * pi],
           # 9
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.2, True,  True, 46, 0.43 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.6, True,  True, 46, -0.43 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, True,  True, 82, 0.46 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.8, True,  True, 82, -0.46 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.0, False, True, 37, pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.0, False, True, 39, pi],
           [12, 1, BLUE,   0, 0, True,  0.017, 10, 0.0, False, True, 41, pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.0, False, True, 43, pi],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.0, False, True, 44, pi],
           [18, 2, BLUE,   0, 0, True,  0.027, 16, 0.0, False, True, 46, pi],
           [19, 2, BLUE,   0, 0, True,  0.03,  18, 0.0, False, True, 48, pi],
           # 20
           [22, 3, BLUE,   0, 0, True,  0.033, 20, 0.0, False, True, 50, pi],
           [24, 3, BLUE,   0, 0, True,  0.035, 21, 0.0, False, True, 51, pi],
           [26, 3, BLUE,   0, 0, True,  0.036, 22, 0.0, False, True, 52, pi],
           [28, 4, BLUE,   0, 0, True,  0.04,  24, 0.0, False, True, 53, pi],

           [18, 2, ORANGE, 0, 0, True,  0.02,  12, 0,   True,  True, 5,  0.00],
           [10, 1, ORANGE, 0, 0, True,  0.014, 8,  0.4, True,  True, 19, pi],
           [10, 1, ORANGE, 0, 0, True,  0.014, 8,  0,   True,  True, 22, 0.6 * pi],
           [10, 1, ORANGE, 0, 0, True,  0.014, 8,  0.4, True,  True, 22, -0.6 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0,   True,  True, 27, 0.00],
           [12, 1, ORANGE, 0, 0, True,  0.017, 10, 0,   True,  True, 65, 0.43 * pi],
           [12, 1, ORANGE, 0, 0, True,  0.017, 10, 0.4, True,  True, 65, -0.43 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.9, True,  True, 56, 0.34 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.4, True,  True, 56, -0.34 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.6, True,  True, 82, 0.39 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.1, True,  True, 82, -0.39 * pi],

           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_31 = ((98, (13, 23)),
                    (90, (13, 22), (23, 24)),
                    (82, (13, 21), (22, 24)),
                    (74, (13, 20), (21, 24)),
                    (66, (13, 19), (20, 24)),
                    (58, (13, 18), (19, 24)),
                    (50, (13, 17), (18, 24)),
                    (42, (13, 16), (17, 24)),
                    (34, (13, 15), (16, 24)),
                    (26, (13, 14), (15, 24)),
                    (18, (14, 24)),
                    (10, (13, 24)))

PARAMS_31 = [MAX_HEALTH_31, HEALTH_STATES_31, RADIUS_31, BODY_31, MAX_VEL_31,
             ACC_31, GUN_TYPE_31, BG_RADIUS_31, SUPERPOWER_31]
###############################################################################
MAX_VEL_32 = 0.6
ACC_32 = 0.00225
GUN_TYPE_32 = 'Gun32'
SUPERPOWER_32 = 'Paralysing_explosion'
MAX_HEALTH_32 = 400
RADIUS_32 = 70
BG_RADIUS_32 = 125
BODY_32 = [[16, 2, BLUE,   0, 0, True,  0.024, 14, 0.1, True,  True, 71,  0.00],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.3, True,  True, 52,  0.5 * pi],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.7, True,  True, 52,  -0.48 * pi],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.9, True,  True, 30,  pi],
           [20, 3, BLUE,   0, 0, True,  0.026, 16, 0.8, True,  True, 96, 0.00],
           [40, 2, BLUE,   0, 0, True,  0.03,  18, 0,   True,  True, 20,  0.00],

           [18, 3, ORANGE, 0, 0, True,  0.026, 15, 0.0, True,  True, 20,  0.00],
           [9,  1, ORANGE, 0, 0, True,  0.014, 8,  0.7, True,  True, 2,   pi],
           [9,  1, ORANGE, 0, 0, True,  0.014, 8,  0.1, True,  True, 24,  0.37 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.014, 8,  0.4, True,  True, 24,  -0.37 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.9, True,  True, 38,  0.00],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.6, True,  True, 47,  0.00],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.5, True,  True, 37,  0.1 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.2, True,  True, 47,  0.095 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.7, True,  True, 37,  -0.1 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.3, True,  True, 47,  -0.095 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.5, True,  True, 36,  0.19 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.2, True,  True, 44,  0.185 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.8, True,  True, 36,  -0.19 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.4, True,  True, 44,  -0.185 * pi],
           [18, 3, ORANGE, 0, 0, True,  0.026, 15, 0.5, True,  True, 46,  pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.4, True,  True, 46,  pi, False, 0, True, 50],

           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25,  0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23,  0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26,  -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27,  pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17,  -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29,  0.25 * pi]]

HEALTH_STATES_32 = ((0, ),)

PARAMS_32 = [MAX_HEALTH_32, HEALTH_STATES_32, RADIUS_32, BODY_32, MAX_VEL_32,
             ACC_32, GUN_TYPE_32, BG_RADIUS_32, SUPERPOWER_32]
###############################################################################
MAX_VEL_33 = 0.55
ACC_33 = 0.002
GUN_TYPE_33 = 'Gun33'
SUPERPOWER_33 = 'Powerful_explosion'
MAX_HEALTH_33 = 400
RADIUS_33 = 70
BG_RADIUS_33 = 90
BODY_33 = [[16, 2, BLUE,   0, 0, True,  0.024, 14, 0.3, True,  True, 33,  pi],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.7, True,  True, 72,  0.9 * pi],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.1, True,  True, 72,  -0.9 * pi],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.5, True,  True, 76,  0.2 * pi],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.9, True,  True, 76,  -0.2 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 9,  0.8, True,  True, 35,  0.61 * pi],
           [10, 1, BLUE,   0, 0, True,  0.015, 9,  0.5, True,  True, 35,  -0.61 * pi],
           [40, 2, BLUE,   0, 0, True,  0.027, 16, 0,   True,  True, 49,  0.00],
           [25, 1, BLUE,   0, 0, True,  0.017, 10, 0.4, True,  True, 6,   pi],
           [9,  1, BLUE,   0, 0, True,  0.014, 8,  0.2, True,  True, 98,  0],

           [13, 2, ORANGE, 0, 0, True,  0.02,  12, 0.7, True,  True, 22,  pi],
           [13, 2, ORANGE, 0, 0, True,  0.02,  12, 0.3, True,  True, 76,  pi],
           [13, 2, ORANGE, 0, 0, True,  0.02,  12, 0.5, True,  True, 56,  0.84 * pi],
           [13, 2, ORANGE, 0, 0, True,  0.02,  12, 0.1, True,  True, 56,  -0.84 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.014, 8,  0.4, True,  True, 65,  0.77 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.014, 8,  0.1, True,  True, 65,  -0.77 * pi],
           [18, 3, ORANGE, 0, 0, True,  0.029, 17, 0.0, True,  True, 49,  0.00],
           [9,  1, ORANGE, 0, 0, True,  0.014, 8,  0.7, True,  True, 30,  0.00],
           [9,  1, ORANGE, 0, 0, True,  0.014, 8,  0.3, True,  True, 44,  0.17 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.014, 8,  0.5, True,  True, 44,  -0.17 * pi],

           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.9, True,  True, 65,  0.00],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.6, True,  True, 74,  0.00],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.3, True,  True, 64,  0.055 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.0, True,  True, 73,  0.06 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.7, True,  True, 64,  -0.055 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.2, True,  True, 73,  -0.06 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.1, True,  True, 60,  0.1 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.5, True,  True, 69,  0.11 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.4, True,  True, 60,  -0.1 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.8, True,  True, 69,  -0.11 * pi],
           [18, 3, ORANGE, 0, 0, True,  0.029, 17, 0.4, True,  True, 49,  pi],

           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25,  0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23,  0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26,  -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27,  pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17,  -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29,  0.25 * pi]]

HEALTH_STATES_33 = ((0, ),)

PARAMS_33 = [MAX_HEALTH_33, HEALTH_STATES_33, RADIUS_33, BODY_33, MAX_VEL_33,
             ACC_33, GUN_TYPE_33, BG_RADIUS_33, SUPERPOWER_33]
###############################################################################
MAX_VEL_34 = 0.3
ACC_34 = 0.001
GUN_TYPE_34 = 'Gun34'
SUPERPOWER_34 = 'StickyCannon'
MAX_HEALTH_34 = 400
RADIUS_34 = 110
BG_RADIUS_34 = 120
BODY_34 = [[12, 1, BLUE,   130, 0.79 * pi,  True,  0.016, 10, 0.4, True,  False, 0,  0],
           [12, 1, BLUE,   130, -0.79 * pi, True,  0.016, 10, 0.9, True,  False, 0,  0],
           [12, 1, BLUE,   68,  0.36 * pi,  True,  0.016, 10, 0.2, True,  False, 0,  0],
           [12, 1, BLUE,   68,  -0.36 * pi, True,  0.016, 10, 0.6, True,  False, 0,  0],
           [40, 2, BLUE,   80,  0,          True,  0.027, 16, 0,   True,  False, 0,  0],
           [58, 2, BLUE,   0,   0,          True,  0.041, 24, 0,   True,  False, 0,  0],
           [18, 2, BLUE,   32,  pi,         True,  0.027, 16, 0.6, True,  False, 0,  0],
           [46, 2, BLUE,   80,  0.76 * pi,  True,  0.03,  18, 0,   True,  False, 0,  0],
           [46, 2, BLUE,   80,  -0.76 * pi, True,  0.03,  18, 0.4, True,  False, 0,  0],

           [11, 1, ORANGE, 80,  0.76 * pi,  True,  0.017, 10, 0,   True,  True,  32, 0.2 * pi],
           [11, 1, ORANGE, 80,  0.76 * pi,  True,  0.017, 10, 0.4, True,  True,  32, -0.2 * pi],
           [11, 1, ORANGE, 80,  0.76 * pi,  True,  0.017, 10, 0.7, True,  True,  48, 0.13 * pi],
           [11, 1, ORANGE, 80,  0.76 * pi,  True,  0.017, 10, 0.2, True,  True,  48, -0.13 * pi],
           [28, 4, ORANGE, 80,  0.76 * pi,  True,  0.044, 26, 0,   True,  True,  0,  0.00],
           [12, 1, ORANGE, 80,  0.76 * pi,  True,  0.019, 11, 0,   True,  True,  36, 0.77 * pi],
           [12, 1, ORANGE, 80,  0.76 * pi,  True,  0.019, 11, 0.4, True,  True,  36, -0.77 * pi],

           [11, 1, ORANGE, 80,  -0.76 * pi, True,  0.017, 10, 0.3, True,  True,  32, 0.2 * pi],
           [11, 1, ORANGE, 80,  -0.76 * pi, True,  0.017, 10, 0.7, True,  True,  32, -0.2 * pi],
           [11, 1, ORANGE, 80,  -0.76 * pi, True,  0.017, 10, 0.0, True,  True,  48, 0.13 * pi],
           [11, 1, ORANGE, 80,  -0.76 * pi, True,  0.017, 10, 0.5, True,  True,  48, -0.13 * pi],
           [28, 4, ORANGE, 80,  -0.76 * pi, True,  0.044, 26, 0.3, True,  True,  0,  0.00],
           [12, 1, ORANGE, 80,  -0.76 * pi, True,  0.019, 11, 0.3, True,  True,  36, 0.77 * pi],
           [12, 1, ORANGE, 80,  -0.76 * pi, True,  0.019, 11, 0.7, True,  True,  36, -0.77 * pi],

           [10, 1, ORANGE, 72,  0.00,       True,  0.015, 9,  0.8, True,  True,  29, pi/4],
           [10, 1, ORANGE, 72,  0.00,       True,  0.015, 9,  0.6, True,  True,  29, -pi/4],
           [10, 1, ORANGE, 72,  0.00,       True,  0.015, 9,  0.4, True,  True,  42, pi/6],
           [10, 1, ORANGE, 72,  0.00,       True,  0.015, 9,  0.2, True,  True,  42, -pi/6],
           [9,  1, ORANGE, 72,  0.00,       True,  0.015, 9,  0,   True,  True,  55, pi/8],
           [9,  1, ORANGE, 72,  0.00,       True,  0.015, 9,  0,   True,  True,  55, -pi/8],
           [6,  1, ORANGE, 72,  0.00,       True,  0.01,  6,  0.3, True,  True,  56, -0.19*pi],
           [6,  1, ORANGE, 72,  0.00,       True,  0.01,  6,  0.9, True,  True,  56, 0.19*pi],
           [28, 4, ORANGE, 72,  0.00,       True,  0.044, 26, 0,   True,  True,  0,  0],
           [12, 1, ORANGE, 72,  0.00,       True,  0.017, 10, 0.2, True,  True,  30, -pi],
           [12, 1, ORANGE, 72,  0.00,       True,  0.017, 10, 0.5, True,  True,  30, -2 * pi/3],
           [12, 1, ORANGE, 72,  0.00,       True,  0.017, 10, 0.8, True,  True,  30, 2 * pi/3],

           [17, 1, VIOLET, 25,  0.8 * pi,   False, 0,     0,  0,   False, False, 0,  0],
           [8,  1, VIOLET, 23,  0.55 * pi,  False, 0,     0,  0,   False, False, 0,  0],
           [8,  1, VIOLET, 26,  -0.45 * pi, False, 0,     0,  0,   False, False, 0,  0],
           [8,  1, VIOLET, 27,  pi,         False, 0,     0,  0,   False, False, 0,  0],
           [8,  1, VIOLET, 17, -0.9 * pi,   False, 0,     0,  0,   False, False, 0,  0],
           [10, 1, VIOLET, 29, 0.25 * pi,   False, 0,     0,  0,   False, False, 0,  0]]

HEALTH_STATES_34 = ((0, ),)

PARAMS_34 = [MAX_HEALTH_34, HEALTH_STATES_34, RADIUS_34, BODY_34, MAX_VEL_34,
             ACC_34, GUN_TYPE_34, BG_RADIUS_34, SUPERPOWER_34]
###############################################################################
MAX_VEL_35 = 0.2
ACC_35 = 0.0005
GUN_TYPE_35 = 'Gun35'
SUPERPOWER_35 = 'FourHomingMissiles'
MAX_HEALTH_35 = 400
RADIUS_35 = 110
BG_RADIUS_35 = 120
BODY_35 = [[11, 1, BLUE,   53,  0.33 * pi,  True,  0.017, 10, 0.1, True,  False, 0,  0],
           [11, 1, BLUE,   53,  -0.33 * pi, True,  0.015, 9,  0.8, True,  False, 0,  0],
           [9,  1, BLUE,   53,  0.22 * pi,  True,  0.014, 8,  0.2, True,  False, 0,  0],
           [9,  1, BLUE,   53,  -0.22 * pi, True,  0.014, 8,  0.9, True,  False, 0,  0],
           [15, 2, BLUE,   56,  0.56 * pi,  True,  0.022, 13, 0.2, True,  False, 0,  0],
           [15, 2, BLUE,   56,  -0.56 * pi, True,  0.022, 13, 0.8, True,  False, 0,  0],
           [11, 1, BLUE,   51,  pi,         True,  0.015, 9,  0.3, True,  False, 0,  0],
           [23, 3, BLUE,   81,  pi,         True,  0.035, 21, 0.4, True,  False, 0,  0],
           [17, 2, BLUE,   92,  0.8 * pi,   True,  0.025, 15, 0.0, True,  False, 0,  0],
           [17, 2, BLUE,   92,  -0.8 * pi,  True,  0.025, 15, 0.5, True,  False, 0,  0],
           [15, 2, BLUE,   94,  0.89 * pi,  True,  0.022, 13, 0.0, True,  False, 0,  0],
           [15, 2, BLUE,   94,  -0.89 * pi, True,  0.022, 13, 0.5, True,  False, 0,  0],
           [46, 2, BLUE,   0,   0,          True,  0.03,  18, 0,   True,  False, 0,  0],
           [28, 2, BLUE,   87,  0.25 * pi,  True,  0.024, 14, 0,   True,  False, 0,  0],
           [28, 2, BLUE,   87,  -0.25 * pi, True,  0.024, 14, 0.4, True,  False, 0,  0],

           [11, 1, ORANGE, 0,   0,          True,  0.017, 10, 0,   True,  True,  32, 0.2 * pi],
           [11, 1, ORANGE, 0,   0,          True,  0.017, 10, 0.4, True,  True,  32, -0.2 * pi],
           [11, 1, ORANGE, 0,   0,          True,  0.017, 10, 0.7, True,  True,  48, 0.13 * pi],
           [11, 1, ORANGE, 0,   0,          True,  0.017, 10, 0.2, True,  True,  48, -0.13 * pi],
           [29, 4, ORANGE, 0,   0,          True,  0.048, 28, 0,   True,  True,  0,  0.00],
           [12, 1, ORANGE, 0,   0,          True,  0.019, 11, 0,   True,  True,  36, 0.77 * pi],
           [12, 1, ORANGE, 0,   0,          True,  0.019, 11, 0.4, True,  True,  36, -0.77 * pi],
           [14, 2, ORANGE, 87,  0.25 * pi,  True,  0.02,  12, 0,   True,  False, 0,  0],
           [14, 2, ORANGE, 87,  -0.25 * pi, True,  0.02,  12, 0.4, True,  False, 0,  0],
           [7, 1,  ORANGE, 100, 0.21 * pi,  True,  0.01,  6,  0.4, True,  False, 0,  0],
           [7, 1,  ORANGE, 100, -0.21 * pi, True,  0.01,  6,  0.7, True,  False, 0,  0],

           [12, 1, ORANGE, 71,  0.55 * pi,  True,  0.019, 11, 0.7, True,  False, 0,  0],
           [12, 1, ORANGE, 71,  -0.55 * pi, True,  0.019, 11, 0.2, True,  False, 0,  0],
           [8,  1, ORANGE, 77,  0.63 * pi,  True,  0.012, 7,  0.6, True,  False, 0,  0],
           [8,  1, ORANGE, 77,  -0.63 * pi, True,  0.012, 7,  0.1, True,  False, 0,  0],
           [8,  1, ORANGE, 91,  0.54 * pi,  True,  0.012, 7,  0.3, True,  False, 0,  0],
           [8,  1, ORANGE, 91,  -0.54 * pi, True,  0.012, 7,  0.9, True,  False, 0,  0],
           [12, 1, ORANGE, 92,  0.8 * pi,   True,  0.019, 11, 0.4, True,  False, 0,  0],
           [12, 1, ORANGE, 92,  -0.8 * pi,  True,  0.019, 11, 0.9, True,  False, 0,  0],
           [8,  1, ORANGE, 105, 0.75 * pi,  True,  0.012, 7,  0.2, True,  False, 0,  0],
           [8,  1, ORANGE, 105, -0.75 * pi, True,  0.012, 7,  0.8, True,  False, 0,  0],
           [8,  1, ORANGE, 106, 0.83 * pi,  True,  0.012, 7,  0.5, True,  False, 0,  0],
           [8,  1, ORANGE, 106, -0.83 * pi, True,  0.012, 7,  0.4, True,  False, 0,  0],

           [17, 1, VIOLET, 0,   0,          False, 0,     0,  0,   False, True,  25, 0.8 * pi],
           [8,  1, VIOLET, 0,   0,          False, 0,     0,  0,   False, True,  23, 0.55 * pi],
           [8,  1, VIOLET, 0,   0,          False, 0,     0,  0,   False, True,  26, -0.45 * pi],
           [8,  1, VIOLET, 0,   0,          False, 0,     0,  0,   False, True,  27, pi],
           [8,  1, VIOLET, 0,   0,          False, 0,     0,  0,   False, True,  17, -0.9 * pi],
           [10, 1, VIOLET, 0,   0,          False, 0,     0,  0,   False, True,  29, 0.25 * pi]]

HEALTH_STATES_35 = ((0, ),)

PARAMS_35 = [MAX_HEALTH_35, HEALTH_STATES_35, RADIUS_35, BODY_35, MAX_VEL_35,
             ACC_35, GUN_TYPE_35, BG_RADIUS_35, SUPERPOWER_35]
###############################################################################
MAX_VEL_40 = 0.7
ACC_40 = 0.003
GUN_TYPE_40 = 'Gun40'
SUPERPOWER_40 = 'Fast_teleportation'
MAX_HEALTH_40 = 500
RADIUS_40 = 60
BG_RADIUS_40 = 100
BODY_40 = [[18, 2, BLUE,   0, 0, True,  0.025, 15, 0.1, True,  True, 15, 0],
           [32, 1, BLUE,   0, 0, True,  0.024, 14, 0,   True,  True, 31, pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, True,  True, 62, 0.9 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, True,  True, 62, -0.9 * pi],
           [12, 1, BLUE,   0, 0, True,  0.019, 11, 0.7, True,  True, 40, 0],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.6, True,  True, 46, 0.65 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.2, True,  True, 46, -0.65 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, True,  True, 30, 0.2 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.8, True,  True, 30, -0.2 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, True,  True, 66, pi],
           # 10
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.1, False, True, 67, pi],
           [12, 1, BLUE,   0, 0, True,  0.017, 10, 0.1, False, True, 68, pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.1, False, True, 69, pi],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.1, False, True, 70, pi],
           [18, 2, BLUE,   0, 0, True,  0.027, 16, 0.1, False, True, 71, pi],
           [20, 3, BLUE,   0, 0, True,  0.03,  18, 0.1, False, True, 73, pi],
           [13, 1, BLUE,   0, 0, True,  0.019, 11, 0.7, False, True, 41, 0],
           [14, 1, BLUE,   0, 0, True,  0.02,  12, 0.7, False, True, 41, 0],
           [15, 2, BLUE,   0, 0, True,  0.022, 13, 0.7, False, True, 42, 0],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.7, False, True, 42, 0],
           [18, 2, BLUE,   0, 0, True,  0.027, 16, 0.7, False, True, 43, 0],
           # 21
           [15, 2, BLUE,   0, 0, True,  0.022, 13, 0.6, False, True, 47, 0.65 * pi],
           [15, 2, BLUE,   0, 0, True,  0.022, 13, 0.2, False, True, 47, -0.65 * pi],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.6, False, True, 48, 0.65 * pi],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.2, False, True, 48, -0.65 * pi],
           [17, 2, BLUE,   0, 0, True,  0.025, 15, 0.6, False, True, 49, 0.65 * pi],
           [17, 2, BLUE,   0, 0, True,  0.025, 15, 0.2, False, True, 49, -0.65 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, False, True, 56, 0.78 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.9, False, True, 56, -0.78 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, False, True, 47, 0.7 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, False, True, 47, -0.7 * pi],
           # 31
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.3, False, True, 48, 0.69 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.7, False, True, 48, -0.69 * pi],
           [12, 1, BLUE,   0, 0, True,  0.016, 10, 0.3, False, True, 48, 0.67 * pi],
           [12, 1, BLUE,   0, 0, True,  0.016, 10, 0.7, False, True, 46, -0.67 * pi],
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.3, False, True, 54, 0.77 * pi],
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.7, False, True, 54, -0.77 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, False, True, 97, pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, False, True, 87, 0.93 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, False, True, 87, -0.93 * pi],
           # 40
           [18, 2, BLUE,   0, 0, True,  0.027, 16, 0.7, False, True, 70, 0.7 * pi],
           [18, 2, BLUE,   0, 0, True,  0.027, 16, 0.7, False, True, 70, -0.7 * pi],
           [22, 3, BLUE,   0, 0, True,  0.032, 19, 0.1, False, True, 77, pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, False, True, 102, pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.8, False, True, 64, 0],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, False, True, 95, 0.93 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, False, True, 95, -0.93 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, False, True, 86, 0.89 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, False, True, 86, -0.89 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, False, True, 78, 0.89 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, False, True, 78, -0.89 * pi],
           # 51
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.1, False, True, 78, 0.89 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.7, False, True, 78, -0.89 * pi],
           [12, 1, BLUE,   0, 0, True,  0.016, 10, 0.1, False, True, 79, 0.89 * pi],
           [12, 1, BLUE,   0, 0, True,  0.016, 10, 0.7, False, True, 79, -0.89 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, False, True, 94, 0.72 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.9, False, True, 94, -0.72 * pi],

           [16, 2, ORANGE, 0, 0, True,  0.024, 15, 0,   True,  True, 27, pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.5, True,  True, 48, pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.1, True,  True, 40, 0.84 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.3, True,  True, 40, -0.84 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.01,  6,  0.1, True,  True, 9, 0.75 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.01,  6,  0.7, True,  True, 9, -0.75 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.01,  6,  0.3, True,  True, 9, 0.25 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.01,  6,  0.5, True,  True, 9, -0.25 * pi],

           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_40 = ((500, (4, 5),  (9, 20),  (21, 35), (37, 40), (45, 55)),
                    (488, (4, 5),  (9, 20),  (21, 35), (37, 40), (45, 53), (55, 57)),
                    (478, (4, 5),  (9, 20),  (21, 35), (37, 40), (45, 51), (53, 57)),
                    (468, (4, 5),  (9, 20),  (21, 35), (37, 40), (45, 49), (51, 57)),
                    (458, (4, 5),  (9, 20),  (21, 35), (37, 40), (43, 44), (45, 49), (51, 57)),
                    (448, (4, 5),  (9, 20),  (21, 35), (37, 40), (43, 44), (45, 47), (49, 57)),
                    (438, (4, 5),  (9, 20),  (21, 35), (37, 40), (43, 44), (47, 57)),
                    (428, (4, 5),  (9, 20),  (21, 35), (37, 40), (45, 57)),
                    (418, (4, 5),  (9, 20),  (21, 35), (37, 40), (44, 57)),
                    (408, (4, 5),  (9, 20),  (21, 35), (37, 40), (43, 57)),
                    (398, (4, 5),  (9, 15),  (16, 20), (21, 35), (37, 40), (42, 57)),
                    (388, (4, 5),  (9, 14),  (15, 20), (21, 35), (37, 40), (42, 57)),
                    (368, (4, 5),  (9, 13),  (14, 20), (21, 35), (37, 40), (42, 57)),
                    (348, (4, 5),  (9, 12),  (13, 20), (21, 35), (37, 40), (42, 57)),
                    (328, (4, 5),  (9, 11),  (12, 20), (21, 35), (37, 40), (42, 57)),
                    (308, (4, 5),  (9, 10),  (11, 20), (21, 35), (37, 40), (42, 57)),
                    (288, (4, 5),  (10, 20), (21, 35), (37, 40), (42, 57)),
                    (278, (4, 5),  (9, 20),  (21, 35), (37, 40), (42, 57)),
                    (268, (2, 5),  (10, 20), (21, 35), (37, 40), (42, 57)),
                    (258, (2, 5),  (9, 20),  (21, 35), (37, 40), (42, 57)),
                    (248, (4, 5),  (9, 15),  (16, 20), (21, 35), (40, 57)),
                    (238, (4, 5),  (9, 15),  (16, 20), (21, 35), (37, 38), (40, 57)),
                    (228, (4, 5),  (9, 15),  (16, 20), (21, 35), (38, 57)),
                    (218, (4, 5),  (9, 15),  (16, 20), (21, 35), (37, 57)),
                    (203, (4, 7),  (9, 15),  (16, 20), (21, 27), (29, 33), (35, 57)),
                    (188, (4, 7),  (9, 15),  (16, 20), (21, 27), (29, 31), (33, 57)),
                    (173, (4, 7),  (9, 15),  (16, 20), (21, 27), (31, 57)),
                    (158, (4, 7),  (9, 15),  (16, 20), (21, 25), (27, 57)),
                    (146, (4, 7),  (9, 15),  (16, 20), (21, 23), (25, 57)),
                    (133, (4, 7),  (9, 15),  (16, 20), (23, 57)),
                    (120, (4, 5),  (9, 15),  (16, 20), (21, 57)),
                    (110, (4, 5),  (9, 15),  (16, 19), (20, 57)),
                    (100, (4, 5),  (9, 15),  (16, 18), (19, 57)),
                    (90,  (4, 5),  (9, 15),  (16, 17), (18, 57)),
                    (80,  (4, 5),  (9, 15),  (17, 57)),
                    (70,  (9, 15), (16, 57)),
                    (60,  (9, 14), (15, 57)),
                    (50,  (9, 13), (14, 57)),
                    (40,  (9, 12), (13, 57)),
                    (30,  (9, 11), (12, 57)),
                    (20,  (9, 10), (11, 57)),
                    (10,  (10, 57)))

PARAMS_40 = [MAX_HEALTH_40, HEALTH_STATES_40, RADIUS_40, BODY_40, MAX_VEL_40,
             ACC_40, GUN_TYPE_40, BG_RADIUS_40, SUPERPOWER_40]
###############################################################################
MAX_VEL_41 = 0.675
ACC_41 = 0.0025
GUN_TYPE_41 = 'Gun41'
SUPERPOWER_41 = 'ExplosionStar'
MAX_HEALTH_41 = 500
RADIUS_41 = 60
BG_RADIUS_41 = 100
BODY_41 = [[16, 2, BLUE,   0, 0, True,  0.024, 14, 0.1, True,  True, 20, 0],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.3, True,  True, 52, 0.81 * pi],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.5, True,  True, 52, -0.81 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.2, True,  True, 28, 0.49 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.6, True,  True, 28, -0.49 * pi],
           [33, 1, BLUE,   0, 0, True,  0.024, 14, 0,   True,  True, 25, pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, True,  True, 42, 0.12 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.8, True,  True, 42, -0.12 * pi],

           [18, 2, ORANGE, 0, 0, True,  0.024, 15, 0.4, True,  True, 22, pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.5, True,  True, 44, pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.1, True,  True, 40, 0.84 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.3, True,  True, 40, -0.84 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.01,  6,  0.1, True,  True, 6, 0.5 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.01,  6,  0.7, True,  True, 6, -0.5 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.2, True,  True, 77, 0.06 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.5, True,  True, 77, -0.06 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.7, True,  True, 66, 0.07 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.9, True,  True, 66, -0.07 * pi],
           [16, 2, ORANGE, 0, 0, True,  0.024, 14, 0.7, True,  True, 51, 0],

           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_41 = ((0, ),)

PARAMS_41 = [MAX_HEALTH_41, HEALTH_STATES_41, RADIUS_41, BODY_41, MAX_VEL_41,
             ACC_41, GUN_TYPE_41, BG_RADIUS_41, SUPERPOWER_41]
###############################################################################
MAX_VEL_42 = 0.65
ACC_42 = 0.0025
GUN_TYPE_42 = 'Gun42'
SUPERPOWER_42 = 'ThreeHomingMissiles'
MAX_HEALTH_42 = 500
RADIUS_42 = 100
BG_RADIUS_42 = 110
BODY_42 = [[19, 2, BLUE,   0, 0, True,  0.027, 16, 0.7, True,  True, 56, 0.6 * pi],
           [19, 2, BLUE,   0, 0, True,  0.027, 16, 0.1, True,  True, 56, -0.6 * pi],
           [19, 2, BLUE,   0, 0, True,  0.027, 16, 0.4, True,  True, 52, pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.7, True,  True, 50, 0],
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.3, True,  True, 48, 0.25 * pi],
           [11, 1, BLUE,   0, 0, True,  0.015, 9,  0.7, True,  True, 48, -0.25 * pi],
           [40, 1, BLUE,   0, 0, True,  0.028, 17, 0,   True,  True, 0,  0],

           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.3, True,  True, 17, 0.34 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.7, True,  True, 17, -0.34 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.9, True,  True, 28, 0.18 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.6, True,  True, 28, -0.18 * pi],
           [23, 3, ORANGE, 0, 0, True,  0.032, 19, 0.1, True,  True, 12, pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.5, True,  True, 39, 0.84 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.1, True,  True, 39, -0.84 * pi],
           [11, 1, ORANGE, 0, 0, True,  0.015, 9,  0.1, True,  True, 56, 0.6 * pi],
           [11, 1, ORANGE, 0, 0, True,  0.015, 9,  0.9, True,  True, 56, -0.6 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.3, True,  True, 54, 0.52 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.6, True,  True, 54, -0.52 * pi],

           [11, 1, ORANGE, 0, 0, True,  0.017, 10, 0.1, True,  True, 63, 0],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.3, True,  True, 76, 0.05 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.9, True,  True, 76, -0.05 * pi],
           [11, 1, ORANGE, 0, 0, True,  0.015, 9,  0.4, True,  True, 66, 0.88 * pi],
           [11, 1, ORANGE, 0, 0, True,  0.015, 9,  0.7, True,  True, 66, -0.88 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.1, True,  True, 82, 0.92 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.7, True,  True, 82, -0.92 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.2, True,  True, 78, 0.82 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.5, True,  True, 78, -0.82 * pi],

           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_42 = ((0, ),)

PARAMS_42 = [MAX_HEALTH_42, HEALTH_STATES_42, RADIUS_42, BODY_42, MAX_VEL_42,
             ACC_42, GUN_TYPE_42, BG_RADIUS_42, SUPERPOWER_42]
###############################################################################
MAX_VEL_43 = 0.5
ACC_43 = 0.002
GUN_TYPE_43 = 'Gun43'
SUPERPOWER_43 = 'PowerfulCannon'
MAX_HEALTH_43 = 500
RADIUS_43 = 100
BG_RADIUS_43 = 120
BODY_43 = [[16, 2, BLUE,   0, 0, True,  0.024, 14, 0.6, True,  True, 104, 0.87 * pi],
           [16, 2, BLUE,   0, 0, True,  0.024, 14, 0.2, True,  True, 104, -0.87 * pi],
           [20, 2, BLUE,   0, 0, True,  0.031, 18, 0.5, True,  True, 28, 0],
           [11, 1, BLUE,   0, 0, True,  0.017, 10, 0.8, True,  True, 40, 0.24 * pi],
           [11, 1, BLUE,   0, 0, True,  0.017, 10, 0.2, True,  True, 40, -0.24 * pi],
           [11, 1, BLUE,   0, 0, True,  0.017, 10, 0.5, True,  True, 57, 0.53 * pi],
           [11, 1, BLUE,   0, 0, True,  0.017, 10, 0.0, True,  True, 57, -0.53 * pi],
           [11, 1, BLUE,   0, 0, True,  0.017, 10, 0.4, True,  True, 80, 0.69 * pi],
           [11, 1, BLUE,   0, 0, True,  0.017, 10, 0.7, True,  True, 80, -0.69 * pi],

           [32, 2, BLUE,   0, 0, True,  0.024, 14, 0,   True,  True, 71, 0],
           [9,  1, BLUE,   0, 0, True,  0.014, 8,  0.1, True,  True, 108, 0],
           [9,  1, BLUE,   0, 0, True,  0.014, 8,  0.4, True,  True, 100, -0.08 * pi],
           [9,  1, BLUE,   0, 0, True,  0.014, 8,  0.8, True,  True, 100, 0.08 * pi],
           [58, 2, BLUE,   0, 0, True,  0.04,  24, 0,   True,  True, 42, pi],

           [7,  1, ORANGE, 0, 0, True,  0.012, 7,  0.1, True,  True, 4,  pi],
           [7,  1, ORANGE, 0, 0, True,  0.012, 7,  0.4, True,  True, 15, pi],
           [7,  1, ORANGE, 0, 0, True,  0.012, 7,  0.7, True,  True, 26, pi],
           [7,  1, ORANGE, 0, 0, True,  0.012, 7,  0.3, True,  True, 30,  0.54 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.012, 7,  0.6, True,  True, 33, 0.64 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.012, 7,  0.9, True,  True, 39, 0.73 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.012, 7,  0.5, True,  True, 30, -0.54 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.012, 7,  0.8, True,  True, 33, -0.64 * pi],
           [7,  1, ORANGE, 0, 0, True,  0.012, 7,  0.1, True,  True, 39, -0.73 * pi],
           [5,  1, ORANGE, 0, 0, True,  0.009, 5,  0.8, True,  True, 40, 0.55 * pi],
           [5,  1, ORANGE, 0, 0, True,  0.009, 5,  0.1, True,  True, 40, -0.55 * pi],

           [7,  1, ORANGE, 0, 0, True,  0.012, 7,  0.1, True,  True, 78, 0],
           [13, 2, ORANGE, 0, 0, True,  0.02,  12, 0.2, True,  True, 60, 0],
           [9,  1, ORANGE, 0, 0, True,  0.014, 8,  0.3, True,  True, 90, 0],
           [9,  1, ORANGE, 0, 0, True,  0.014, 8,  0.7, True,  True, 69, -0.09 * pi],
           [9,  1, ORANGE, 0, 0, True,  0.014, 8,  0.9, True,  True, 69, 0.09 * pi],

           [20, 3, ORANGE, 0, 0, True,  0.03,  18, 0.3, True,  True, 47, 0.89 * pi],
           [20, 3, ORANGE, 0, 0, True,  0.031, 18, 0.7, True,  True, 47, -0.89 * pi],
           [22, 3, ORANGE, 0, 0, True,  0.035, 21, 0,   True,  True, 64, pi],
           [11, 1, ORANGE, 0, 0, True,  0.017, 10, 0,   True,  True, 82, 0.93 * pi],
           [11, 1, ORANGE, 0, 0, True,  0.017, 10, 0.4, True,  True, 82, -0.93 * pi],
           [10, 1, ORANGE, 0, 0, True,  0.015, 9,  0,   True,  True, 66, 0.82 * pi],
           [10, 1, ORANGE, 0, 0, True,  0.015, 9,  0.4, True,  True, 66, -0.82 * pi],

           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_43 = ((0, ),)

PARAMS_43 = [MAX_HEALTH_43, HEALTH_STATES_43, RADIUS_43, BODY_43, MAX_VEL_43,
             ACC_43, GUN_TYPE_43, BG_RADIUS_43, SUPERPOWER_43]
###############################################################################
MAX_VEL_44 = 0.23
ACC_44 = 0.0008
GUN_TYPE_44 = 'Gun44'
SUPERPOWER_44 = 'StickyExplosion'
MAX_HEALTH_44 = 500
RADIUS_44 = 95
BG_RADIUS_44 = 140
BODY_44 = [[23, 3, BLUE,   96,  0.23 * pi,  True,  0.035, 21, 0,   True,  False, 0,  0],
           [23, 3, BLUE,   96,  -0.23 * pi, True,  0.035, 21, 0.4, True,  False, 0,  0],
           [16, 2, BLUE,   62,  0.23 * pi,  True,  0.024, 14, 0.5, True,  False, 0,  0],
           [16, 2, BLUE,   62,  -0.23 * pi, True,  0.024, 14, 0.8, True,  False, 0,  0],
           [11, 1, BLUE,   40,  0.23 * pi,  True,  0.017, 10, 0.3, True,  False, 0,  0],
           [11, 1, BLUE,   40,  -0.23 * pi, True,  0.017, 10, 0.9, True,  False, 0,  0],
           [13, 1, BLUE,   41,  0.75 * pi,  True,  0.02,  12, 0.5, True,  False, 0,  0],
           [13, 1, BLUE,   41,  -0.75 * pi, True,  0.02,  12, 0.8, True,  False, 0,  0],
           [40, 2, BLUE,   90,  0.75 * pi,  True,  0.027, 16, 0,   True,  False, 0,  0],
           [40, 2, BLUE,   90,  -0.75 * pi, True,  0.027, 16, 0.4, True,  False, 0,  0],
           [34, 2, BLUE,   0,   0,          True,  0.024, 14, 0.8, True,  False, 0,  0],

           [11, 1, ORANGE, 90,  0.75 * pi,  True,  0.017, 10, 0,   True,  True,  32, 0.2 * pi],
           [11, 1, ORANGE, 90,  0.75 * pi,  True,  0.017, 10, 0.4, True,  True,  32, -0.2 * pi],
           [11, 1, ORANGE, 90,  0.75 * pi,  True,  0.017, 10, 0.7, True,  True,  48, 0.13 * pi],
           [11, 1, ORANGE, 90,  0.75 * pi,  True,  0.017, 10, 0.2, True,  True,  48, -0.13 * pi],
           [28, 4, ORANGE, 90,  0.75 * pi,  True,  0.044, 26, 0,   True,  True,  0,  0.00],
           [12, 1, ORANGE, 90,  0.75 * pi,  True,  0.019, 11, 0,   True,  True,  36, 0.77 * pi],
           [12, 1, ORANGE, 90,  0.75 * pi,  True,  0.019, 11, 0.4, True,  True,  36, -0.77 * pi],

           [11, 1, ORANGE, 90,  -0.75 * pi, True,  0.017, 10, 0.4, True,  True,  32, 0.2 * pi],
           [11, 1, ORANGE, 90,  -0.75 * pi, True,  0.017, 10, 0.8, True,  True,  32, -0.2 * pi],
           [11, 1, ORANGE, 90,  -0.75 * pi, True,  0.017, 10, 0.1, True,  True,  48, 0.13 * pi],
           [11, 1, ORANGE, 90,  -0.75 * pi, True,  0.017, 10, 0.6, True,  True,  48, -0.13 * pi],
           [28, 4, ORANGE, 90,  -0.75 * pi, True,  0.044, 26, 0.4, True,  True,  0,  0.00],
           [12, 1, ORANGE, 90,  -0.75 * pi, True,  0.019, 11, 0.4, True,  True,  36, 0.77 * pi],
           [12, 1, ORANGE, 90,  -0.75 * pi, True,  0.019, 11, 0.8, True,  True,  36, -0.77 * pi],

           [22, 3, ORANGE, 0,   0,          True,  0.035, 21, 0,   True,  False, 0,  0],
           [9,  1, ORANGE, 25,  0.5 * pi,   True,  0.015, 9,  0.4, True,  False, 0,  0],
           [9,  1, ORANGE, 25,  -0.5 * pi,  True,  0.015, 9,  0.8, True,  False, 0,  0],
           [9,  1, ORANGE, 25,  pi,         True,  0.015, 9,  0.2, True,  False, 0,  0],
           [9,  1, ORANGE, 25,  0,          True,  0.015, 9,  0.6, True,  False, 0,  0],
           [14, 2, ORANGE, 96,  0.23 * pi,  True,  0.022, 13, 0.6, True,  False, 0,  0],
           [14, 2, ORANGE, 96,  -0.23 * pi, True,  0.022, 13, 0.1, True,  False, 0,  0],
           [7,  1, ORANGE, 110, 0.2 * pi,   True,  0.012, 7,  0.4, True,  False, 0,  0],
           [7,  1, ORANGE, 110, -0.2 * pi,  True,  0.012, 7,  0.7, True,  False, 0,  0],

           [17, 1, VIOLET, 0,   0,          False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0,   0,          False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0,   0,          False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0,   0,          False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0,   0,          False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0,   0,          False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_44 = ((0, ),)

PARAMS_44 = [MAX_HEALTH_44, HEALTH_STATES_44, RADIUS_44, BODY_44, MAX_VEL_44,
             ACC_44, GUN_TYPE_44, BG_RADIUS_44, SUPERPOWER_44]
###############################################################################
MAX_VEL_50 = 0.7
ACC_50 = 0.003
GUN_TYPE_50 = 'Gun50'
SUPERPOWER_50 = 'Ghost'
MAX_HEALTH_50 = 1
RADIUS_50 = 60
BG_RADIUS_50 = 100
BODY_50 = [[26, 3, BLUE,   0, 0, True,  0.035, 22, 0,   True,  True, 0, 0],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.7, True,  True, 35, pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, True,  True, 32, 0.64 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, True,  True, 32, -0.64 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.7, True,  True, 32, 0.48 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.9, True,  True, 32, -0.48 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.9, True,  True, 47, 0.56 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.2, True,  True, 47, -0.56 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.6, True,  True, 56, 0.64 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.9, True,  True, 56, -0.64 * pi],
           # 10
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, True,  True, 56, 0.47 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, True,  True, 56, -0.47 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.2, True,  True, 35, 0.12 * pi],
           [9,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, True,  True, 35, -0.12 * pi],
           [14, 1, BLUE,   0, 0, True,  0.014, 8,  0.4, True,  True, 50, 0],

           [16, 2, ORANGE, 0, 0, True,  0.024, 15, 0,   True,  True, 0, 0],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.6, True,  True, 16, pi],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.8, True,  True, 23, 0],
           [9,  1, ORANGE, 0, 0, True,  0.012, 7,  0.1, True,  True, 37, 0],

           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_50 = ((0, ),)

PARAMS_50 = [MAX_HEALTH_50, HEALTH_STATES_50, RADIUS_50, BODY_50, MAX_VEL_50,
             ACC_50, GUN_TYPE_50, BG_RADIUS_50, SUPERPOWER_50]
###############################################################################
MAX_VEL_51 = 0.65
ACC_51 = 0.0025
GUN_TYPE_51 = 'Gun51'
SUPERPOWER_51 = 'Shurikens'
MAX_HEALTH_51 = 1
RADIUS_51 = 75
BG_RADIUS_51 = 100
BODY_51 = [[8,  1, BLUE,   0, 0, True,  0.012, 7,  0.3, True,  True, 67, 0.91 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.6, True,  True, 67, -0.91 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.9, True,  True, 56, 0.86 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.4, True,  True, 56, -0.86 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.7, True,  True, 76, 0.84 * pi],
           [14, 2, BLUE,   0, 0, True,  0.02,  12, 0.4, True,  True, 76, -0.84 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.1, True,  True, 40, 0.48 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.8, True,  True, 40, -0.48 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.5, True,  True, 40, 0.58 * pi],
           [8,  1, BLUE,   0, 0, True,  0.012, 7,  0.0, True,  True, 40, -0.58 * pi],

           [12, 2, BLUE,   0, 0, True,  0.02,  12, 0.0, True,  True, 63, 0.42 * pi],
           [12, 2, BLUE,   0, 0, True,  0.02,  12, 0.4, True,  True, 63, -0.42 * pi],
           [18, 3, BLUE,   0, 0, True,  0.027, 16, 0.5, True,  True, 60, 0.54 * pi],
           [18, 3, BLUE,   0, 0, True,  0.027, 16, 0.9, True,  True, 60, -0.54 * pi],
           [12, 2, BLUE,   0, 0, True,  0.02,  12, 0.2, True,  True, 66, 0.65 * pi],
           [12, 2, BLUE,   0, 0, True,  0.02,  12, 0.8, True,  True, 66, -0.65 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.2, True,  True, 76, 0.11 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.8, True,  True, 76, -0.11 * pi],
           [12, 2, BLUE,   0, 0, True,  0.02,  12, 0.7, True,  True, 62, 0.13 * pi],
           [12, 2, BLUE,   0, 0, True,  0.02,  12, 0.3, True,  True, 62, -0.13 * pi],

           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.5, True,  True, 57, 0.22 * pi],
           [10, 1, BLUE,   0, 0, True,  0.014, 8,  0.0, True,  True, 57, -0.22 * pi],
           [21, 3, BLUE,   0, 0, True,  0.032, 19, 0.1, True,  True, 45, pi],
           [21, 3, BLUE,   0, 0, True,  0.032, 19, 0.5, True,  True, 43, 0],
           [36, 1, BLUE,   0, 0, True,  0.029, 17, 0,   True,  True, 0,  0],

           [21, 3, ORANGE, 0, 0, True,  0.035, 21, 0.1, True,  True, 4,  0],
           [10, 1, ORANGE, 0, 0, True,  0.014, 8,  0,   True,  True, 26, 0.68 * pi],
           [10, 1, ORANGE, 0, 0, True,  0.014, 8,  0.4, True,  True, 26, -0.68 * pi],
           [10, 1, ORANGE, 0, 0, True,  0.014, 8,  0.7, True,  True, 26,  pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.9, True,  True, 23, 0.00],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.6, True,  True, 32, 0.00],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.2, True,  True, 29, 0.22 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.2, True,  True, 29, -0.22 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.4, True,  True, 37, 0.17 * pi],
           [6,  1, ORANGE, 0, 0, True,  0.01,  6,  0.4, True,  True, 37, -0.17 * pi],
           [12, 1, ORANGE, 0, 0, True,  0.017, 10, 0.7, True,  True, 55,  pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.3, True,  True, 70, 0.93 * pi],
           [8,  1, ORANGE, 0, 0, True,  0.012, 7,  0.9, True,  True, 70, -0.93 * pi],

           [17, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 25, 0.8 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 23, 0.55 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 26, -0.45 * pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 27, pi],
           [8,  1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 17, -0.9 * pi],
           [10, 1, VIOLET, 0, 0, False, 0,     0,  0,   False, True, 29, 0.25 * pi]]

HEALTH_STATES_51 = ((0, ),)

PARAMS_51 = [MAX_HEALTH_51, HEALTH_STATES_51, RADIUS_51, BODY_51, MAX_VEL_51,
             ACC_51, GUN_TYPE_51, BG_RADIUS_51, SUPERPOWER_51]
###############################################################################
PLAYER_PARAMS = {(0, 0): PARAMS_00,
                 (1, 0): PARAMS_10,
                 (1, 1): PARAMS_11,
                 (1, 2): PARAMS_12,
                 (2, 0): PARAMS_20,
                 (2, 1): PARAMS_21,
                 (2, 2): PARAMS_22,
                 (2, 3): PARAMS_23,
                 (3, 0): PARAMS_30,
                 (3, 1): PARAMS_31,
                 (3, 2): PARAMS_32,
                 (3, 3): PARAMS_33,
                 (3, 4): PARAMS_34,
                 (3, 5): PARAMS_35,
                 (4, 0): PARAMS_40,
                 (4, 1): PARAMS_41,
                 (4, 2): PARAMS_42,
                 (4, 3): PARAMS_43,
                 (4, 4): PARAMS_44,
                 (4, 5): PARAMS_00,
                 (5, 0): PARAMS_50,
                 (5, 1): PARAMS_51,
                 (5, 2): PARAMS_00,
                 (5, 3): PARAMS_00,
                 (5, 4): PARAMS_00,
                 (5, 5): PARAMS_00}
###############################################################################


def convert_body(body):
    for i in range(len(body)):
        if body[i][2] == ORANGE: body[i][2] = 'ORANGE'
        elif body[i][2] == BLUE: body[i][2] = 'BLUE'
        elif body[i][2] == VIOLET: body[i][2] = 'VIOLET'
        elif body[i][2] == LIGHT_ORANGE: body[i][2] = 'LIGHT_ORANGE'
        body[i] = [body[i][0], body[i][1], body[i][2], 0, 0, body[i][5], body[i][6], body[i][7], body[i][8], body[i][10], body[i][9], body[i][3], body[i][4]]
    return body


def align_body(body):
    body = convert_body(body)
    max_sizes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(body[0])):
        for j in range(len(body)):
            if i == 2:
                if body[j][2] == ORANGE:
                    body[j][2] = 'ORANGE'
                elif body[j][2] == BLUE:
                    body[j][2] = 'BLUE'
                elif body[j][2] == VIOLET:
                    body[j][2] = 'VIOLET'
            elif i == 12:
                sign = '' if body[j][12] > 0 else '-'
                if body[j][12] == 0:
                    body[j][12] = '0.00'
                elif body[j][12] == pi:
                    body[j][12] = 'pi'
                else:
                    body[j][12] = sign + str(round(abs(body[j][12]/pi), 3)) + ' * pi'
            else:
                body[j][i] = str(body[j][i])
            if len(body[j][i]) > max_sizes[i]:
                max_sizes[i] = len(str(body[j][i]))

    for i in range(len(body)):
        print('           [' + body[i][0] + ', ' + ' '*(max_sizes[0]-len(body[i][0])) +
              body[i][1] + ', ' + ' ' * (max_sizes[1] - len(body[i][1])) +
              body[i][2] + ', ' + ' ' * (max_sizes[2] - len(body[i][2])) +
              body[i][3] + ', ' + ' ' * (max_sizes[3] - len(body[i][3])) +
              body[i][4] + ', ' + ' ' * (max_sizes[4] - len(body[i][4])) +
              body[i][5] + ', ' + ' ' * (max_sizes[5] - len(body[i][5])) +
              body[i][6] + ', ' + ' ' * (max_sizes[6] - len(body[i][6])) +
              body[i][7] + ', ' + ' ' * (max_sizes[7] - len(body[i][7])) +
              body[i][8] + ', ' + ' ' * (max_sizes[8] - len(body[i][8])) +
              body[i][9] + ', ' + ' ' * (max_sizes[9] - len(body[i][9])) +
              body[i][10] + ', ' + ' ' * (max_sizes[10] - len(body[i][10])) +
              body[i][11] + ', ' + ' ' * (max_sizes[11] - len(body[i][11])) +
              body[i][12] +'],')

#convert_body(BODY_00)
#align_body(BODY_33)
