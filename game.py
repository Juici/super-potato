from constants import GAME_NAME, WINDOW_SIZE, FULLSCREEN
from window import Window
from startmenu import StartMenu


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
