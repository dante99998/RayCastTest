import pygame as pg
import random as rand
from math import cos, sin, pi, trunc

import numpy as np

from settings import *
from utils import *

d2r = pi / 180 # degree to radians 
r2d = 180 / pi # radians to degree
fov = pi / 3 # field of view

cc = CommonColors()
colors = (cc.White, cc.Silver, cc.Gray, cc.Red, cc.Maroon, cc.Yellow, cc.Olive, cc.Lime, cc.Green, cc.Aqua, cc.Teal, cc.Blue)

class Player:
    x = 50
    y = 50
    w = 5
    h = 5
    color = cc.Black

    a = 0

    def __init__(self):
        pass

class Game:
    is_running = True
    dir = DIR_RIGHT
    
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.display = pg.display.set_mode(SCR_SIZE)
        self.bg_color = cc.White

        self.player = Player()

        # pg.draw.rect(self.display , RED, (10,10, 100, 100))
        # self.display.fill(cc.White)

        # 16x16
        self.map = "0000222222220000"\
                   "1              0"\
                   "1      11111   0"\
                   "1     0        0"\
                   "0     0  1110000"\
                   "0     3        0"\
                   "0   10000      0"\
                   "0   0   11100  0"\
                   "0   0   0      0"\
                   "0   0   1  00000"\
                   "0       1      0"\
                   "2       1      0"\
                   "0       0      0"\
                   "0 0000000      0"\
                   "0              0"\
                   "0002222222200000"

        self.draw_map(self.map, self.display)
        self.draw_player(self.player, self.display)
        # self.draw_laser_line(self.player, self.display, self.map, self.player.a)
        self.draw_fov(self.player, self.display, self.map)

        self.once = True

    def draw_map(self, g_map, display):
        rect_w = int(SCR_WIDTH / MAP_WIDTH)
        rect_h = int(SCR_HEIGHT / MAP_HIEGHT)
        for i in range(MAP_HIEGHT):
            for j in range(MAP_WIDTH):
                ind = i + MAP_WIDTH * j
                if(g_map[ind] == ' '): continue
                rect_x = i * rect_w
                rect_y = j * rect_h
                pg.draw.rect(display, cc.Aqua, (rect_x, rect_y, rect_w, rect_h))

    def draw_player(self, player, display):
        p = player
        pg.draw.rect(display, p.color, (p.x, p.y, p.w, p.h))

    def draw_laser_line(self, player, display, gmap, angle):
        rect_w = SCR_WIDTH / MAP_WIDTH
        rect_h = SCR_HEIGHT / MAP_HIEGHT

        for i in range(SCR_WIDTH):
            x = ftoi(player.x + i * cos(angle * d2r))
            y = ftoi(player.y + i * sin(angle * d2r))
            mx = int(x / rect_w)
            my = int(y / rect_h)

            mi = mx + my*MAP_WIDTH
            if gmap[mi] != ' ': break
        
            display.set_at((x, y), cc.Black)

    def draw_fov(self, player, display, gmap):
        for i in range(60):
            angle = i + player.a
            self.draw_laser_line(player, display, gmap, angle)
        
    def render(self):
        pg.display.update()

    def update(self):
        self.clock.tick(FPS)

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.is_running = False

        key_pressed = pg.key.get_pressed()
                
        if key_pressed[pg.K_d]:
            self.player.x += 1 
        elif key_pressed[pg.K_a]:
            self.player.x -= 1
        elif key_pressed[pg.K_w]:
            self.player.y -= 1
        elif key_pressed[pg.K_s]:
            self.player.y += 1
        # elif key_pressed[pg.K_UP]:
        #     self.display.fill(BLACK)
        # elif key_pressed[pg.K_DOWN]:
        #     self.display.fill(BLACK)
        if key_pressed[pg.K_LEFT]:
            self.player.a += 1
        if key_pressed[pg.K_RIGHT]:
            self.player.a -= 1

        self.display.fill(cc.White)
        self.draw_map(self.map, self.display)
        self.draw_player(self.player, self.display)
        # self.draw_laser_line(self.player, self.display, self.map, self.player.a)
        self.draw_fov(self.player, self.display, self.map)
            

    def quit(self):
        pg.quit()

