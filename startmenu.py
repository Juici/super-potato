from button import Button
from window import Window, WindowHandler
from util import simplegui, Color


class StartMenu(WindowHandler):

    def __init__(self, window: Window):
        super().__init__(window)
        self.btn_start = Button("Start Game", (200, 50), (50, 50), 3, Color(255, 0, 0), Color(127, 0, 0), Color(0, 190, 0), Color(190, 0, 0), 0.05)

    def render(self, canvas: simplegui.Canvas):
        self.btn_start.render(canvas)
        