from util import simplegui
from window import WindowHandler
import button

class StartMenu(WindowHandler):

    def __init__(self):

    	self.btn_start = button("Start Game", Vector(200, 50), Vector(50, 50), "Red", "Blue")

    def render(self):

    	self.btn_start().update()
