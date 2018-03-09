from util import simplegui
from window import Window, WindowHandler
from button import Button

class HelpMenu(WindowHandler):

    def __init__(self, window: Window):
        super().__init__(window)

        btn_back = Button("Back to main menu", (200, 50), (50, 50), Color(255,0,0), Color(0, 0, 255))
        self.children.append(btn_back)

    def render(self, canvas: simplegui.Canvas):
        super().render(canvas)

        canvas.draw_text('Keys:', (20,20), 24, 'Black')
        canvas.draw_text('D - Go forwards', (20, 40), 24, 'Black')
        canvas.draw_text('A - Go backwards', (20, 60), 24, 'Black')
        canvas.draw_text('Space bar - Jump', (20, 80), 24, 'Black')
