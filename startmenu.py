from modules import simplegui
from vector import Vector
from window import Window, WindowHandler
from util import Font, Color
from button import Button
from constants import *
from levelone import LevelOne

BUTTON_SIZE = Vector(200, 50)

# TODO: Source image locally.
BG_IMAGE = simplegui.load_image('https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/0kjHIH6/old-retro-video-game-arcade-clouds-moving-on-a-blue-sky_hcd0pxim__F0000.png')

class StartMenu(WindowHandler):

    #window: Window, text: str, pos: Vector, size: Vector = Vector(150, 50),
                 #bg: Color = Color(200, 200, 200), fg: Color = Color(20, 20, 20),
                 #bg_over: Color = Color(220, 220, 220), fg_over: Color = Color(20, 20, 20),
                 #border_size: int = 0, font: Font = Font('sans-serif', 15)

    def btn1_on_click(self, btn: Button, pos: Vector):
        print("Start button clicked")

        self.window.destroy()  # TODO: Switch to game view.

    def btn2_on_click(self, btn: Button, pos: Vector):
        # TODO: Load Jamie's help class.
        print("Help button clicked")

    def __init__(self, window: Window):
        super().__init__(window)

        win_size = window.get_size()

        # Template to create new button
        btn1 = Button(window, "Start Game", Vector(win_size[0] / 2 - BUTTON_SIZE.x / 2, 300), BUTTON_SIZE, Color(255, 0, 0), Color(0, 255, 0), Color(0, 255, 0), Color(255, 0, 0), 0)
        btn1.set_click_handler(self.btn1_on_click)
        self.children.append(btn1)

        btn2 = Button(window, "Help", Vector(win_size[0] / 2 - BUTTON_SIZE.x / 2 , 375), BUTTON_SIZE, Color(255, 0, 0), Color(0, 255, 0), Color(0, 255, 0), Color(255, 0, 0), 0)
        btn2.set_click_handler(self.btn2_on_click)
        self.children.append(btn2)

    def render(self, canvas: simplegui.Canvas):
        # Draw background.
        canvas.draw_image(BG_IMAGE, (1920 / 2, 1080 / 2), (1920, 1080), (500, 300),
                          self.window.get_size())

        # Draw children.
        super().render(canvas)

#        self.background_pos_x += 1
#        if self.background_pos_x == IMAGE_SIZE.x:
#            self.background_pos_x = 0

