#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colors import BUBBLE_COLOR, BUBBLE_COLOR_2


BUBBLE_MAX_VEL = 0.4
BUBBLE_ACC = 0.0015
BUBBLE_RADIUS = [12, 18, 24]
BUBBLE_HEALTH = [1, 5, 25]
BUBBLE_BODY = [((BUBBLE_RADIUS[0], 2, BUBBLE_COLOR,   0, 0, True, 0.018, 11, 0, True, False),),
               ((BUBBLE_RADIUS[1], 2, BUBBLE_COLOR,   0, 0, True, 0.014, 8,  0, True, False),),
               ((BUBBLE_RADIUS[2], 3, BUBBLE_COLOR_2, 0, 0, True, 0.019, 11, 0, True, False),)]
