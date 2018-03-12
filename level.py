from modules import simplegui
from constants import *
from vector import Vector
from window import Window, WindowHandler
from level_items import Character, Platform, Trap, Finish


class GameView(WindowHandler):
    """
    A game level.
    """

    def __init__(self, window: Window, next_level: 'Level'):
        super().__init__(window)
        self.next_level = next_level
        self.window = window
        self.offset = 0

    def win(self):
        self.window.handler = self.next_level

    def render(self, canvas: simplegui.Canvas):
        super().render(canvas)

        self.offset += LEVEL_X_PUSH
