from util import simplegui
from window import Window, WindowHandler
from button import Button
from util import Font, Color
from vector import Vector

BUTTON_SIZE = Vector(200, 50)

BG_IMAGE = simplegui.load_image('https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/0kjHIH6/old-retro-video-game-arcade-clouds-moving-on-a-blue-sky_hcd0pxim__F0000.png')

class HelpMenu(WindowHandler):

    def btn1_on_click(self, btn: Button, pos: Vector):
        print("Back button clicked")

        self.window.destroy()  # TODO: Switch to game view.

    def __init__(self, window: Window):
        super().__init__(window)

        win_size = window.get_size()

        btn1 = Button(window, "Back to start menu", Vector(win_size[0] / 2 - BUTTON_SIZE.x / 2, 300), BUTTON_SIZE,
                    Color(255, 0, 0), Color(0, 255, 0), Color(0, 255, 0), Color(255, 0, 0), 0)
        btn1.set_click_handler(self.btn1_on_click)
        self.children.append(btn1)

    def render(self, canvas: simplegui.Canvas):
        canvas.draw_image(BG_IMAGE, (1920 / 2, 1080 / 2), (1920, 1080), (500, 300),
                          self.window.get_size())
        super().render(canvas)

        canvas.draw_text('Help menu', (430, 40), 28, 'Black')
        canvas.draw_text('Keys:', (60,60), 24, 'Black')
        canvas.draw_text('D - Go forwards', (60, 80), 24, 'Black')
        canvas.draw_text('A - Go backwards', (60, 100), 24, 'Black')
        canvas.draw_text('Space bar - Jump', (60, 120), 24, 'Black')
