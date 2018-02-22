# Imports

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math, Level, StartMenu, Vector, GameInstance

# Constants

WINDOW_SIZE = Vector((600, 400))

# Variables



# Initialisation

gameWindow = GameInstance(WINDOW_SIZE)