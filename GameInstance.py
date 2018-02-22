try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class GameInstance:

    def drawWindow(self, canvas): pass

    def __init__(self, windowSize):
        window = simplegui.create_frame("Game Name", windowSize.x, windowSize.y)
        window.set_draw_handler(self.drawWindow)
        self.window = window