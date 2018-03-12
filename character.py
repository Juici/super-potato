from block import Block
from util import simplegui, Polygon
from constants import *
from vector import Vector
from window import Renderable, Window
from typing import Tuple


class Character(Renderable):

    def __init__(self, window: Window, initial_pos: Vector, size: Vector):
        super().__init__(window)

        self.current_position = initial_pos
        self.size = size
        self.target_move_x = 0
        self.target_move_y = 0
        self.force_down_y = 0  # 0 on ground collision, set to 1 and multiply by 2 each frame
        self.on_ground = False
        self.jumping = False
        self.offset = Vector(-size.x / 2, -size.y)

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
        if key == Key.SPACE:
            self.jumping = True
        elif key == Key.KEY_A:
            self.target_move_x -= 1
        elif key == Key.KEY_D:
            self.target_move_x += 1

    def on_key_up(self, key: Key):
        if key == Key.SPACE:
            self.jumping = False
        elif key == Key.KEY_A:
            self.target_move_x += 1
        elif key == Key.KEY_D:
            self.target_move_x -= 1

    def get_pos(self) -> Vector:
        return self.current_position

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

    def render(self, canvas: simplegui.Canvas):
        target_position = self.get_next_pos()
        window_size = self.window.get_size()

        # Check if next position will be in the window's width bounds and rectify if not
        if target_position.x > window_size[0] / 2:
            target_position.x = window_size[0] / 2
        elif target_position.x - self.size.x < 0:
            # TODO: death
            self.parent.children.remove(self)

        # Store any renderable the character is colliding with
        colliding_with = None

        for r in self.parent.children:
            if isinstance(r, Block):
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

        if colliding_with is None:
            # If not colliding with any object, check window collision
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
