from constants import FULLSCREEN, GAME_NAME, WINDOW_SIZE
from startmenu import StartMenu
from window import Window
from level import Level
from level_items import *
from vector import Vector

def main():
    """
    The main launch function.
    """
    window = Window(GAME_NAME, WINDOW_SIZE, fullscreen=FULLSCREEN)
    
    level_one = Level(window)
    level_two = Level(window)

    playerchar = Character(Vector(100, 100), Vector(10, 10), window, level_one)

    platform_start = Platform(Vector(50, 550), Vector(200, 10), "rgb(127, 127, 127)", window, level_one)
    platform_one = Platform(Vector(300, 550), Vector(100, 10), "rgb(127, 127, 127)", window, level_one)
    platform_two = Platform(Vector(420, 485), Vector(100, 10), "rgb(127, 127, 127)", window, level_one)
    platform_three = Platform(Vector(540, 420), Vector(300, 10), "rgb(127, 127, 127)", window, level_one)
    platform_four = Platform(Vector(940, 380), Vector(15, 10), "rgb(127, 127, 127)", window, level_one)
    platform_five = Platform(Vector(940, 300), Vector(15, 10), "rgb(127, 127, 127)", window, level_one)
    platform_six = Platform(Vector(1020, 300), Vector(600, 10), "rgb(127, 127, 127)", window, level_one)

    trap_one = Trap(Vector(1200, 270), Vector(80, 30), "rgb(180, 16, 16)", window, level_one)

    finish_one = Finish(Vector(1580, 180), Vector(40, 120), "rgb(255, 255, 255)", window, level_one)

    window.handler = level_one
    window.show()

    # Wait for user to lose or hit finish line
    #


# Check we are running and not importing.
if __name__ == '__main__':
    main()
