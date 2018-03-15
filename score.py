from constants import *

class Score:

    def __init__(self):
        self.score = 0

    def add_score(self, score, newScore: int):
        self.score += newScore

    def reset_score(self, score):
        self.score = 0

    def render(self, score, canvas: simplegui.Canvas):
        canvas.draw_text("SCORE: " + str(self.score), WINDOW_SIZE[], 16, "White")
