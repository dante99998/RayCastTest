from math import pi

FPS = 60

d2r = pi / 180 # degree to radians 
r2d = 180 / pi # radians to degree
fov = 60 # field of view

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (75, 192, 71)
RED   = (216, 30, 30)

DIR_RIGHT = (5, 0)
DIR_LEFT  = (-5, 0)
DIR_UP    = (0, -5)
DIR_DOWN  = (0, 5)

SCR_WIDTH  = 512
SCR_HEIGHT = 512
MAP_HIEGHT = 16
MAP_WIDTH  = 16

fov_factor = int(512 / fov)
VIEW_WIDTH = 512 - fov_factor
ALL_SCR_WIDTH  = SCR_WIDTH + VIEW_WIDTH
ALL_SCR_HEIGHT = SCR_HEIGHT


SCR_SIZE = (ALL_SCR_WIDTH, ALL_SCR_HEIGHT)
BLOCK_SIZE = (10, 10)
START_POS = (0, 10)

class CommonColors:
    White	    = (255, 255, 255)  #FFFFFF	rgb(255, 255, 255)
    Silver	    = (192, 192, 192)  #C0C0C0	rgb(192, 192, 192)
    Gray	    = (128, 128, 128)  #808080	rgb(128, 128, 128)
    Black	    = (0, 0, 0)        #000000	rgb(0, 0, 0)
    Red	        = (255, 0, 0)      #FF0000	rgb(255, 0, 0)
    Maroon	    = (128, 0, 0)      #800000	rgb(128, 0, 0)
    Yellow	    = (255, 255, 0)    #FFFF00	rgb(255, 255, 0)
    Olive	    = (128, 128, 0)    #808000	rgb(128, 128, 0)
    Lime	    = (0, 255, 0)      #00FF00	rgb(0, 255, 0)
    Green	    = (0, 128, 0)      #008000	rgb(0, 128, 0)
    Aqua	    = (0, 255, 255)    #00FFFF	rgb(0, 255, 255)
    Teal	    = (0, 128, 128)    #008080	rgb(0, 128, 128)
    Blue	    = (0, 0, 255)      #0000FF	rgb(0, 0, 255)
    Navy	    = (0, 0, 128)      #000080	rgb(0, 0, 128)
    Fuchsia     = (255, 0, 255)    #FF00FF	rgb(255, 0, 255)
    Purple	    = (128, 0, 128)    #800080	rgb(128, 0, 128)
    Sky         = (135,206,235)    #87CEEB  rgb(135,206,235)
    SaddleBrown = (139,69,19)	   #8B4513	rgb(139,69,19)
    SandyBrown	= (244,164,96)     #F4A460	rgb(244,164,96)