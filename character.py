from util import simplegui
from constants import *
from vector import Vector
from window import Renderable, Window
#from sprite import Sprite

class Character:

    def __init__(self, spritesheet_image: str, window: Window):
        self.current_position = Vector(0, 0)
        self.window_size = window.get_size()

    def get_desired_movement() -> Vector:
        return Vector(self.target_move_x, 0)

    def on_key_down(self, key: Key):
        if (key == Key.KEY_D):
            self.target_move.x += 1
        elif (key == Key.KEY_A):
            self.target_move.x -= 1

    def on_key_up(self, key: Key):
        if (key == Key.KEY_D):
            self.target_move.x -= 1
        elif (key == Key.KEY_A):
            self.target_move.x += 1

    def get_current_position() -> Vector:
        return self.current_position

    def render(self, canvas: simplegui.Canvas, renderables: Renderable):
        #canvas.draw_image()
        self.sprite.render(canvas)
        temp_position = self.current_position + Vector(self.target_move_x, 0)
        if temp_position.x <= self.window_size[0] and temp_position.x >= 0:
            self.current_position = temp_position
        self.draw_text("C", (self.current_position.x, self.current_position.y), 10, "Red")