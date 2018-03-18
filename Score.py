from constants import *
from util import simplegui

class Score:

    def __init__(self):
        self.high_score = 0
        self.score = 0

    def get_high_score(self):
        return self.high_score

    def get_score(self):
        return self.score

    def add_score(self, new_score: int):
        self.score += new_score

    def reset_score(self):
        self.score = 0