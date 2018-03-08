from constants import *
from window import Window
from startmenu import StartMenu
from level import Level
from character import Character


def main():
    """
    The main launch function.
    """
    window = Window(GAME_NAME, WINDOW_SIZE, controls=SHOW_CONTROL_PANEL, fullscreen=FULLSCREEN)
    playerchar = Character("noimage", window)
    first_level = Level(window)
    first_level.set_character(window)
    window.handler = first_level
    window.show()


# Check we are running and not importing.
if __name__ == '__main__':
    main()
