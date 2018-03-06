from modules import pygame, simplegui
from vector import Vector


class Color(object):

    def __init__(self, r: int, g: int, b: int):
        self.r = max(0, min(r, 255))
        self.g = max(0, min(g, 255))
        self.b = max(0, min(b, 255))

    def __add__(self, k: float):
        r = int(self.r + k)
        g = int(self.g + k)
        b = int(self.b + k)
        return Color(r, g, b)

    def __sub__(self, k: float):
        self.__add__(-k)

    def __mul__(self, k: float):
        r = int(self.r * k)
        g = int(self.g * k)
        b = int(self.b * k)
        return Color(r, g, b)

    def __rmul__(self, k: float):
        self.__mul__(k)

    def __truediv__(self, k: float):
        self.__mul__(1.0 / k)

    def __str__(self):
        return 'rgb(' + str(self.r) + ',' + str(self.g) + ',' + str(self.b) + ')'


class Font(object):

    def __init__(self, face: str, size: int):
        self.face = face
        self.size = size

    # noinspection PyProtectedMember
    def get_text_bounds(self, text: str, hidpi_factor: float = 1.0) -> Vector:
        """
        Returns to bounds of the text in this font.
        """
        font_name = self.face
        if self.face in simplegui._SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME:
            font_name = simplegui._SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME[font_name]
        bounds = pygame.font.SysFont(font_name, int(self.size * hidpi_factor)).size(text)
        return Vector(bounds[0], bounds[1])


class Polygon(object):
    """
    Represents a bounding area in the form of a polygon.
    """

    def __init__(self, *points: Vector):
        """
        Constructs a polygon from a list of Vectors.
        """
        self.points = list(points)

    def __getitem__(self, item: int) -> Vector:
        return self.points[item]

    def __setitem__(self, key: int, value: Vector):
        self.points[key] = value

    def __len__(self):
        return len(self.points)

    def is_inside(self, p: Vector) -> bool:
        """
        Returns `true` if the vector `p` is inside the polygon.
        """
        n = len(self.points)

        i = 0
        j = n - 1
        c = False

        while i < n:
            if ((self.points[i].y > p.y) != (self.points[j].y > p.y)) and (
                    p.x < (self.points[j].x - self.points[i].x) * (p.y - self.points[i].y) / (
                    self.points[j].y - self.points[i].y) + self.points[i].x):
                c = not c

            j = i
            i += 1

        return c
