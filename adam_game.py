from constants import FULLSCREEN, GAME_NAME, WINDOW_SIZE
from startmenu import StartMenu
from window import Window
from level import Level
from character import Character
from block import Block
from vector import Vector


def main():
    """
    The main launch function.
    """
    window = Window(GAME_NAME, WINDOW_SIZE, fullscreen=FULLSCREEN)
    first_level = Level(window)
    playerchar = Character(Vector(100, 100), Vector(10, 10), window, first_level)
    block_one = Block(Vector(300, 550), Vector(100, 10), "rgb(127, 127, 127)", window, first_level)
    block_two = Block(Vector(420, 520), Vector(100, 10), "rgb(127, 127, 127)", window, first_level)
    block_three = Block(Vector(540, 420), Vector(300, 10), "rgb(127, 127, 127)", window, first_level)
    window.handler = first_level
    window.show()


# Check we are running and not importing.
if __name__ == '__main__':
    main()
