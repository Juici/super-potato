from util import simplegui
from constants import *
from window import Window, Renderable, WindowHandler
from vector import Vector

class Level(WindowHandler):
    """
    A game level.
    """

    def __init__(self, window: Window):
        super().__init__(window)
        self.renderables = []
        self.character = None
        self.parallax_offset_x = 0

    def add_renderable(self, item: Renderable):
        self.renderables.append(item)

    def set_character(self, character: Renderable):
        self.character = character

    def render(self, canvas: simplegui.Canvas):
        for rend in self.renderables:
            rend.render(canvas, self.renderables)
        self.character.render(canvas, self.renderables)

    def on_key_down(self, key: Key):
        if (self.character):
            self.character.on_key_down(key)

    def on_key_up(self, key: Key):
        if (self.character):
            self.character.on_key_up(key)
