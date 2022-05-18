import pygame as pg

class Widjet:
	def __init__(self, rect, fg_color, bg_color):
		self.rect = rect
		self.fg_color = fg_color
		self.bg_color = bg_color

	def draw(self, window):
		pg.draw.rect(window, rect, bg_color)
