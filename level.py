from util import simplegui
from pygame import time
from constants import *
from window import Window, Renderable, WindowHandler
from vector import Vector
from level_items import *
from math import *

class Level(WindowHandler):
    """
    A game level.
    """

    def __init__(self, window: Window):
        super().__init__(window)
        self.renderables = []
        self.platforms = []
        self.traps = []
        self.character = None
        self.window_size = window.get_size()
        self.offset = 0
        self.complete_status = 0

    def add_platform(self, item: Platform):
        self.platforms.append(item)
        self.renderables.append(item)

    def add_trap(self, item: Trap):
        self.traps.append(item)
        self.renderables.append(item)

    def set_character(self, character: Renderable):
        self.character = character

    def set_finish(self, finish: Renderable):
        self.finish = finish

    def onto_next_level(self):
        pass
        
    def restart_level(self):
        pass

    def render(self, canvas: simplegui.Canvas):
        char = self.character
        for rend in self.renderables:
            rend.render(canvas)
        char.render(canvas)
        self.finish.render(canvas)
        char_pos = char.get_pos()
        self.offset += LEVEL_X_PUSH

        level_status = 0

        for trap in self.traps:
            if trap.get_bounding_box().intersects_with(char.get_bounding_box()):
                level_status = 1
                break

        if char_pos.x == 0 or char_pos.y == self.window_size[1]:
            level_status = 1

        if level_status == 2:
            self.onto_next_level()
        else:
            self.restart_level()

    def on_key_down(self, key: Key):
        if (self.character):
            self.character.on_key_down(key)

    def on_key_up(self, key: Key):
        if (self.character):
            self.character.on_key_up(key)
