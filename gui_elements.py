#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
import numpy as np
from math import copysign, hypot, sqrt, copysign

import config as c

from data_start_menu import TriangleData, PlayLabelData, StartButtonData
import colors as col


class PauseButton:
    def __init__(self, top_x, top_y, is_pressed, text, colors=(col.DARK_GREY, col.LIGHT_GREY)):
        self.x = top_x
        self.y = top_y
        self.w = 160
        self.h = 40
        self.w2 = self.w // 2
        self.h2 = self.h // 2

        self.text = text
        pg.font.init()
        font = pg.font.SysFont('Arial', 18, True)
        self.text_surface = font.render(text, True, col.WHITE)
        self.text_x = self.x + self.w2 - self.text_surface.get_width()//2
        self.text_y = self.y + self.h2 - self.text_surface.get_height()//2

        self.circle_x1 = self.x+self.h2
        self.circle_y1 = self.y+self.h2
        self.circle_x2 = self.x+self.w-self.h2
        self.circle_y2 = self.y+self.h2

        self.is_pressed = is_pressed
        self.colors = colors
        self.color = self.colors[1] if self.is_pressed else self.colors[0]
        self.rect = pg.Rect(self.x+self.h2, self.y, self.w-self.h, self.h)

    def cursor_on_button(self, pos):
        return self.rect.collidepoint(pos) or \
                hypot(pos[0]-self.circle_x1, pos[1]-self.circle_y1) <= self.h2 or \
                hypot(pos[0]-self.circle_x2, pos[1]-self.circle_y2) <= self.h2

    def update_color(self, pos):
        if self.cursor_on_button(pos):
            self.color = self.colors[1]
        elif not self.is_pressed:
            self.color = self.colors[0]

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect)
        pg.draw.circle(surface, self.color, (self.circle_x1, self.circle_y1), self.h2)
        pg.draw.circle(surface, self.color, (self.circle_x2, self.circle_y2), self.h2)
        surface.blit(self.text_surface, (self.text_x, self.text_y))
# _________________________________________________________________________________________________


class ExitButton:
    def __init__(self):
        self.x = 70
        self.y = 540
        self.r = 23
        self.d = int(self.r / sqrt(2))
        self.colors = ((33, 51, 62), col.LIGHT_GREY)
        self.color = self.colors[0]

    def cursor_on_button(self, pos):
        return hypot(pos[0] - self.x, pos[1] - self.y) <= self.r

    def update_color(self, pos):
        self.color = self.colors[1] if self.cursor_on_button(pos) else self.colors[0]

    def draw(self, surface):
        pg.draw.circle(surface, col.WHITE, (self.x, self.y), self.r)
        pg.draw.circle(surface, self.color, (self.x, self.y), self.r-3)
        pg.draw.line(surface, col.WHITE, (self.x - self.d + 1, self.y + self.d - 1),
                                         (self.x + self.d - 1, self.y - self.d + 1), 4)
        pg.draw.line(surface, col.WHITE, (self.x - self.d + 1, self.y - self.d + 1),
                                         (self.x + self.d - 1, self.y + self.d - 1), 4)
# _________________________________________________________________________________________________


