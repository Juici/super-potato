import simplegui

from typing import List

from util import Font, Color
from window import Window, WindowHandler
from levels import Level
from level_items import *

__all__ = ['World']


class World(WindowHandler):
    """
    A game level.
    """

    def __init__(self, window: Window, source: WindowHandler):
        super().__init__(window)
        self.levels = self._init_levels()
        self.level = self.levels[0]
        self.player = Player(self)
        self.window = window
        self.source = source

        self.score_font = Font('monospace', 16, window.hidpi_factor)
        self.score_font_color = Color(255, 255, 255)

    def render(self, canvas: simplegui.Canvas):
        # Shouldn't be None here.
        if self.level is None:
            self.window.handler = self.source
            return

        self.level.render(self, canvas)

    def on_key_down(self, key: int):
        self.player.on_key_down(key)

    def on_key_up(self, key: int):
        self.player.on_key_up(key)

    def _init_levels(self) -> List[Level]:
        levels: List[Level] = []

        level1 = Level(1, (1, 4))

        level1.add_item(Platform(self, (1, 1), (10, 1)))
        level1.add_item(Platform(self, (6, 2), (1, 1)))
        level1.add_item(Platform(self, (14, 2), (4, 1)))
        level1.add_item(Platform(self, (18, 1), (4, 1)))
        level1.add_item(Platform(self, (24, 1), (4, 1)))
        level1.add_item(Platform(self, (29, 2), (2, 1)))
        level1.add_item(Platform(self, (32, 4), (2, 1)))
        level1.add_item(Platform(self, (34, 3), (2, 1)))
        level1.add_item(Platform(self, (40, 5), (1, 2)))
        level1.add_item(Platform(self, (36, 4), (4, 1)))
        level1.add_item(Trap(self, (34, 4), (2, 1)))
        level1.add_item(Finish(self, (40, 7), (1, 2)))

        level2 = Level(2, (1, 4))

        level2.add_item(Platform(self, (0, 1), (10, 1)))
        level2.add_item(Platform(self, (9, 3), (1, 2)))
        level2.add_item(Platform(self, (10, 3), (7, 1)))
        level2.add_item(Platform(self, (20, 3), (7, 1)))
        level2.add_item(Platform(self, (30, 3), (7, 1)))
        level2.add_item(Platform(self, (40, 4), (2, 1)))
        level2.add_item(Platform(self, (44, 4), (2, 1)))
        level2.add_item(Platform(self, (48, 4), (2, 1)))
        level2.add_item(Platform(self, (52, 4), (2, 1)))
        level2.add_item(Platform(self, (56, 4), (2, 1)))
        level2.add_item(Trap(self, (10, 2), (48, 1)))
        level2.add_item(Finish(self, (58, 2), (5, 1)))

        levels.append(level1)
        levels.append(level2)

        return levels
