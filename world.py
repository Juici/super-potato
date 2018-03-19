import simplegui

from typing import List
from window import Window, WindowHandler
from levels import Level
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
        if self.level is None:
            pass  # TODO: finish logic

        self.level.render(self, canvas)

    def on_key_down(self, key: int):
        self.player.on_key_down(key)

    def on_key_up(self, key: int):
        self.player.on_key_up(key)

    def _init_levels(self) -> List[Level]:
        levels: List[Level] = []

        level1 = Level(1, (1, 4))
        level1.add_item(Platform(self, (1, 1), (10, 1)))
        level1.add_item(Platform(self, (14, 2), (4, 1)))
        level1.add_item(Platform(self, (6, 2), (1, 1)))
        levels.append(level1)

        return levels
