import simplegui

from typing import List
from window import Window, WindowHandler
from levels import Level
from geom import Vector
from level_items import *

__all__ = ['World']


class World(WindowHandler):
    """
    A game level.
    """

    def __init__(self, window: Window):
        super().__init__(window)
        self.levels = self._init_levels()
        self.level = self.levels[0]
        self.player = Player(self)
        self.window = window

    def render(self, canvas: simplegui.Canvas):
        # Shouldn't be None here.
        self.level.render(self, canvas)

        if self.level is None:
            pass  # TODO: finish logic

    def on_key_down(self, key: int):
        self.player.on_key_down(key)

    def on_key_up(self, key: int):
        self.player.on_key_up(key)
    
    def _init_levels(self) -> List[Level]:
        levels: List[Level] = []

        level1 = Level(1, Vector(100, 100))
        levels.append(level1)


        return levels
