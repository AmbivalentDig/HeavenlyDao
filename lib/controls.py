from lib import event as e
import pygame as pg
from lib.config import config as cfg
from multipledispatch import dispatch

class EventHandler:
    def __init__(self):
        pass
        
    def _handle(self, event):
        pass

    def handle(self, event_list: list):
        for event in event_list:
            self._handle(event)

        
class KeyboardHadler(EventHandler):
    def __init__(self):
        self.presskey = e.Event(0)
        self.foward = e.Event(0)
        self.backward = e.Event(0)
        self.right = e.Event(0)
        self.left = e.Event(0)  
        self.esc = e.Event(0)
        self.enter = e.Event(0)

    def _handle(self, event):
        if event.type == pg.KEYDOWN:
            key = event.key
            _event = None
            if key == cfg.ControlKey.Foward:
                _event = self.foward
            elif key == cfg.ControlKey.Backward:
                _event = self.backward
            elif key == cfg.ControlKey.Left:
                _event = self.left
            elif key == cfg.ControlKey.Right:
                _event = self.right
            elif key == cfg.ControlKey.Enter:
                _event = self.enter
            elif key == cfg.ControlKey.Esc:
                _event = self.esc
            if isinstance(_event, e.Event):
                _event.invoke()

class MouseHandler(EventHandler):
    def __init__(self):
        self.left_click = e.Event(1)
        self.right_click = e.Event(1)
        self.middle_click = e.Event(1)

    def _handle(self, event: pg.event.Event):
        if event.type == pg.MOUSEBUTTONDOWN:
            left, middle, right = pg.mouse.get_pressed()
            _event = None
            if left:
                _event = self.left_click
            elif middle:
                _event = self.middle_click
            elif right:
                _event = self.right_click
            _event.invoke(event)

class SystemMsgHandler(EventHandler):
    def __init__(self):
        self.exit = e.Event(0)
    
    def _handle(self, event: pg.event.Event):
        if event.type == pg.QUIT:
            self.exit.invoke()
