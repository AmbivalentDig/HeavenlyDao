import pygame as pg
from lib.config import config as cfg
from lib import type
from lib import event as e

class Text:
	def __init__(self, text, rect, font, fg_color):
		self.text = text
		self.font = font
		self.rect = rect
		self.fg_color = fg_color

	def draw(self, window):
		text = self.font.render(self.text, True, self.fg_color)
		place = text.get_rect(center=self.rect.center)
		window.blit(text, place)


class Widjet:
	def __init__(self, rect, fg_color, bg_color):
		self.rect = rect
		self.fg_color = fg_color
		self.bg_color = bg_color

	def draw(self, window):
		pg.draw.rect(window, rect, bg_color)

class Button(Widjet):
	def __init__(self, function, rect: pg.Rect, text, fg_color, bg_color):
		super().__init__(rect, fg_color, bg_color)
		self.function = function
		self.text = Text(text, self.rect, cfg.Fonts.ButtonFonts, self.fg_color)

	def click(self, event):
		if self.rect.collidepoint(event.pos):
			self.function()

	def draw(self, window):
		super().draw(window)
		self.text.draw(window)

class InputBox(Widjet):
	def __init__(self, rect, inactive_color, bg_color, active_color, text=''):
		super().__init__(rect, inactive_color, bg_color)
		self.active_color = active_color
		self.inactive_color = inactive_color
		self.text = Text(text, self.rect, cfg.Fonts.ButtonFonts, inactive_color)
		self.active_color = False

	def button_down(self, event):
		if self.active:
			if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
			else:
				self.text += event.unicode
	
	def mouse_click(self, event):
		if self.rect.collidepoint(event.pos):
			self.active = not self.active
		else:
			self.active = False
		self.text.fg_color = self.active_color if self.active else self.inactive_color
	
	def draw(self, window):
		super().draw(window)
		self.text.draw(window)

class ImageBox(pg.sprite.Sprite):
	def __init__(self, center_point, bg_color, image):
		pg.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = self.image.get_rect(center=center_point.to_tuple())
		self.update_event = e.event(0)
	
	def update(self):
		self.update_event.invoke()