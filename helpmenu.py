from util import simplegui, Color
from window import Window, WindowHandler
from button import Button

class helpMenu(WindowHandler):
    def __init__(self, window, Window):
        super().__init__(window)
        self.btn_backToMenu = Button("Back to main menu", (200, 50), (50, 50), Color(255,0,0), Color(0, 0, 255))

    def draw_handler(simplegui.Canvas):
        #Requires source image centre and source image height/width.
        canvas.draw_image(image, (), (), (50, 50), (100, 100))
    #Requires address of image. Intended to display an image detailing the control scheme.
    image = simplegui.load_image()

    def render(self, canvas: simplegui.Canvas):
        self.btn_backToMenu.render(canvas)

    #May need to be altered/moved.
    frame = simplegui.create_frame('Display', 100, 100)
    frame.set_draw_handler(draw_handler)
    frame.start()