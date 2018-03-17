from constants import *
import simplegui

class Score:

    def __init__(self):
        self.score = 0

    def add_score(self, new_score: int):
        self.score += new_score

    def reset_score(self):
        self.score = 0

    def render(self, canvas: simplegui.Canvas):
        canvas.draw_text("SCORE: " + str(self.score), WINDOW_SIZE, 16, "White")
