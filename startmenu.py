from typing import Tuple
from button import Button
from window import Window, WindowHandler
from util import simplegui, Color

def generic_button_click(btn):
    print("Clicked " + str(btn.caption))

class StartMenu(WindowHandler):

    def __init__(self, window: Window):
        super().__init__(window)
        self.btn = []

        #Args: text, font size, font face (either monospace, serif or sans-serif), position, size, border size, back colour normal, text colour normal, back colour mouse over, text colour mouse over, lerp factor (bigger = more aggressive change)
        for x in range(4):
            new_button = Button("Test" + str(x), 16 + 8 * (x + 1), "serif", (200 * (x + 1), 50), (100, 50), 3, Color(255, 0, 0), Color(127, 0, 0), Color(0, 190, 0), Color(190, 0, 0), 0.05)
            new_button.set_click_handler(generic_button_click)
            self.btn.append(new_button)

    def render(self, canvas: simplegui.Canvas):
        for button in self.btn:
            button.render(canvas)
        
    def on_click(self, pos: Tuple[int, int]):
        for button in self.btn:
            if button.check_click():
                break