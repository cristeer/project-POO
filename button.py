import pygame

class Button():
	
	def __init__(self, pos, text_input, text_font, base_color, hovering_color):
		self.__x_pos = pos[0]
		self.__y_pos = pos[1]
		self.__font = text_font
		self.__base_color = base_color
		self.__hovering_color = hovering_color
		self.__text_input = text_input
		self.__text = self.font.render(self.text_input, True, self.base_color)
		self.__rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
	
	# Setters e Getters
	@property
	def x_pos(self):
		return self.__x_pos
	
	@x_pos.setter
	def x_pos(self, value):
		self.__x_pos = value

	@property
	def y_pos(self):
		return self.__y_pos
	
	@y_pos.setter
	def y_pos(self, value):
		self.__y_pos = value
		
	@property
	def font(self):
		return self.__font
	
	@font.setter
	def font(self, value):
		self.__font = value

	@property
	def base_color(self):
		return self.__base_color
	
	@base_color.setter
	def base_color(self, value):
		self.__base_color = value
		
	@property
	def hovering_color(self):
		return self.__hovering_color
	
	@hovering_color.setter
	def hovering_color(self, value):
		self.__hovering_color = value
		
	@property
	def text_input(self):
		return self.__text_input
	
	@text_input.setter
	def text_input(self, value):
		self.__text_input = value

	@property
	def text(self):
		return self.__text
	
	@text.setter
	def text(self, value):
		self.__text = value

	@property
	def rect(self):
		return self.__rect
	
	@rect.setter
	def rect(self, value):
		self.__rect = value

	def update(self, screen):
		screen.blit(self.text, self.rect)

	def checkForInput(self, position):
		return self.rect.collidepoint(position)

	def changeColor(self, position):
		if self.rect.collidepoint(position):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)