class SideButton:
    def __init__(self, top_x, top_y, name, is_pressed):
        self.x = top_x
        self.y = top_y
        self.w, self.h = 60, 100
        self.is_pressed = is_pressed

        self.surface = pg.Surface((self.w, self.h))
        self.setup_surface(is_pressed)

        pg.font.init()
        size = 18 if len(name) >= 10 else 22
        font = pg.font.Font(c.FONT_2, size)
        text = font.render(name, True, col.WHITE)
        self.name = pg.transform.rotate(text, 90)
        self.name_x = self.x + (self.w - self.name.get_width()) // 2
        self.name_y = self.y + (self.h - self.name.get_height()) // 2

    def setup_surface(self, is_pressed):
        self.surface.fill(col.COLOR_KEY)
        pg.draw.rect(self.surface, col.BLACK, pg.Rect(15, 0, 45, 100))
        pg.draw.rect(self.surface, col.BLACK, pg.Rect(0, 15, 15, 70))
        pg.draw.circle(self.surface, col.BLACK, (15, 15), 15)
        pg.draw.circle(self.surface, col.BLACK, (15, 85), 15)

        self.surface.set_colorkey(col.COLOR_KEY)
        alpha = 125 if is_pressed else 70
        self.surface.set_alpha(alpha)

    def is_chosen(self, pos):
        return self.x <= pos[0] <= self.x+self.w and self.y <= pos[1] <= self.y+self.h

    def set_pressed(self):
        self.is_pressed = True
        self.surface.set_alpha(125)

    def set_unpressed(self):
        self.is_pressed = False
        self.surface.set_alpha(70)

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        screen.blit(self.name, (self.name_x, self.name_y))
# _________________________________________________________________________________________________


class UpgradeCaption:
    def __init__(self):
        self.x = 30
        self.y = -80
        self.Y0 = -80
        self.Y1 = 10
        self.vel_y = (self.Y1 - self.Y0) / 350
        self.vel_y_sign = copysign(1, self.vel_y)
        self.caption = None

    def set_caption(self, text):
        w, h = c.SCR_W - 60, 70
        self.caption = pg.Surface((w, h))
        self.caption.fill(col.COLOR_KEY)
        edge = 10
        pg.draw.rect(self.caption, col.WHITE, pg.Rect(edge, 0, w - 2 * edge, edge))
        pg.draw.rect(self.caption, col.WHITE, pg.Rect(0, edge, w, h - 2 * edge))
        pg.draw.rect(self.caption, col.WHITE, pg.Rect(edge, h - edge, w - 2 * edge, edge))
        pg.draw.circle(self.caption, col.WHITE, (edge, edge), edge)
        pg.draw.circle(self.caption, col.WHITE, (w - edge, edge), edge)
        pg.draw.circle(self.caption, col.WHITE, (w - edge, h - edge), edge)
        pg.draw.circle(self.caption, col.WHITE, (edge, h - edge), edge)

        pg.font.init()
        font = pg.font.Font(c.FONT_1, 52)
        label = font.render(text, True, col.UPG_LABEL_COLOR)
        self.caption.blit(label, (35, 15))

        self.caption.set_alpha(235)
        self.caption.set_colorkey(col.COLOR_KEY)

    def reset_velocity(self):
        self.vel_y = abs(self.vel_y)

    def update_pos(self, dt):
        self.y += self.vel_y * dt
        if self.vel_y_sign * self.y > self.vel_y_sign * self.Y1:
            self.y = self.Y1
        elif self.vel_y_sign * self.y < self.vel_y_sign * self.Y0:
            self.y = self.Y0

    def draw(self, surface):
        surface.blit(self.caption, (self.x, self.y))
# _________________________________________________________________________________________________


