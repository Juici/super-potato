import simplegui

from typing import TYPE_CHECKING
from constants import PLAYER_SIZE, PLAYER_VELOCITY, PLAYER_ACCELERATION, Key
from util import Color
from geom import Vector, Polygon
from window import Renderable

# Work around cyclic imports.
if TYPE_CHECKING:
    from world import World

__all__ = ['LevelItem', 'Rect', 'Trap', 'Finish', 'Platform', 'Player']


class LevelItem(Renderable):

    def __init__(self, world: 'World'):
        super().__init__(world.window)
        self.world = world

    def get_bounds(self) -> Polygon:
        raise NotImplementedError

    def on_collide(self, player: 'Player'):
        pass

    def collides_with(self, polygon: Polygon) -> bool:
        poly1 = self.get_bounds()
        n1 = len(poly1)
        if n1 == 0:
            return False

        poly2 = polygon
        n2 = len(poly2)
        if n2 == 0:
            return False

        # Basic cases where a point is inside the polygon.
        if poly1.contains(poly2[0]):
            return True
        elif poly2.contains(poly1[0]):
            return True

        from geom import lines_intersect

        # Loop bounds.
        for i1 in range(n1):
            j1 = (i1 + 1) % n1
            l1 = (poly1[i1], poly1[j1])

            for i2 in range(n2):
                j2 = (i2 + 1) % n2
                l2 = (poly2[i2], poly2[j2])

                if lines_intersect(l1, l2):
                    return True

        return False  # TODO: implement some nutty polygon-polygon collision logic


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

        return pos + offset

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
        return Color(0, 0, 0, 0.0)

    def render(self, canvas: simplegui.Canvas):
        point_list = self.get_bounds().into_point_list()
        border_width = self.get_border_width()
        border_color = self.get_border_color()
        fill_color = self.get_fill_color()

        canvas.draw_polygon(point_list, border_width, border_color, fill_color)

    def get_bounds(self) -> Polygon:
        dpi_factor = self.window.hidpi_factor

        pos = self.get_render_pos() * dpi_factor
        size = self.get_size() * dpi_factor

        return Polygon(
            Vector(pos.x, pos.y),
            Vector(pos.x + size.x, pos.y),
            Vector(pos.x + size.x, pos.y + size.y),
            Vector(pos.x, pos.y + size.y),
        )


class Trap(Rect):

    def __init__(self, world: 'World', pos: Vector, size: Vector):
        super().__init__(world)

        self.pos = pos
        self.size = size
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

    def __init__(self, world: 'World', pos: Vector, size: Vector,
                 color: Color = Color(200, 200, 200), fill: bool = False):
        super().__init__(world)

        self.pos = pos
        self.size = size
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

    def jump(self):
        self.vel.y = PLAYER_VELOCITY[1]
        self.accel.y = PLAYER_ACCELERATION[1]

    def get_bounds(self) -> Polygon:
        dpi_factor = self.window.hidpi_factor

        pos = (self.pos - self.world.level.offset) * dpi_factor
        size = self.size * dpi_factor

        return Polygon(
            Vector(pos.x, pos.y),
            Vector(pos.x + size.x, pos.y),
            Vector(pos.x + size.x, pos.y + size.y),
            Vector(pos.x, pos.y + size.y)
        )

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

        # Draw player.
        point_list = bounds.into_point_list()
        color = Color(120, 120, 200)

        canvas.draw_polygon(point_list, 1, color, color)  # TODO: sprite?

        # Update position.
        self.last_pos = self.pos.copy()
        self.pos.add(self.vel)
        self.vel.add(self.accel)

        # Check collisions position.
        for item in self.world.level.items:
            if item.collides_with(bounds):
                item.on_collide(self)
