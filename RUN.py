#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from underwater import Underwater
from data_cursor import CURSOR


def main():
    pygame.mixer.pre_init(44100, 16, 4, 1024)
    pygame.init()
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP,
                              pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])
    cursor = pygame.cursors.compile(CURSOR, black='.', white='X')
    pygame.mouse.set_cursor((32, 32), (0, 0), *cursor)

    Underwater().run()


if __name__ == '__main__':
    main()