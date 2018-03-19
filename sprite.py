import util
import simplegui

from typing import Tuple, Optional
from geom import Vector


class Sprite(object):
    """
    Represents a sprite to be drawn on the canvas.
    """

    def __init__(self, image: str, cols: int = 1, rows: int = 1):
        """
        Creates a sprite with the specified image and number of cols and rows.
        """
        self.image = util.load_image(image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.cols = cols
        self.rows = rows

        self.sprite_size = (self.width // cols, self.height // rows)
        self.sprite_center = (self.sprite_size[0] / 2, self.sprite_size[1] / 2)

    def draw(self, canvas: simplegui.Canvas, pos: Vector, size: Optional[Vector] = None,
             index: Tuple[int, int] = (0, 0)):
        """
        Draw the sprite on the canvas.
        """
        source_center = [self.sprite_size[i] * index[i] + self.sprite_center[i] for i in [0, 1]]
        if size is not None:
            size = size.into_tuple()
        else:
            size = self.sprite_size
        canvas.draw_image(self.image, source_center, self.sprite_size, pos.into_tuple(), size)