class UpgradeButton:
    def __init__(self, text_0, text_1, text_2, text_3, text_4,
                 text_5, labels, button_type, player_state):

        self.player_state = player_state
        self.button_type = button_type

        self.w = 220 if self.button_type in [1, 2, 3] else 300
        self.h = 460
        self.w2, self.h2 = self.w//2, self.h//2

        if self.button_type in [1, 4]:
            self.x, self.y = -self.w, 100
            self.X0, self.Y0 = -self.w, 100
            self.X1 = 30 if self.button_type == 1 else 65
            self.Y1 = 100
        elif self.button_type == 2:
            self.x, self.y = 290, c.SCR_H
            self.X0, self.Y0 = 290, c.SCR_H
            self.X1, self.Y1 = 290, 100
        elif self.button_type in [3, 5]:
            self.x, self.y = c.SCR_W, 100
            self.X0, self.Y0 = c.SCR_W, 100
            self.X1 = c.SCR_W-self.w-30 if self.button_type == 3 else c.SCR_W-self.w-65
            self.Y1 = 100

        self.vel_x = (self.X1 - self.X0) / 350
        self.vel_x_sign = copysign(1, self.vel_x)
        self.vel_y = (self.Y1 - self.Y0) / 350
        self.vel_y_sign = copysign(1, self.vel_y)

        self.labels = self.setup_labels(labels, tank_name=text_0)
        self.texts = self.setup_texts(text_1, text_2, text_3)

        self.bg = self.setup_bg()

    @staticmethod
    def setup_labels(texts, tank_name):
        labels = []
        pg.font.init()
        font = pg.font.Font(c.FONT_1, 30)
        labels.append(font.render(texts[0], True, col.UPG_LABEL_COLOR))
        font = pg.font.Font(c.FONT_2, 19)
        labels.append(font.render(tank_name, True, col.BLACK))
        labels.append(font.render(texts[1], True, col.BLACK))
        labels.append(font.render(texts[2], True, col.BLACK))
        del font
        return labels

    def setup_texts(self, text_1, text_2, text_3):
        texts = []
        texts.append(TextBox(text_1, None, 18, False, col.BLACK, (self.w2, 195)))
        texts.append(TextBox(text_2, None, 18, False, col.BLACK, (self.w2, 270)))
        texts.append(TextBox(text_3, None, 18, False, col.BLACK, (5, 335), False))
        return texts

    def setup_bg(self):
        bg = pg.Surface((self.w, self.h))
        bg.fill(col.COLOR_KEY)
        edge = 10
        pg.draw.rect(bg, col.WHITE, pg.Rect(edge, 0, self.w-2*edge, self.h))
        pg.draw.rect(bg, col.WHITE, pg.Rect(0, edge, edge, self.h-2*edge))
        pg.draw.rect(bg, col.WHITE, pg.Rect(self.w-edge, edge, edge, self.h-2*edge))

        pg.draw.circle(bg, col.WHITE, (edge, edge), edge)
        pg.draw.circle(bg, col.WHITE, (self.w-edge, edge), edge)
        pg.draw.circle(bg, col.WHITE, (self.w-edge, self.h-edge), edge)
        pg.draw.circle(bg, col.WHITE, (edge, self.h-edge), edge)

        pg.draw.circle(bg, col.UPG_CIRCLE_COLOR_1, (self.w2, 66), 33)
        pg.draw.circle(bg, col.UPG_CIRCLE_COLOR_2, (self.w2, 66), 30)
        pg.draw.circle(bg, col.UPG_CIRCLE_COLOR_3, (self.w2, 66), 27)
        pg.draw.polygon(bg, col.UPG_ARROW_COLOR,
                        ((self.w2, 50), (self.w2+11, 65), (self.w2+4, 65), (self.w2+4, 80),
                         (self.w2-4, 80), (self.w2-4, 65), (self.w2-11, 65)))

        bg.blit(self.labels[0], ((self.w-self.labels[0].get_size()[0])//2, 5))
        bg.blit(self.labels[1], ((self.w-self.labels[1].get_size()[0])//2, 100))
        bg.blit(self.labels[2], ((self.w-self.labels[2].get_size()[0])//2, 165))
        bg.blit(self.labels[3], ((self.w-self.labels[3].get_size()[0])//2, 240))

        for text in self.texts:
            text.draw(bg)

        bg.set_alpha(230)
        bg.set_colorkey(col.COLOR_KEY)
        return bg

    def cursor_on_button(self, pos):
        return self.x <= pos[0] <= self.x+self.w and self.y <= pos[1] <= self.y+self.h

    def update(self, dt):
        self.x += self.vel_x * dt
        if self.vel_x_sign * self.x > self.vel_x_sign * self.X1:
            self.x = self.X1
        elif self.vel_x_sign * self.x < self.vel_x_sign * self.X0:
            self.x = self.X0

        self.y += self.vel_y * dt
        if self.vel_y_sign * self.y > self.vel_y_sign * self.Y1:
            self.y = self.Y1
        elif self.vel_y_sign * self.y < self.vel_y_sign * self.Y0:
            self.y = self.Y0

        alpha = 255 if self.cursor_on_button(pg.mouse.get_pos()) else 230
        self.bg.set_alpha(alpha)

    def draw(self, surface):
        surface.blit(self.bg, (int(self.x), int(self.y)))
# _________________________________________________________________________________________________


class StatusBar:
    def __init__(self, x, y, width, height, value, max_value):
        self.width = width
        self.value = value
        self.max_value = max_value
        self.k = width/max_value if max_value else 0
        self.color = col.STATUS_BAR_BG

        self.edge_rect = pg.Rect(x, y, width, height)
        self.value_rect = pg.Rect(x, y, self.k * value, height)

    def set_value(self, value):
        self.value = min(value, self.max_value)
        self.value_rect.width = self.k * self.value

    def add_value(self, value):
        self.value = min(self.value + value, self.max_value)
        self.value_rect.width = self.k * self.value

    def set_max_value(self, max_value):
        self.max_value = max_value
        self.k = self.width / max_value if max_value else 0

    def move(self, x, y):
        self.edge_rect.x = x
        self.edge_rect.y = y
        self.value_rect.x = x
        self.value_rect.y = y

    def draw(self, surface):
        pg.draw.rect(surface, col.WHITE, self.edge_rect, 1)
        pg.draw.rect(surface, self.color, self.value_rect)
# _________________________________________________________________________________________________


class TextBox:
    def __init__(self, text, font, size, is_bold, color, pos_0, centralised=True):
        self.color = color
        self.x, self.y = pos_0[0], pos_0[1]
        self.centralised = centralised
        self.text = text

        pg.font.init()
        if font is None:
            self.font = pg.font.SysFont('calibri', size, is_bold)
        elif font not in ['Arial', 'calibri']:
            self.font = pg.font.Font(font, size)
        else:
            self.font = pg.font.SysFont(font, size, is_bold)

        self.letter_h = self.font.size('A')[1]
        self.box = self.make_box(text)
        self.w, self.h = self.get_box_size()

    def make_box(self, text):
        box = []
        for string in text:
            box.append(self.font.render(string, True, self.color, None))
        return box

    def get_box_size(self):
        width = 0
        for i in range(len(self.box)):
            width = max(self.box[i].get_size()[0], width)
        height = len(self.box) * self.letter_h
        return width, height

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def is_on_screen(self):
        return -self.w <= self.x <= c.SCR_W and -self.h <= self.y <= c.SCR_H

    def draw(self, surface, dx=0, dy=0):
        if self.is_on_screen():
            y = self.y
            for string in self.box:
                x = self.x - string.get_width()/2 if self.centralised else self.x
                surface.blit(string, (int(x) - int(dx), int(y)-int(dy)))
                y += self.letter_h
# _________________________________________________________________________________________________


class Triangle(TriangleData):
    def __init__(self, pos, k):
        TriangleData.__init__(self)
        self.pos = pos

        self.dots = self.TRIANGLE_DOTS_MIN.copy()
        self.dots_delta = k * (self.TRIANGLE_DOTS_MAX - self.TRIANGLE_DOTS_MIN)

        self.edge_dots = self.TRIANGLE_EDGE_DOTS_MIN.copy()
        self.edge_dots_delta = k * (self.TRIANGLE_EDGE_DOTS_MAX - self.TRIANGLE_EDGE_DOTS_MIN)

        self.color = self.TRIANGLE_COLOR_MIN.copy()
        self.color_delta = k * (self.TRIANGLE_COLOR_MAX - self.TRIANGLE_COLOR_MIN)

    def draw(self, surface):
        pg.draw.polygon(surface, col.WHITE, self.edge_dots + self.pos)
        pg.draw.polygon(surface, self.color, self.dots + self.pos)
# _________________________________________________________________________________________________


class PlayLabel(PlayLabelData):
    def __init__(self, text, k):
        PlayLabelData.__init__(self)
        self.text = text
        self.color = self.PLAY_LABEL_COLOR_MIN.copy()
        self.color_delta = k * (self.PLAY_LABEL_COLOR_MAX - self.PLAY_LABEL_COLOR_MIN)

        pg.font.init()
        self.font = pg.font.Font(c.FONT_1, 36)
        self.text_surface = self.font.render(text, True, self.color)

        self.x = c.SCR_W2 - self.font.size(text)[0] // 2
        self.y = 0.72*c.SCR_H - self.font.size(text)[1] // 2

    def set_text(self, text):
        self.text_surface = self.font.render(text, True, self.color)

    def draw(self, surface):
        surface.blit(self.text_surface, (self.x, self.y))
# _________________________________________________________________________________________________


class StartButton(StartButtonData):
    def __init__(self):
        StartButtonData.__init__(self)
        self.is_scaling = False
        self.is_visible = True

        self.color = self.BUTTON_COLOR_MIN.copy()
        self.color_delta = self.K * (self.BUTTON_COLOR_MAX - self.BUTTON_COLOR_MIN)

        self.a = self.BUTTON_A_MIN
        self.a_delta = self.K * (self.BUTTON_A_MAX - self.BUTTON_A_MIN)
        self.b = self.BUTTON_B_MIN
        self.b_delta = self.K * (self.BUTTON_B_MAX - self.BUTTON_B_MIN)
        self.x = c.SCR_W2
        self.y = c.SCR_H + self.b
        self.velocity = (0.125*c.SCR_H + self.b) / 250

        self.triangle = Triangle(np.array([self.x, self.y], dtype=float), self.K)

        self.play_label = None

    def reset(self):
        self.is_scaling = False
        self.is_visible = True
        self.a = self.BUTTON_A_MIN
        self.b = self.BUTTON_B_MIN
        self.adjust_pos(1)

    def adjust_pos(self, marker):
        if marker == -1:
            self.x = c.SCR_W2
            self.y = 0.875 * c.SCR_H
            self.triangle.pos = np.array([self.x, self.y], dtype=float)
        elif marker == 1:
            self.x = c.SCR_W2
            self.y = c.SCR_H + self.b
            self.triangle.pos = np.array([self.x, self.y], dtype=float)

    def set_play_label(self, text):
        self.play_label = PlayLabel(text, self.K)

    def cursor_on_button(self, x, y):
        if (self.x-x)*(self.x-x) / (self.a*self.a) + \
           (self.y-y)*(self.y-y) / (self.b*self.b) <= 1:
            return True
        return False

    def scale(self, dt, k):
        self.triangle.dots += self.triangle.dots_delta * k*dt
        self.triangle.edge_dots += self.triangle.edge_dots_delta * k*dt
        self.triangle.color += self.triangle.color_delta * k*dt

        self.a += self.a_delta * k*dt
        self.b += self.b_delta * k*dt
        self.color += self.color_delta * k*dt

        self.play_label.color += self.play_label.color_delta * k*dt

        if k > 0 and self.a > self.BUTTON_A_MAX:
            self.a = self.BUTTON_A_MAX
            self.b = self.BUTTON_B_MAX
            self.color = self.BUTTON_COLOR_MAX.copy()

            self.triangle.dots = self.triangle.TRIANGLE_DOTS_MAX.copy()
            self.triangle.edge_dots = self.triangle.TRIANGLE_EDGE_DOTS_MAX.copy()
            self.triangle.color = self.triangle.TRIANGLE_COLOR_MAX.copy()

            self.play_label.color = self.play_label.PLAY_LABEL_COLOR_MAX.copy()
            self.play_label.set_text(self.play_label.text)
            self.is_scaling = False

        elif k < 0 and self.a < self.BUTTON_A_MIN:
            self.a = self.BUTTON_A_MIN
            self.b = self.BUTTON_B_MIN
            self.color = self.BUTTON_COLOR_MIN.copy()

            self.triangle.dots = self.triangle.TRIANGLE_DOTS_MIN.copy()
            self.triangle.edge_dots = self.triangle.TRIANGLE_EDGE_DOTS_MIN.copy()
            self.triangle.color = self.triangle.TRIANGLE_COLOR_MIN.copy()

            self.play_label.color = self.play_label.PLAY_LABEL_COLOR_MIN.copy()
            self.play_label.set_text('')
            self.is_scaling = False
        else:
            self.play_label.set_text(self.play_label.text)
            self.is_scaling = True

    def move(self, dy):
        self.y += dy
        self.triangle.pos[1] += dy

    def update(self, x, y, dt, time, marker):
        if not marker:
            k = 1 if self.cursor_on_button(x, y) else -1
            self.scale(dt, k)

        elif marker == -1:
            if time < 300:
                self.is_visible = True if (time // 50) % 2 else False
            elif 300 <= time < 750:
                self.scale(dt, -1)
            elif 750 <= time <= 1000:
                dy = self.velocity * dt
                self.move(dy)

        elif marker == 1:
            if 1500 >= time >= 1250:
                dy = -self.velocity * dt
                self.move(dy)

    def draw(self, surface):
        if self.is_visible:
            rect = pg.Rect(int(self.x-self.a), int(self.y-self.b),
                           int(2*self.a), int(2*self.b))
            pg.draw.ellipse(surface, self.color, rect)
            self.triangle.draw(surface)
        self.play_label.draw(surface)
# _________________________________________________________________________________________________


class PopupWindow:
    def __init__(self, x, y, width, height, vel, duration):
        self.x = x
        self.y = y
        self.Y0 = y
        self.Y1 = y+height+10 if vel > 0 else y-height-10
        self.width = width
        self.height = height
        self.time = 0
        self.vel = vel
        self.vel_sign = copysign(1, self.vel)
        self.duration = duration
        self.state_marker = 0
        self.background = self.set_background(width, height)

    @staticmethod
    def set_background(width, height):
        surface = pg.Surface((width, height), 0x00010000)
        surface.fill(col.POPUP_WINDOW_COLOR)
        transparent_color = (0, 0, 0, 0)

        pixels = pg.PixelArray(surface)
        for x in range(0, width//2):
            for y in range(0, height//2):
                if x <= 5 and y <= 5 and (x-5)*(x-5)+(y-5)*(y-5) >= 25:
                    pixels[x, y] = transparent_color
                    pixels[width-1 - x, y] = transparent_color
                    pixels[x, height-1 - y] = transparent_color
                    pixels[width-1 - x, height-1 - y] = transparent_color
        surface = pixels.make_surface()

        return surface

    def activate(self):
        if self.state_marker != 3:
            self.state_marker = 1
        self.time = 0

    def reset(self):
        self.state_marker = 0
        self.time = 0
        self.y = self.Y0

    def update(self, dt):
        if self.state_marker == 1:  # window appears
            self.y += self.vel * dt
            if self.vel_sign * self.y > self.vel_sign * self.Y1:
                self.state_marker = 3
                self.y = self.Y1
        elif self.state_marker == 2:  # window hides
            self.y -= self.vel * dt
            if self.vel_sign * self.y < self.vel_sign * self.Y0:
                self.state_marker = 0  # window is closed
                self.y = self.Y0
        elif self.state_marker == 3:  # window is opened
            self.time += dt
            if self.time >= self.duration:
                self.state_marker = 2
                self.time = 0

    def is_on_screen(self):
        return self.vel_sign*self.Y0 < self.vel_sign*self.y <= self.vel_sign*self.Y1
# _________________________________________________________________________________________________
