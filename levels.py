from typing import List, TYPE_CHECKING
from geom import Vector
from level_items import LevelItem

# Work around cyclic imports.
if TYPE_CHECKING:
    from world import World

import simplegui

__all__ = ['Level', 'LEVELS']


class Level(object):
    """
    A game level.
    """

    def __init__(self, level: int, start_pos: Vector, scroll: Vector = Vector(1, 0)):
        self.level = level
        self.start_pos = start_pos

        self.offset = Vector(0, 0)
        self.scroll = scroll

        self.items: List[LevelItem] = []
        self.finished = False

    def add_item(self, item: LevelItem):
        """
        Adds the item to the level.
        """
        self.items.append(item)

    def finish(self):
        """
        Finishes the level.
        """
        self.finished = True

    def render(self, world: 'World', canvas: simplegui.Canvas):
        """
        Called on every game tick to render the level.
        """
        for item in self.items:
            item.render(canvas)

        # Add the level scroll, mutating the current offset.
        self.offset.add(self.scroll)

        # Load next level.
        if self.finished:
            next_level = self.level + 1
            if len(LEVELS) >= next_level:
                world.level = LEVELS[next_level - 1]
            else:
                world.level = None


LEVELS: List[Level] = []


def _init_levels():
    level1 = Level(1, Vector(100, 100))
    LEVELS.append(level1)


_init_levels()

del _init_levels
