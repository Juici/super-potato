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

        win_size = window.get_size()
        win_center = (win_size[0] / 2, win_size[1] / 2)

        dpi_factor = window.hidpi_factor

        button_size = (BUTTON_SIZE[0] * dpi_factor, BUTTON_SIZE[1] * dpi_factor)
        button_font = Font('sans-serif', 16, dpi_factor)

        self.bg_image = util.load_image('assets/background.png')

        self.logo = util.load_image('assets/logo.png')
        self.logo_size = (self.logo.get_width(), self.logo.get_height())
        self.logo_center = (self.logo_size[0] / 2, self.logo_size[1] / 2)

        self.max_score = 0
        self.last_active_level = None

        # Template to create new button
        start_btn = Button(window,
                           '[ Start ]',
                           Vector(win_center[0] - button_size[0] / 2,
                                  win_center[1] - button_size[1]),
                           Vector(*button_size),
                           Color(0, 102, 255), Color(255, 255, 255),
                           Color(0, 80, 230), Color(255, 255, 255),
                           font=button_font)
        start_btn.set_click_handler(self.start)
        self.children.append(start_btn)

        help_btn = Button(window,
                          '[ Help ]',
                          Vector(win_center[0] - button_size[0] / 2,
                                 win_center[1] + button_size[1]),
                          Vector(*button_size),
                           Color(0, 102, 255), Color(255, 255, 255),
                           Color(0, 80, 230), Color(255, 255, 255),
                          font=button_font)
        help_btn.set_click_handler(self.help)
        self.children.append(help_btn)

    def render(self, canvas: simplegui.Canvas):
        # Draw background.
        bg_size = (self.bg_image.get_width(), self.bg_image.get_height())
        bg_center = (bg_size[0] / 2, bg_size[1] / 2)
        window_size = self.window.get_size()
        window_center = (window_size[0] / 2, window_size[1] / 2)
        canvas.draw_image(self.bg_image, bg_center, bg_size, window_center, window_size)

        if not(self.last_active_level is None):
            last_score = self.last_active_level.get_score()
            if last_score > self.max_score:
                self.max_score = last_score

        # Draw logo
        canvas.draw_image(self.logo, self.logo_center, self.logo_size, (window_center[0], window_center[1] - 250), (window_size[0] / 3, window_size[1] / 3))
        #TODO: load highscore
        canvas.draw_text("HIGH SCORE // " + str(self.max_score), (20, 40), 40, "White")

        # Draw children.
        super().render(canvas)