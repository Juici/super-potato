from modules import simplegui
from vector import Vector
from window import Window, WindowHandler
from util import Font


class StartMenu(WindowHandler):

    def __init__(self, window: Window):
        super().__init__(window)

        # TODO: start menu

    def render(self, canvas: simplegui.Canvas):
        super().render(canvas)

        text = 'hello there!'
        hidpi_factor = self.window.hidpi_factor
        font = Font('sans-serif', 20)
        text_bounds = font.get_text_bounds(text, hidpi_factor)
        text_pos = (
            self.window.width / 2 - text_bounds.x / 2,
            self.window.height / 2 + text_bounds.y / 4
        )
        canvas.draw_text(text, text_pos, int(font.size * hidpi_factor), 'yellow', font.face)

    def on_click(self, pos: Vector):
        super().on_click(pos)
