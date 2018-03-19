import util
import simplegui

from util import Color, Font
from geom import Vector
from window import Window, WindowHandler
from button import Button

__all__ = ['StartMenu']


class StartMenu(WindowHandler):

    def start(self, btn: Button, pos: Vector):
        from world import World

        btn.window.handler = World(btn.window, self)

    def help(self, btn: Button, pos: Vector):
        from helpmenu import HelpMenu

        btn.window.handler = HelpMenu(btn.window)

    def __init__(self, window: Window):
        super().__init__(window)

        from constants import BUTTON_SIZE

        self.window_size = window.get_size()
        self.window_center = (self.window_size[0] / 2, self.window_size[1] / 2)

        dpi_factor = window.hidpi_factor

        button_size = (BUTTON_SIZE[0] * dpi_factor, BUTTON_SIZE[1] * dpi_factor)
        button_font = Font('sans-serif', 16, dpi_factor)

        self.bg_image = util.load_image('assets/background.png')
        self.bg_size = (self.bg_image.get_width(), self.bg_image.get_height())
        self.bg_center = (self.bg_size[0] / 2, self.bg_size[1] / 2)

        self.logo = util.load_image('assets/logo.png')
        self.logo_size = (self.logo.get_width(), self.logo.get_height())
        self.logo_center = (self.logo_size[0] / 2, self.logo_size[1] / 2)

        self.max_score = 0
        self.last_active_level = None

        self.text_font = Font('monospace', 20, window.hidpi_factor)
        self.text_font_color = Color(255, 255, 255)

        # Template to create new button
        start_btn = Button(window,
                           '[ Start ]',
                           Vector(self.window_center[0] - button_size[0] / 2,
                                  self.window_center[1] - button_size[1]),
                           Vector(*button_size),
                           Color(0, 102, 255), Color(255, 255, 255),
                           Color(0, 80, 230), Color(255, 255, 255),
                           font=button_font)
        start_btn.set_click_handler(self.start)
        self.children.append(start_btn)

        help_btn = Button(window,
                          '[ Help ]',
                          Vector(self.window_center[0] - button_size[0] / 2,
                                 self.window_center[1] + button_size[1]),
                          Vector(*button_size),
                          Color(0, 102, 255), Color(255, 255, 255),
                          Color(0, 80, 230), Color(255, 255, 255),
                          font=button_font)
        help_btn.set_click_handler(self.help)
        self.children.append(help_btn)

    def render(self, canvas: simplegui.Canvas):
        # Draw background.
        canvas.draw_image(self.bg_image, self.bg_center, self.bg_size, self.window_center,
                          self.window_size)

        if not (self.last_active_level is None):
            last_score = self.last_active_level.get_score()
            if last_score > self.max_score:
                self.max_score = last_score

        # Draw logo
        canvas.draw_image(self.logo, self.logo_center, self.logo_size,
                          (self.window_center[0], self.window_size[1] / 4),
                          (self.window_size[0] / 4, self.window_size[1] / 4))

        # TODO: load highscore
        dpi_factor = self.window.hidpi_factor
        canvas.draw_text("HIGH SCORE // {0:d}".format(self.max_score),
                         (10 * dpi_factor, 20 * dpi_factor), self.text_font.get_size(),
                         str(self.text_font_color), self.text_font.get_face())

        # Draw children.
        super().render(canvas)
