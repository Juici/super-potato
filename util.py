import pygame
import simplegui

from geom import Vector

__all__ = ['load_image', 'Color', 'Font']


def load_image(path: str) -> simplegui.Image:
    """
    Loads an image from the path.
    """
    if path.startswith('http'):
        return simplegui.load_image(path)
    else:
        # noinspection PyProtectedMember
        return simplegui._load_local_image(path)


class Color(object):

    def __init__(self, r: int, g: int, b: int, a: float = 1.0):
        self.r = max(0, min(r, 255))
        self.g = max(0, min(g, 255))
        self.b = max(0, min(b, 255))
        self.a = max(0.0, min(a, 1.0))

    def __str__(self):
        return 'rgba(%d,%d,%d,%d)' % (self.r, self.g, self.b, self.a)


class Font(object):

    def __init__(self, face: str, size: int, hidpi_factor: float = 1.0):
        self.face = face
        self.size = size
        self.hidpi_factor = hidpi_factor

    def get_face(self):
        return self.face

    def get_size(self):
        return self.size * self.hidpi_factor

    def get_raw_size(self):
        return self.size

    # noinspection PyProtectedMember
    def get_text_bounds(self, text: str) -> Vector:
        """
        Returns to bounds of the text in this font.
        """
        font_name = self.face
        if font_name in simplegui._SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME:
            font_name = simplegui._SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME[font_name]
        bounds = pygame.font.SysFont(font_name, int(self.size * self.hidpi_factor)).size(text)
        return Vector(bounds[0], bounds[1])
