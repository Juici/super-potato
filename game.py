from constants import *
from window import Window


def main():
    """
    The main launch function.
    """
    window = Window(GAME_NAME, WINDOW_SIZE, controls=SHOW_CONTROL_PANEL, fullscreen=FULLSCREEN)
    window.show()


# Check we are running and not importing.
if __name__ == '__main__':
    main()
