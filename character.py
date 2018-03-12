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

    def get_desired_movement() -> Vector:
        return Vector(self.target_move_x, 0)

    def on_key_down(self, key: Key):
        if (key == Key.KEY_A):
            print("Down A")
            self.target_move_x -= 1
        elif (key == Key.KEY_D):
            print("Down D")
            self.target_move_x += 1

    def on_key_up(self, key: Key):
        print("A key up")
        if (key == Key.KEY_A):
            print("Up A")
            self.target_move_x += 1
        elif (key == Key.KEY_D):
            print("Up D")
            self.target_move_x -= 1

    def get_pos() -> Vector:
        return self.current_position

    def render(self, canvas: simplegui.Canvas, renderables: Renderable):
        #canvas.draw_image()
        #self.sprite.render(canvas)
        #print(self.target_move_x)
        temp_position = self.current_position + Vector(self.target_move_x, 0)
        if temp_position.x <= self.window_size[0] and temp_position.x >= 0:
            self.current_position = temp_position
        canvas.draw_text("C", (self.current_position.x, self.current_position.y), 10, "Red")
