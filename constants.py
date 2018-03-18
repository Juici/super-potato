from enum import IntEnum

__all__ = [
    'GAME_NAME',
    'WINDOW_SIZE',
    'FULLSCREEN',
    'HIDPI_FACTOR',
    'PLAYER_SIZE',
    'PLAYER_VELOCITY',
    'ACCEL_GRAVITY',
    'ACCEL_JUMP',
    'BUTTON_SIZE',
    'LEVEL_BACKGROUND_IMAGE',
    'GRID_SIZE',
    'BLOCK_SIZE',
    'Key'
]

_DPI_SCALE_OPTION = 'dpi-scale'


def _get_hidpi_factor() -> float:
    from sys import argv

    for arg in argv:
        flag = str(arg).lower()

        dpi_scale_opt = '--{0}='.format(_DPI_SCALE_OPTION)
        if flag.startswith(dpi_scale_opt):
            try:
                return float(flag[len(dpi_scale_opt):])
            except ArithmeticError:
                break

    return 1.0


GRID_SIZE = (32, 18)

GAME_NAME = "Super Potato"  # Game name and title of window.
WINDOW_SIZE = (GRID_SIZE[0] * 50, GRID_SIZE[1] * 50)  # The default window size.

BLOCK_SIZE = WINDOW_SIZE[0] / GRID_SIZE[0]

FULLSCREEN = False  # Display fullscreen.

HIDPI_FACTOR = _get_hidpi_factor()  # HiDPI screen scale factor.

PLAYER_SIZE = (BLOCK_SIZE, BLOCK_SIZE * 2)
PLAYER_VELOCITY = (2.8, 10)  # (run, jump)
ACCEL_GRAVITY = -0.2
# PLAYER_VELOCITY_DIVISOR = 1.05

BUTTON_SIZE = (200, 50)

LEVEL_BACKGROUND_IMAGE = 'assets/background.png'

# LEVEL_BACKGROUND_DIMS = (1920, 1080)
# LEVEL_BACKGROUND_STRETCH_X = 1200

ACCEL_JUMP = 2


# LEVEL_BLOCK_SCALE_PX = (WINDOW_SIZE[0] / LEVEL_GRID[0], WINDOW_SIZE[1] / LEVEL_GRID[1])


# Better than the basic simplegui key map.
class Key(IntEnum):
    """
    Keys for keyboard events.
    """

    BACKSPACE = 8
    TAB = 9
    ENTER = 13

    SHIFT = 16
    CTRL = 17
    ALT = 18

    PAUSE_BREAK = 19
    CAPS_LOCK = 20
    ESCAPE = 27
    SPACE = 32

    PAGE_UP = 33
    PAGE_DOWN = 34

    END = 35
    HOME = 36

    ARROW_LEFT = 37
    ARROW_UP = 38
    ARROW_RIGHT = 39
    ARROW_DOWN = 40

    INSERT = 45
    DELETE = 46

    KEY_0 = 48
    KEY_1 = 49
    KEY_2 = 50
    KEY_3 = 51
    KEY_4 = 52
    KEY_5 = 53
    KEY_6 = 54
    KEY_7 = 55
    KEY_8 = 56
    KEY_9 = 57

    KEY_A = 65
    KEY_B = 66
    KEY_C = 67
    KEY_D = 68
    KEY_E = 69
    KEY_F = 70
    KEY_G = 71
    KEY_H = 72
    KEY_I = 73
    KEY_J = 74
    KEY_K = 75
    KEY_L = 76
    KEY_M = 77
    KEY_N = 78
    KEY_O = 79
    KEY_P = 80
    KEY_Q = 81
    KEY_R = 82
    KEY_S = 83
    KEY_T = 84
    KEY_U = 85
    KEY_V = 86
    KEY_W = 87
    KEY_X = 88
    KEY_Y = 89
    KEY_Z = 90

    LEFT_WINDOW = 91
    RIGHT_WINDOW = 92
    SELECT = 93

    NUMPAD_0 = 96
    NUMPAD_1 = 97
    NUMPAD_2 = 98
    NUMPAD_3 = 99
    NUMPAD_4 = 100
    NUMPAD_5 = 101
    NUMPAD_6 = 102
    NUMPAD_7 = 103
    NUMPAD_8 = 104
    NUMPAD_9 = 105

    MULTIPLY = 106
    ADD = 107
    SUBTRACT = 109
    DECIMAL_POINT = 110
    DIVIDE = 111

    FUNCTION_1 = 112
    FUNCTION_2 = 113
    FUNCTION_3 = 114
    FUNCTION_4 = 115
    FUNCTION_5 = 116
    FUNCTION_6 = 117
    FUNCTION_7 = 118
    FUNCTION_8 = 119
    FUNCTION_9 = 120
    FUNCTION_10 = 121
    FUNCTION_11 = 122
    FUNCTION_12 = 123

    NUM_LOCK = 144
    SCROLL_LOCK = 145

    SEMICOLON = 186
    EQUALS = 187
    COMMA = 188
    DASH = 189
    PERIOD = 190
    FORWARD_SLASH = 191
    GRAVE = 192

    LEFT_BRACKET = 219
    BACK_SLASH = 220
    RIGHT_BRACKET = 221
    SINGLE_QUOTE = 222


del _get_hidpi_factor
