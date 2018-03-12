from modules import simplegui
from vector import Vector
from window import Window, WindowHandler
<<<<<<< HEAD
from util import Font, Color
from button import Button
from constants import *
from levelone import LevelOne

START_BUTTON_SIZE = Vector(200, 50)
IMAGE_SIZE = Vector(1000, 300)

class StartMenu(WindowHandler):

    #window: Window, text: str, pos: Vector, size: Vector = Vector(150, 50),
                 #bg: Color = Color(200, 200, 200), fg: Color = Color(20, 20, 20),
                 #bg_over: Color = Color(220, 220, 220), fg_over: Color = Color(20, 20, 20),
                 #border_size: int = 0, font: Font = Font('sans-serif', 15)

    def handle_btn_1_click(self, pos: Vector, dunno):
        self.window.destroy()

    def __init__(self, window: Window):
        super().__init__(window)

        win_size = window.get_size()
        self.btns = []
        self.window = window

        # Template to create new button
        btn1 = Button(window, "Start Game", Vector(win_size[0] / 2 - START_BUTTON_SIZE.x / 2, 100), START_BUTTON_SIZE, Color(255, 0, 0), Color(0, 255, 0), Color(0, 255, 0), Color(255, 0, 0), 0)
        btn1.set_click_handler(self.handle_btn_1_click)
        self.btns.append(btn1)

    def render(self, canvas: simplegui.Canvas):
        super().render(canvas)
        for btn in self.btns:
            btn.render(canvas)

        self.background_pos_x += 1
        if self.background_pos_x == IMAGE_SIZE.x:
            self.background_pos_x = 0

        canvas.draw_image()

    def on_click(self, pos: Vector):
        super().on_click(pos)
        for btn in self.btns:
            btn.on_click(pos)
