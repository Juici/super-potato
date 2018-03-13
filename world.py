from typing import List
from window import Window, WindowHandler
from levels import Level

import simplegui

__all__ = ['World']


class World(WindowHandler):
    """
    A game level.
    """

    def __init__(self, window: Window, levels: List[Level]):
        super().__init__(window)
        self.level = levels[0]

    def render(self, canvas: simplegui.Canvas):
        # Shouldn't be None here.
        self.level.render(self, canvas)

        if self.level is None:
            pass  # TODO: finish logic
