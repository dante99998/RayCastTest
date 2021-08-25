import pygame as pg
import random as rand
from math import cos, sin, pi, sqrt

import numpy as np

from settings import *
from utils import *

def sqr(x):
    return x * x

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
        self.wall_color = {'0': cc.Blue, '1': cc.Green, '2': cc.Red, '3': cc.Silver}

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

        self.rect_w = SCR_WIDTH // MAP_WIDTH
        self.rect_h = SCR_HEIGHT // MAP_HIEGHT

        self.draw_map(self.map, self.display)
        self.draw_player(self.player, self.display)
        # self.draw_laser_line(self.player, self.display, self.map, self.player.a)
        self.draw_fov(self.player, self.display, self.map)

        self.once = True

    def draw_map(self, g_map, display):
        for i in range(MAP_HIEGHT):
            for j in range(MAP_WIDTH):
                ind = i + MAP_WIDTH * j
                if(g_map[ind] == ' '): continue
                rect_x = i * self.rect_w
                rect_y = j * self.rect_h
                pg.draw.rect(display, cc.Aqua, (rect_x, rect_y, self.rect_w, self.rect_h))

    def draw_player(self, player, display):
        p = player
        pg.draw.rect(display, p.color, (p.x, p.y, p.w, p.h))

    def draw_laser_line(self, player, display, gmap, angle):
        for i in range(SCR_WIDTH):
            x = ftoi(player.x + i * cos(angle * d2r))
            y = ftoi(player.y + i * sin(angle * d2r))
            mx = x // self.rect_w # map x coord
            my = y // self.rect_h # and y

            mi = mx + my*MAP_WIDTH
            wc = gmap[mi] # wall character
            if wc != ' ': return x, y, self.wall_color[wc]
      
            display.set_at((x, y), cc.Black)

    def draw_fov(self, player, display, gmap):
        ff = 10 # fence factor
        dist_coef = cos(1 * d2r)
        for i in range(fov):
            angle = i + player.a
            wx, wy, wc = self.draw_laser_line(player, display, gmap, angle) # wall (x, y, color)

            dx = abs(wx - player.x) # distance x
            dy = abs(wy - player.y)
            len = sqrt(sqr(dx) + sqr(dy)) # float

            fx = SCR_WIDTH + i * fov_factor  # fence x
            # fence_h = SCR_HEIGHT * ff // len # 
            fence_h = SCR_HEIGHT * ff / len * dist_coef # correct fish eye effect - WRONG!!!
            fy = (SCR_HEIGHT / 2) - (fence_h / 2)
            
            pg.draw.rect(display, wc, (fx, fy, fov_factor, fence_h))
            self.draw_background(display, *(fx, fy, fov_factor, fence_h))

    def draw_background(self, display, *rect):
        x, y, w, h = rect
        # sky
        pg.draw.rect(display, cc.Sky, (x, 0, w, y))
        # ground
        gx = x
        gy = (SCR_HEIGHT / 2) + (h / 2)
        gw = w
        gh = SCR_HEIGHT - gy
        pg.draw.rect(display, cc.SaddleBrown, (gx, gy, gw, gh))
        
    def wall_detect(self, player: Player, gmap):
        rw = self.rect_w
        rh = self.rect_h
        for i in range(SCR_WIDTH):
            x = ftoi(player.x + i * cos(angle * d2r))
            y = ftoi(player.y + i * sin(angle * d2r))
            mx = x // self.rect_w # map x coord
            my = y // self.rect_h # and y

            mi = mx + my*MAP_WIDTH
            if gmap[mi] != ' ': return x, y
        
            display.set_at((x, y), cc.Black)

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

