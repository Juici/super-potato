from util import Polygon, Color, Box
from modules import simplegui
from constants import *
from vector import Vector
from window import Renderable, Window
from typing import Tuple


class GenericSquare(Renderable):

    def __init__(self, window: Window, position: Vector, size: Vector, color: Color):
        super().__init__(window)

        self.position = position
        self.size = size
        self.color = color
        self.bounding_box = Box(self)

    def get_bounds(self) -> Polygon:
        return Polygon(
            self.position,
            self.position + (self.size.x, 0),
            self.position + self.size,
            self.position + (0, self.size.y),
        )

    def get_pos(self) -> Vector:
        return self.position

    def get_size(self) -> Vector:
        return self.size

    def get_next_pos(self) -> Vector:
        return self.position

    def update_positions(self):
        self.position -= Vector(LEVEL_X_PUSH, 0)
        self.bounding_box.update_box()

    def get_bounding_box(self):
        return self.bounding_box

class Trap(GenericSquare):

    def __init__(self, window: Window, position: Vector, size: Vector, color: Color):
        super().__init__(window, position, size, color)

    def render(self, canvas: simplegui.Canvas):
        super().update_positions()
        canvas.draw_polygon(self.bounding_box.get_render_vertices(), 1, str(self.color),
                            str(self.color))


class Finish(GenericSquare):

    def __init__(self, window: Window, position: Vector, size: Vector, color: Color):
        super().__init__(window, position, size, color)

    def render(self, canvas: simplegui.Canvas):
        super().update_positions()
        canvas.draw_polygon(self.bounding_box.get_render_vertices(), 1, str(self.color),
                            str(self.color))


class Platform(GenericSquare):

    def __init__(self, window: Window, position: Vector, size: Vector, color: Color):
        super().__init__(window, position, size, color)

    def render(self, canvas: simplegui.Canvas):
        super().update_positions()
        canvas.draw_polygon(self.bounding_box.get_render_vertices(), 1, str(self.color))


class Character(Renderable):

    def __init__(self, window: Window, initial_pos: Vector, size: Vector):
        super().__init__(window)

        self.current_position = initial_pos
        self.size = size
        self.target_move_x = 0
        self.target_move_y = 0
        self.force_down_y = 0
        self.on_ground = False
        self.jumping = False
        self.keyed_down = False
        self.offset = Vector(-size.x / 2, -size.y)
        self.bounding_box = Box(self)

    def get_bounds(self) -> Polygon:
        pos = self.current_position
        size = self.size
        return Polygon(
            Vector(pos.x, pos.y),
            Vector(pos.x + size.x, pos.y),
            Vector(pos.x + size.x, pos.y + size.y),
            Vector(pos.x, pos.y + size.y)
        )

    def on_key_down(self, key: Key):
        self.keyed_down = True # Prevents bug between level switching
        if key == Key.SPACE:
            self.jumping = True
        elif key == Key.KEY_A:
            self.target_move_x -= 1
        elif key == Key.KEY_D:
            self.target_move_x += 1

    def on_key_up(self, key: Key):
        if self.keyed_down:
            if key == Key.SPACE:
                self.jumping = False
            elif key == Key.KEY_A:
                self.target_move_x += 1
            elif key == Key.KEY_D:
                self.target_move_x -= 1

    def get_pos(self) -> Vector:
        return self.current_position + self.offset

    def get_size(self) -> Vector:
        return self.size

    def get_next_pos(self) -> Vector:
        return self.current_position + Vector(
            self.target_move_x * PLAYER_MOVEMENT_SCALAR - LEVEL_X_PUSH, self.force_down_y)

    def get_vertices(self) -> Tuple:
        initial_pos = (self.current_position + self.offset)
        return (
            initial_pos.into_tuple(),
            (initial_pos + Vector(self.size.x, 0)).into_tuple(),
            (initial_pos + Vector(self.size.x, self.size.y)).into_tuple(),
            (initial_pos + Vector(0, self.size.y)).into_tuple()
        )

    def die(self):
        self.parent.children.remove(self)

    def progress(self):
        self.parent.win()

    def render(self, canvas: simplegui.Canvas):
        target_position = self.get_next_pos()
        window_size = self.window.get_size()
        self.bounding_box.update_box()

        # Check if next position will be in the correct width bounds and rectify if not
        if target_position.x > window_size[0] / 2:
            target_position.x = window_size[0] / 2
        elif target_position.x - self.size.x < 0:
            # TODO: death
            self.die()

        # Store any renderable the character is colliding with
        colliding_with = None

        for r in self.parent.children:
            if isinstance(r, Platform):
                r_pos = r.get_next_pos()

                # If character is on the same x bounds
                if r_pos.x <= self.current_position.x <= r_pos.x + r.get_size().x:
                    # If character is about to either drop lower or continue to drop
                    if (r_pos.y - target_position.y) <= 0:
                        # If character has just passed through
                        if (r_pos.y - self.current_position.y) > 0:
                            colliding_with = r
                            target_position.y = r_pos.y - 0.1
                            self.on_ground = True
                            self.force_down_y = 0
                            break
            elif isinstance(r, Trap):
                if (r.get_bounding_box().collides(self.bounding_box)):
                    colliding_with = r
                    self.die()
                    break
            elif isinstance(r, Finish):
                if (r.get_bounding_box().collides(self.bounding_box)):
                    colliding_with = r
                    self.progress()
                    break

        if colliding_with is None:
            # If not colliding with any object, check window height collision
            if 0 <= target_position.y <= window_size[1]:
                self.on_ground = False
                self.force_down_y += PLAYER_GRAVITY
            else:
                target_position.y = window_size[1]
                self.force_down_y = 0
                self.on_ground = True

        if self.jumping and self.on_ground:
            self.force_down_y = -PLAYER_JUMP_FORCE

        self.current_position = target_position
        canvas.draw_polygon(self.get_vertices(), 1, "Red", "Red")
