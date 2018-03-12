from typing import Callable

from constants import HIDPI_FACTOR
from modules import pygame, simplegui
from util import Color, Font, Polygon
from vector import Vector
from window import Renderable, Window


class Button(Renderable):

    def __init__(self, window: Window, text: str, pos: Vector, size: Vector = Vector(150, 50),
                 bg: Color = Color(200, 200, 200), fg: Color = Color(20, 20, 20),
                 bg_over: Color = Color(220, 220, 220), fg_over: Color = Color(20, 20, 20),
                 border_size: int = 0, font: Font = Font('sans-serif', 15, HIDPI_FACTOR)):
        super().__init__(window)
        self._click_handler = None

        self.text = text
        self.pos = pos
        self.size = size

        # Initial colours
        self.bg = bg
        self.fg = fg
        self.bg_over = bg_over
        self.fg_over = fg_over

        # Extra
        self.font = font
        self.border_size = border_size

        # Center
        self.center = (
            self.pos[0] + self.size[0] / 2,
            self.pos[1] + self.size[1] / 2
        )

        # Get corners
        self.bounds = Polygon(
            Vector(pos.x, pos.y),
            Vector(pos.x + size.x, pos.y),
            Vector(pos.x + size.x, pos.y + size.y),
            Vector(pos.x, pos.y + size.y)
        )

    def get_bounds(self) -> Polygon:
        return self.bounds

    def render(self, canvas: simplegui.Canvas):
        mouse = pygame.mouse.get_pos()
        mouse = Vector(mouse[0], mouse[1])

        if self.get_bounds().contains(mouse):
            fg = self.fg_over
            bg = self.bg_over
        else:
            fg = self.fg
            bg = self.bg

        points = [(v.x, v.y) for v in self.bounds]
        canvas.draw_polygon(points, self.border_size, str(bg), str(bg))

        # Center text on button
        font_bounds = self.font.get_text_bounds(self.text)
        text_pos = (
            self.center[0] - font_bounds.x / 2,
            self.center[1] + font_bounds.y / 4,
        )

        canvas.draw_text(self.text, text_pos, self.font.get_size(), str(fg), self.font.get_face())

    def on_click(self, pos: Vector):
        if self._click_handler is not None:
            self._click_handler(self, pos)

    def set_click_handler(self, handler: Callable[['Button', Vector], None]):
        self._click_handler = handler
