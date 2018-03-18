import simplegui

from typing import TYPE_CHECKING
from constants import PLAYER_SIZE, PLAYER_VELOCITY, PLAYER_ACCELERATION, PLAYER_VELOCITY_DIVISOR, LEVEL_BLOCK_SCALE_PX, Key
from util import Color
from geom import Vector, Polygon, BoundingBox
from window import Renderable
from math import floor

# Work around cyclic imports.
if TYPE_CHECKING:
    from world import World

__all__ = ['LevelItem', 'Rect', 'Trap', 'Finish', 'Platform', 'Player']

def get_scaled_space(vec: Vector) -> Vector:
    return Vector(floor(vec.x * LEVEL_BLOCK_SCALE_PX[0]),
                  floor(vec.y * LEVEL_BLOCK_SCALE_PX[1]))


class LevelItem(Renderable):

    def __init__(self, world: 'World'):
        super().__init__(world.window)
        self.world = world
        self.bounds = BoundingBox(Vector(0, 0), Vector(0, 0))

    def get_bounds(self) -> BoundingBox:
        return self.bounds

    def on_collide(self, player: 'Player'):
        pass

    def collides_with(self, other: BoundingBox) -> bool:
        return self.get_bounds().collides(other)


class Rect(LevelItem):
    """
    A generic rectangle to be drawn on the canvas.
    *Should be extended, not created directly.*
    """

    def __init__(self, world: 'World'):
        super().__init__(world)

    def get_pos(self) -> Vector:
        """
        Returns the position of the rectangle in the world.
        """
        raise NotImplementedError

    def get_size(self) -> Vector:
        """
        Returns the size of the rectangle.
        """
        raise NotImplementedError

    def get_render_pos(self) -> Vector:
        """
        Returns the render position of the rectangle.
        """
        pos = self.get_pos()
        offset = self.world.level.offset

        return pos - offset

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
        self.bounds.min = self.get_pos()
        self.bounds.max = self.bounds.min + self.get_size()

        point_list = self.bounds.into_point_list()
        border_width = self.get_border_width()
        border_color = str(self.get_border_color())
        fill_color = str(self.get_fill_color())

        canvas.draw_polygon(point_list, border_width, border_color, fill_color)

    def get_bounds(self) -> BoundingBox:
        return self.bounds


class Trap(Rect):

    def __init__(self, world: 'World', pos: Vector, size: Vector):
        super().__init__(world)

        self.pos = get_scaled_space(pos)
        self.size = get_scaled_space(size)
        self.color = Color(150, 40, 40)

    def get_pos(self) -> Vector:
        return self.pos

    def get_size(self) -> Vector:
        return self.size

    def get_border_color(self) -> Color:
        return self.color

    def on_collide(self, player: 'Player'):
        pass  # TODO: death logic


class Finish(Rect):

    def __init__(self, world: 'World', pos: Vector, size: Vector):
        super().__init__(world)

        self.pos = get_scaled_space(pos)
        self.size = get_scaled_space(size)
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

    def __init__(self, world: 'World', pos: Vector, size: Vector,
                 color: Color = Color(200, 200, 200), fill: bool = False):
        super().__init__(world)

        self.pos = get_scaled_space(pos)
        self.size = get_scaled_space(size)
        self.color = color
        self.fill = fill

    def get_pos(self) -> Vector:
        return self.pos

    def get_size(self) -> Vector:
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
        self.bounds = BoundingBox(Vector(0, 0), self.size)

    def jump(self):
        self.vel.y = PLAYER_VELOCITY[1]
        self.accel.y = PLAYER_ACCELERATION[1]

    def get_pos(self):
        return self.pos

    def get_size(self):
        return self.size

    def get_bounds(self) -> BoundingBox:
        return self.bounds

    def on_key_down(self, key: int):
        if key == Key.SPACE:
            self.jumping = True  # Allow holding jump button.

            if self.on_ground:
                self.jump()

        elif key == Key.KEY_A:
            self.accel.x = -PLAYER_ACCELERATION[0]

        elif key == Key.KEY_D:
            self.accel.x = PLAYER_ACCELERATION[0]

    def on_key_up(self, key: Key):
        if key == Key.SPACE:
            self.jumping = False

        elif key == Key.KEY_A:
            if self.accel.x < 0:
                self.accel.x = 0

        elif key == Key.KEY_D:
            if self.accel.x > 0:
                self.accel.x = 0

    def render(self, canvas: simplegui.Canvas):
        bounds = self.get_bounds()
        bounds.min = self.get_pos()
        bounds.max = bounds.min + self.get_size()

        # Draw player.
        point_list = bounds.into_point_list()
        color = Color(120, 120, 200)

        canvas.draw_polygon(point_list, 1, str(color), str(color))  # TODO: sprite?

        # Update position.
        self.last_pos = self.pos.copy()
        self.pos.add(self.vel)
        self.vel.add(self.accel)

        vel_mag_x = abs(self.vel.x)
        if vel_mag_x > PLAYER_VELOCITY[0]:
            sign = self.vel.x / vel_mag_x
            self.vel.x = sign * PLAYER_VELOCITY[0]

        if self.accel.x == 0:
            self.vel.x /= PLAYER_VELOCITY_DIVISOR

        # Check collisions position.
        for item in self.world.level.items:
            if item.collides_with(bounds):
                item.on_collide(self)
