from util import simplegui
from constants import *
from vector import Vector
from window import Renderable, Window
from level import Level
#from sprite import Sprite

class Character(Renderable):

    def __init__(self, position: Vector, size: Vector, window: Window, level: Level):
        self.current_position = position
        self.window_size = window.get_size()
        self.size = size
        self.target_move_x = 0
        self.target_move_y = 0
        self.force_down_y = 0 # Keep 0 on ground collision, else set to 1 and multiply by 2 each frame
        self.on_ground = False
        self.jumping = False
        self.level = level
        level.set_character(self)

    def on_key_down(self, key: Key):
        if (key == Key.SPACE):
            self.jumping = True
        if (key == Key.KEY_A):
            self.target_move_x -= 1
        elif (key == Key.KEY_D):
            self.target_move_x += 1

    def on_key_up(self, key: Key):
        if (key == Key.SPACE):
            self.jumping = False
        if (key == Key.KEY_A):
            self.target_move_x += 1
        elif (key == Key.KEY_D):
            self.target_move_x -= 1

    def get_pos(self) -> Vector:
        return self.current_position

    def get_size(self) -> Vector:
        return self.size

    def get_next_pos(self) -> Vector:
        return self.current_position + Vector(self.target_move_x * PLAYER_MOVEMENT_SCALAR, self.force_down_y)

    def render(self, canvas: simplegui.Canvas, renderables: Renderable):
        target_position = self.get_next_pos()
        window_size = self.window_size

        # Check if next position will be in the window's width bounds and rectify if not
        if target_position.x > window_size[0]:
            target_position.x = window_size[0]
        elif target_position.x < 0:
            target_position.x = 0

        # Store any renderable the character is colliding with
        colliding_with = None

        for renderable in self.level.renderables:
            renderable_pos = renderable.get_next_pos()
            # If character is on the same x bounds
            if self.current_position.x >= renderable_pos.x and self.current_position.x <= renderable_pos.x + renderable.get_size().x:
                # If character is about to either drop lower or continue to drop
                if (renderable_pos.y - target_position.y) <= 0:
                    # If character has just passed through
                    if (renderable_pos.y - self.current_position.y) > 0:
                        colliding_with = renderable
                        target_position.y = renderable_pos.y - 0.1
                        self.on_ground = True
                        self.force_down_y = 0
                        break

        if colliding_with == None:
            # If not colliding with any object, check window collision
            if target_position.y <= window_size[1] and target_position.y >= 0:
                self.on_ground = False
                self.force_down_y += PLAYER_GRAVITY
            else:
                target_position.y = window_size[1]
                self.force_down_y = 0
                self.on_ground = True

        if self.jumping and self.on_ground:
            self.force_down_y = -PLAYER_JUMP_FORCE

        self.current_position = target_position
        canvas.draw_text("C", self.current_position.into_tuple(), 30, "Red")
