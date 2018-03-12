from modules import simplegui
from constants import *
from vector import Vector
from window import Window, WindowHandler
from character import Character


class GameView(WindowHandler):
    """
    A game level.
    """

    def __init__(self, window: Window):
        super().__init__(window)
        self.offset = 0

        self.add_child(Character(window, Vector(100, 0), Vector(50, 100)))

    def render(self, canvas: simplegui.Canvas):
        super().render(canvas)

        self.offset += LEVEL_X_PUSH
