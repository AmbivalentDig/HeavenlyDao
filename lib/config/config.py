from lib.type import * 
import pygame as pg

resolution = Point(900, 900)

class ControlKey:
    Foward = pg.K_w
    Backward = pg.K_s
    Left = pg.K_a
    Right = pg.K_d
    Enter = pg.K_KP_ENTER
    Esc = pg.K_ESCAPE