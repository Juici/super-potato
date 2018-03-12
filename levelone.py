from modules import simplegui
from vector import Vector
from window import Window, WindowHandler
from util import Font, Color

class LevelOne(WindowHandler):

    #window: Window, text: str, pos: Vector, size: Vector = Vector(150, 50),
                 #bg: Color = Color(200, 200, 200), fg: Color = Color(20, 20, 20),
                 #bg_over: Color = Color(220, 220, 220), fg_over: Color = Color(20, 20, 20),
                 #border_size: int = 0, font: Font = Font('sans-serif', 15)

    def __init__(self, window: Window):
        super().__init__(window)


    def render(self, canvas: simplegui.Canvas):
        super().render(canvas)

    def on_click(self, pos: Vector):
        super().on_click(pos)
