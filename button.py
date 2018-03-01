from typing import Tuple

from util import Color, simplegui
from window import Renderable


class Button(Renderable):

    def __init__(self, caption: str, pos: Tuple[int, int], size: Tuple[int, int],
                 bg: Color, fg: Color):
        self.caption = caption
        self.size = size
        self.pos = pos
        self.bg = bg
        self.fg = fg

        self.vertices = (
            self.pos,
            (self.pos[0] + self.size[0], self.pos[1]),
            (self.pos[0] + self.size[0], self.pos[1] + self.size[1]),
            (self.pos[0], self.pos[1] + self.size[1])
        )

    def get_center(self) -> Tuple[int, int]:
        return self.pos[0] + self.size[0], self.pos[1] + self.size[1]

    def render(self, canvas: simplegui.Canvas):
        canvas.draw_polygon(self.vertices, 1, str(self.bg), str(self.bg))
