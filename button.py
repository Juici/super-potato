from util import simplegui
from vector import Vector

class Button:

	def __init__(self, caption, size, position, back_colour, over_colour):

		self.caption = caption
		self.size = size
		self.position = position
		self.back_colour = back_colour
		self.over_colour = over_colour
		self.update_vertices()

	def update_centre():

		self.centre = self.position + self.size / 2

	def update_vertices():

		self.vertices = [
			self.position, # Top-left
			self.position + Vector(1, 0) * self.size,
			self.position + Vector(0, 1) * self.size,
			self.position + Vector(1, 1) * self.size
		]

	def object_render(canvas):

		self.update_centre()
		self.draw_centre()
		self.draw_polygon(self.vertices, 1, self.back_colour, self.back_colour)



