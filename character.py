from util import simplegui
from constants import *
from vector import Vector
from window import Renderable, Window
#from sprite import Sprite

class Character(Renderable):

    def __init__(self, spritesheet_image: str, window: Window):
        self.current_position = Vector(100, 200)
        self.window_size = window.get_size()
        self.target_move_x = 0
        self.target_move_y = 0
        self.force_down_y = 0 # Keep 0 on ground collision, else set to 1 and multiply by 2 each frame
        self.on_ground = False
        self.jumping = False
        self.gravity = 0.2

    def extrapolate(self) -> Vector:
        return self.current_position + Vector(self.target_move_x, self.target_move_y)

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

    def render(self, canvas: simplegui.Canvas, renderables: Renderable):
        temp_position = self.extrapolate()

        if temp_position.x <= self.window_size[0] and temp_position.x >= 0:
            self.current_position.x = temp_position.x

        if temp_position.y <= self.window_size[1] and temp_position.y >= 0:
            self.on_ground = False
            self.force_down_y += self.gravity
        else:
            self.force_down_y = self.window_size[1]
            self.current_position.y = 0
            self.on_ground = True

        print(self.on_ground)
        print(self.jumping)

        if self.jumping and self.on_ground:
            print("OK")
            self.force_down_y = -5

        self.current_position.y += self.force_down_y
        
        canvas.draw_text("C", (self.current_position.x, self.current_position.y), 10, "Red")
