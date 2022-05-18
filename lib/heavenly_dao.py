import pygame as pg
from lib.type import *
from lib import controls
import sys

class Game:
    def __init__(self, resoulution):
        self.root = pg.display.set_mode(resoulution.to_tuple())
        pg.display.set_caption('Application')
        self.keyboardHadler = controls.KeyboardHadler() 
        self.mouseHandler = controls.MouseHandler()
        self.sysMsgHandler = controls.SystemMsgHandler()
        self.sysMsgHandler.exit.subscribe(self.end_game)
        self.run = True

    def start(self):
        while self.run:
            self.gameloop()            
        return pg.quit()

    def gameloop(self):
        event_list = pg.event.get()
        self.keyboardHadler.handle(event_list)
        self.mouseHandler.handle(event_list) 
        self.sysMsgHandler.handle(event_list)
        self.root.fill(pg.colordict.THECOLORS['black'])
        pg.display.update()

    def end_game(self):
        self.run = False
