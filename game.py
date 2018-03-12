from constants import FULLSCREEN, GAME_NAME, WINDOW_SIZE
from startmenu import StartMenu
from window import Window


def main():
    """
    The main launch function.
    """

    window = Window(GAME_NAME, WINDOW_SIZE, fullscreen=FULLSCREEN)
    window.handler = StartMenu(window)
    window.show()


# Check we are running and not importing.
if __name__ == '__main__':
    main()
