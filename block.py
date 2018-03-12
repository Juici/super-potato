from util import simplegui, Color, Polygon
from constants import *
from vector import Vector
from window import Renderable, Window


class Block(Renderable):

    def __init__(self, window: Window, position: Vector, size: Vector, color: Color):
        super().__init__(window)

        self.position = position
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

    def get_bounds(self) -> Polygon:
        return Polygon(*self.vertices)

    def update_vertices(self):
        for index in range(4):
            self.vertex_positions[index] = (self.vertices[index] + self.position).into_tuple()

    def get_size(self) -> Vector:
        return self.size

    def get_next_pos(self) -> Vector:
        return self.position

    def render(self, canvas: simplegui.Canvas):
        self.update_vertices()
        self.position -= Vector(LEVEL_X_PUSH, 0)

        canvas.draw_polygon(self.vertex_positions, 1, str(self.color))
