import util

from modules import simplegui
from vector import Vector
from window import Window, WindowHandler
from util import Font, Color
from button import Button
from levelone import LevelOne


# TODO: Source image locally.
# BG_IMAGE = simplegui.load_image('https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/0kjHIH6/old-retro-video-game-arcade-clouds-moving-on-a-blue-sky_hcd0pxim__F0000.png')


class StartMenu(WindowHandler):

    def btn1_on_click(self, btn: Button, pos: Vector):
        print("Start button clicked")

        self.window.destroy()  # TODO: Switch to game view.

    def btn2_on_click(self, btn: Button, pos: Vector):
        # TODO: Load Jamie's help class.
        print("Help button clicked")

    def __init__(self, window: Window):
        super().__init__(window)

        win_size = window.get_size()
        win_center = (win_size[0] / 2, win_size[1] / 2)

        dpi_factor = window.hidpi_factor

        button_size = (200 * dpi_factor, 50 * dpi_factor)
        button_font = Font('sans-serif', 16, dpi_factor)

        self.bg_image = util.load_image('assets/background.png')

        # Template to create new button
        btn1 = Button(window,
                      'Start',
                      Vector(win_center[0] - button_size[0] / 2,
                             win_center[1] - button_size[1]),
                      Vector.new_from(button_size),
                      Color(255, 0, 0), Color(0, 255, 0),
                      Color(0, 255, 0), Color(255, 0, 0),
                      font=button_font)
        btn1.set_click_handler(self.btn1_on_click)
        self.children.append(btn1)

        btn2 = Button(window,
                      'Help',
                      Vector(win_center[0] - button_size[0] / 2,
                             win_center[1] + button_size[1]),
                      Vector.new_from(button_size),
                      Color(255, 0, 0), Color(0, 255, 0),
                      Color(0, 255, 0), Color(255, 0, 0),
                      font=button_font)
        btn2.set_click_handler(self.btn2_on_click)
        self.children.append(btn2)

    def render(self, canvas: simplegui.Canvas):
        # Draw background.
        bg_size = (self.bg_image.get_width(), self.bg_image.get_height())
        bg_center = (bg_size[0] / 2, bg_size[1] / 2)
        window_size = self.window.get_size()
        window_center = (window_size[0] / 2, window_size[1] / 2)
        canvas.draw_image(self.bg_image, bg_center, bg_size, window_center, window_size)

        # Draw children.
        super().render(canvas)

#        self.background_pos_x += 1
#        if self.background_pos_x == IMAGE_SIZE.x:
#            self.background_pos_x = 0
