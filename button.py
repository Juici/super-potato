from typing import Tuple

from util import Color, simplegui
from window import Renderable
from pygame import mouse, font
from math import floor

# Taken directly from simplegui source
_SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME = {
    'monospace': 'courier,couriernew',
    'sans-serif': 'arial,tahoma',
    'serif': 'timesnewroman,garamond,georgia'}

# May be best put these methods in a different file

def lerp_color(col_a: Color, col_b: Color, factor: float):
    # Apparently you can't perform numeric operations on Color objects ¯\_(ツ)_/¯
    inverse = 1.0 - factor

    final_r = inverse * col_a.r + factor * col_b.r
    final_g = inverse * col_a.g + factor * col_b.g
    final_b = inverse * col_a.b + factor * col_b.b

    return Color(final_r, final_g, final_b)

def floor_color(col: Color):
    return Color(floor(col.r), floor(col.g), floor(col.b))

def get_colour_str(col: Color):
    col = floor_color(col)
    return "rgb(" + str(col.r) + "," + str(col.g) + "," + str(col.b) + ")"

class Button(Renderable):

    def __init__(self, caption: str, font_size: int, font_face: str,
        pos: Tuple[int, int], size: Tuple[int, int], border_size: int,
        bg: Color, fg: Color, bg_over: Color, fg_over: Color, lerp_factor: float):

        # Get string bounds
        font_bounds = font.SysFont(_SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME[font_face], font_size).size(caption)

        # General attributes
        self.caption = caption
        self.size = size
        self.pos = pos
        self.border_size = border_size
        self.lerp_factor = lerp_factor
        self.font_size = font_size
        self.font_face = font_face
        self.center = (
            self.pos[0] + self.size[0] / 2 - font_bounds[0] / 2,
            self.pos[1] + self.size[1] / 2 + font_bounds[1] / 4
        )

        # Initial colours
        self.bg = bg
        self.fg = fg
        self.bg_over = bg_over
        self.fg_over = fg_over

        # Current and target colours
        self.bg_color = bg
        self.fg_color = fg
        self.bg_target = bg
        self.fg_target = fg

        # Get corners
        self.vertices = (
            self.pos,
            (self.pos[0] + self.size[0], self.pos[1]),
            (self.pos[0] + self.size[0], self.pos[1] + self.size[1]),
            (self.pos[0], self.pos[1] + self.size[1])
        )

    def get_center(self) -> Tuple[int, int]:
        return self.center

    def render(self, canvas: simplegui.Canvas):
        x0 = self.vertices[0][0];
        y0 = self.vertices[0][1];
        x1 = self.vertices[2][0];
        y1 = self.vertices[2][1];

        mouse_x, mouse_y = mouse.get_pos()

        # Check if mouse is inside button boundaries
        if (mouse_x >= x0 and mouse_x <= x1) and (mouse_y >= y0 and mouse_y <= y1):
            self.fg_target = self.fg_over
            self.bg_target = self.bg_over
        else:
            self.fg_target = self.fg
            self.bg_target = self.bg

        # Linearly interpolate colours for smooth effect
        self.bg_color = lerp_color(self.bg_color, self.bg_target, self.lerp_factor)
        self.fg_color = lerp_color(self.fg_color, self.fg_target, self.lerp_factor)

        center_x, center_y = self.get_center()
        canvas.draw_polygon(self.vertices, self.border_size, get_colour_str(self.bg_color), get_colour_str(self.bg_color))
        canvas.draw_text(self.caption, (center_x, center_y), self.font_size, get_colour_str(self.fg_color), self.font_face)