import math
import simplegui

from typing import TYPE_CHECKING, Tuple
from constants import PLAYER_SIZE, PLAYER_VELOCITY, ACCEL_GRAVITY, BLOCK_SIZE, GRID_SIZE, Key
from util import Color
from geom import Vector, BoundingBox
from window import Renderable

# Work around cyclic imports.
if TYPE_CHECKING:
    from world import World

__all__ = ['LevelItem', 'Rect', 'Trap', 'Finish', 'Platform', 'Player']


class LevelItem(Renderable):

    def __init__(self, world: 'World'):
        super().__init__(world.window)
        self.world = world

    def get_bounds(self) -> BoundingBox:
        raise NotImplementedError

    def on_collide(self, player: 'Player'):
        pass

    def collides_with(self, box: BoundingBox) -> bool:
        return self.get_bounds().collides(box)


class Rect(LevelItem):
    """
    A generic rectangle to be drawn on the canvas.
    *Should be extended, not created directly.*
    """

    def __init__(self, world: 'World'):
        super().__init__(world)

    def get_pos(self) -> Tuple[int, int]:
        raise NotImplementedError

    def get_size(self) -> Tuple[int, int]:
        return 1, 1

    def get_border_width(self) -> int:
        """
        Returns the border width.
        """
        return 1

    def get_border_color(self) -> Color:
        """
        Returns the border color of the rectangle.
        """
        return Color(200, 200, 200)

    def get_fill_color(self) -> Color:
        """
        Returns the fill color of the rectangle.
        """
        return Color(0, 0, 0)

    def render(self, canvas: simplegui.Canvas):
        bounds = self.get_bounds()

        point_list = bounds.into_point_list()
        border_width = self.get_border_width()
        border_color = str(self.get_border_color())
        fill_color = str(self.get_fill_color())

        canvas.draw_polygon(point_list, border_width, border_color, fill_color)

    def get_bounds(self) -> BoundingBox:
        dpi_factor = self.window.hidpi_factor

        pos = self.get_pos()
        size = self.get_size()

        pos = Vector(
            pos[0] * BLOCK_SIZE,
            (GRID_SIZE[1] - pos[1] - 1) * BLOCK_SIZE,
        )
        size = Vector(
            size[0] * BLOCK_SIZE,
            size[1] * BLOCK_SIZE,
        )

        pos = (pos - self.world.level.offset) * dpi_factor
        size = size * dpi_factor

        return BoundingBox(pos, pos + size)


class Trap(Rect):

    def __init__(self, world: 'World', pos: Tuple[int, int], size: Tuple[int, int]):
        super().__init__(world)

        self.pos = pos
        self.size = size
        self.color = Color(150, 40, 40)

    def get_pos(self) -> Tuple[int, int]:
        return self.pos

    def get_size(self) -> Tuple[int, int]:
        return self.size

    def get_border_color(self) -> Color:
        return self.color

    def on_collide(self, player: 'Player'):
        pass  # TODO: death logic


class Finish(Rect):

    def __init__(self, world: 'World', pos: Vector, size: Vector):
        super().__init__(world)

        self.pos = pos
        self.size = size
        self.color = Color(40, 200, 40)

    def get_pos(self) -> Vector:
        return self.pos

    def get_size(self) -> Vector:
        return self.size

    def get_border_color(self) -> Color:
        return self.color

    def on_collide(self, player: 'Player'):
        pass  # TODO: finish logic


class Platform(Rect):

    def __init__(self, world: 'World', pos: Tuple[int, int], size: Tuple[int, int],
                 color: Color = Color(200, 200, 200), fill: bool = False):
        super().__init__(world)

        self.pos = pos
        self.size = size
        self.color = color
        self.fill = fill

    def get_pos(self) -> Tuple[int, int]:
        return self.pos

    def get_size(self) -> Tuple[int, int]:
        return self.size

    def get_border_color(self) -> Color:
        return self.color

    def get_fill_color(self) -> Color:
        if self.fill:
            return self.color
        return super().get_fill_color()

    def on_collide(self, player: 'Player'):
        pass  # TODO: solid collision


class Player(Renderable):

    def __init__(self, world: 'World'):
        super().__init__(world.window)
        self.world = world

        self.size = Vector(*PLAYER_SIZE)

        self.pos = world.level.start_pos
        self.last_pos = self.pos.copy()
        self.vel = Vector(0, 0)
        self.accel = Vector(0, 0)

        self.on_ground = False
        self.jumping = False
        self.moving_x = False

        self.colliding_with = None

        self.score = 0

    def jump(self):
        self.vel.y = PLAYER_VELOCITY[1]
        self.accel.y = ACCEL_GRAVITY[1]

    def get_bounds(self) -> BoundingBox:
        dpi_factor = self.window.hidpi_factor

        pos = self.pos * dpi_factor
        size = self.size * dpi_factor

        return BoundingBox(pos, pos + size)

    def on_key_down(self, key: int):
        if key == Key.SPACE:
            self.jumping = True  # Allow holding jump button.

            if self.on_ground:
                self.jump()

        elif key == Key.KEY_A:
            self.vel.x = -PLAYER_VELOCITY[0]

        elif key == Key.KEY_D:
            self.vel.x = PLAYER_VELOCITY[0]

    def on_key_up(self, key: int):
        if key == Key.SPACE:
            self.jumping = False

        elif key == Key.KEY_A:
            if self.vel.x < 0:
                self.vel.x = 0

        elif key == Key.KEY_D:
            if self.vel.x > 0:
                self.vel.x = 0

    def render(self, canvas: simplegui.Canvas):
        bounds = self.get_bounds()

        # Draw player.
        point_list = bounds.into_point_list()
        color = Color(120, 120, 200)

        canvas.draw_polygon(point_list, 1, str(color), str(color))  # TODO: sprite?

        # Update position.
        self.last_pos = self.pos.copy()
        self.pos.add(self.vel)
        self.vel.add(self.accel)

        if abs(self.vel.x) > PLAYER_VELOCITY[0]:
            self.vel.x = math.copysign(PLAYER_VELOCITY[0], self.vel.x)

        # Check collisions position.
        did_collide = False
        for item in self.world.level.items:
            if item.collides_with(bounds):
                item.on_collide(self)
                if did_collide == False:
                    self.colliding_with = item
                    did_collide = True

        # Do gravity
        if did_collide:
            hit_pos = self.colliding_with.get_bounds().min
            self.accel.y = 0
            self.vel.y = 0
            self.pos = Vector(self.pos.x, hit_pos.y - self.size.y)
        else:
            self.accel.y = -ACCEL_GRAVITY
