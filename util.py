try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

try:
    import pygame
except ImportError:
    pygame = None


class Color(object):

    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b


def __str__(self):
    return 'rgb(' + str(self.r) + ',' + str(self.g) + ',' + str(self.b) + ')'
