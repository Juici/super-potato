from util import simplegui, Color
from constants import *
from vector import Vector
from window import Renderable, Window
from level import Level
#from sprite import Sprite

class Block(Renderable):

    def __init__(self, position: Vector, size: Vector, color: Color, window: Window, level: Level):
        self.position = position
        self.last_position = position + Vector(1, 0)
        self.size = size
        self.color = color
        self.window_size = window.get_size()
        self.vertices = [
            Vector(0, 0),
            Vector(size.x, 0),
            Vector(size.x, size.y),
            Vector(0, size.y)
        ]
        self.vertex_positions = [
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0)
        ]
        level.add_renderable(self)

    def update_vertices(self):
        if self.position != self.last_position:
            self.last_position = self.position
            for index in range(4):
                self.vertex_positions[index] = (self.vertices[index] + self.position).into_tuple()

    def get_size(self) -> Vector:
        return self.size

    def get_next_pos(self) -> Vector:
        return self.position

    def render(self, canvas: simplegui.Canvas, renderables: Renderable):
        self.update_vertices()
        canvas.draw_polygon(self.vertex_positions, 1, str(self.color))
