import simplegui

from typing import List, TYPE_CHECKING, Tuple
from constants import GRID_SIZE, BLOCK_SIZE
from geom import Vector
from level_items import LevelItem

# from constants import LEVEL_BACKGROUND_IMAGE, WINDOW_SIZE
# from util import load_image

# Work around cyclic imports.
if TYPE_CHECKING:
    from world import World

__all__ = ['Level']


class Level(object):
    """
    A game level.
    """

    def __init__(self, level: int, start_pos: Tuple[int, int], scroll: Vector = Vector(0.05, 0)):
        self.level = level
        self.start_pos = Vector(
            start_pos[0] * BLOCK_SIZE,
            (GRID_SIZE[1] - start_pos[1] - 1) * BLOCK_SIZE,
        )

        self.offset = Vector(0, 0)
        self.scroll = scroll

        self.items: List[LevelItem] = []
        self.finished = False

        # Just some initialisation stuff here; less to compute later.
        # self.background_offset = LEVEL_BACKGROUND_STRETCH_X / 2
        # self.background_image = load_image(LEVEL_BACKGROUND_IMAGE)
        # self.bg_size = (self.background_image.get_width(), self.background_image.get_height())
        # self.bg_center = (self.bg_size[0] / 2, self.bg_size[1] / 2)
        # self.half_window_height = WINDOW_SIZE[1] / 2

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

        # Draw background

        # window_center_first = (
        #     -(self.offset.x % LEVEL_BACKGROUND_STRETCH_X) + self.background_offset,
        #     self.half_window_height
        # )
        # window_center_next = (
        #     window_center_first[0] + LEVEL_BACKGROUND_STRETCH_X,
        #     window_center_first[1]
        # )
        # real_size = (LEVEL_BACKGROUND_STRETCH_X, WINDOW_SIZE[1])
        #
        # canvas.draw_image(self.background_image, self.bg_center, self.bg_size, window_center_first,
        #                   real_size)
        # canvas.draw_image(self.background_image, self.bg_center, self.bg_size, window_center_next,
        #                   real_size)

        world.player.score += 1
        canvas.draw_text("SCORE: " + str(world.player.score), (750, 40), 40, "White")

        # Render items
        for item in self.items:
            item.render(canvas)

        # Render player
        world.player.render(canvas)

        # Add the level scroll, mutating the current offset.
        self.offset.add(self.scroll * BLOCK_SIZE)

        # Load next level.
        if self.finished:
            levels = world.levels

            next_level = self.level + 1
            if len(levels) >= next_level:
                world.level = levels[next_level - 1]
            else:
                world.level = None
