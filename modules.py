__all__ = ['pygame', 'simplegui']

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

try:
    import pygame
except ImportError:
    pygame = None
