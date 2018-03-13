import simplegui
import util

from util import Font, Color
from geom import Vector
from window import Window, WindowHandler
from button import Button

__all__ = ['HelpMenu']


class HelpMenu(WindowHandler):

    def back(self, btn: Button, pos: Vector):
        from startmenu import StartMenu

        btn.window.handler = StartMenu(btn.window)

    def __init__(self, window: Window):
        super().__init__(window)

        from constants import BUTTON_SIZE

        window_size = window.get_size()
        window_center = (window_size[0] / 2, window_size[1] / 2)

        dpi_factor = window.hidpi_factor

        button_size = (BUTTON_SIZE[0] * dpi_factor, BUTTON_SIZE[1] * dpi_factor)
        button_font = Font('sans-serif', 16, dpi_factor)

        self.bg_image = util.load_image('assets/background.png')

        back_btn = Button(window,
                          'Back',
                          Vector(window_center[0] - button_size[0] / 2,
                                 window_size[1] * 2 / 3),
                          Vector(*button_size),
                          Color(255, 0, 0), Color(0, 255, 0),
                          Color(0, 255, 0), Color(255, 0, 0),
                          font=button_font)
        back_btn.set_click_handler(self.back)
        self.children.append(back_btn)

    def render(self, canvas: simplegui.Canvas):
        # Draw background.
        bg_size = (self.bg_image.get_width(), self.bg_image.get_height())
        bg_center = (bg_size[0] / 2, bg_size[1] / 2)
        window_size = self.window.get_size()
        window_center = (window_size[0] / 2, window_size[1] / 2)
        canvas.draw_image(self.bg_image, bg_center, bg_size, window_center, window_size)

        # Draw children.
        super().render(canvas)

        # TODO: style and center text to relative window and dpi factor
        canvas.draw_text('Help menu', (430, 40), 28, 'Black')
        canvas.draw_text('Keys:', (60, 60), 24, 'Black')
        canvas.draw_text('D - Go forwards', (60, 80), 24, 'Black')
        canvas.draw_text('A - Go backwards', (60, 100), 24, 'Black')
        canvas.draw_text('Space bar - Jump', (60, 120), 24, 'Black')
