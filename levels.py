import simplegui

from typing import List, TYPE_CHECKING
from geom import Vector
from level_items import LevelItem
from constants import LEVEL_BACKGROUND_IMAGE, LEVEL_BACKGROUND_DIMS, LEVEL_BACKGROUND_STRETCH_X, WINDOW_SIZE
from util import load_image

# Work around cyclic imports.
if TYPE_CHECKING:
    from world import World

__all__ = ['Level']


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

        self.parallax = load_image(LEVEL_BACKGROUND_IMAGE)

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

        # Draw parallax background, todo
        bg_size = (self.parallax.get_width(), self.parallax.get_height())
        bg_center = (bg_size[0] / 2, bg_size[1] / 2)
        window_center = (-self.offset.x, WINDOW_SIZE[1] / 2)
        canvas.draw_image(self.parallax, bg_center, bg_size, window_center, (LEVEL_BACKGROUND_STRETCH_X, WINDOW_SIZE[1]))

        # Render items
        for item in self.items:
            item.render(canvas)

        # Render player
        world.player.render(canvas)

        # Add the level scroll, mutating the current offset.
        self.offset.add(self.scroll)

        # Load next level.
        if self.finished:
            levels = self.world.levels

            next_level = self.level + 1
            if len(levels) >= next_level:
                world.level = levels[next_level - 1]
            else:
                world.level = None
