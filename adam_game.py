from constants import FULLSCREEN, GAME_NAME, WINDOW_SIZE
from startmenu import StartMenu
from window import Window
from level import GameView
from level_items import *
from vector import Vector

def main():
    """
    The main launch function.
    """
    window = Window(GAME_NAME, WINDOW_SIZE, fullscreen=FULLSCREEN)
    
    level_two = GameView(window, None)
    level_one = GameView(window, level_two)

    l1_player_character    = Character(window, Vector(100, 100), Vector(10, 10))
    l1_trap_one            = Trap(window, Vector(1200, 270), Vector(80, 30), "rgb(180, 16, 16)")
    l1_finish_one          = Finish(window, Vector(1580, 180), Vector(40, 120), "rgb(255, 255, 255)")
    l1_platform_start      = Platform(window, Vector(50, 550), Vector(200, 10), "rgb(127, 127, 127)")
    l1_platform_one        = Platform(window, Vector(300, 550), Vector(100, 10), "rgb(127, 127, 127)")
    l1_platform_two        = Platform(window, Vector(420, 485), Vector(100, 10), "rgb(127, 127, 127)")
    l1_platform_three      = Platform(window, Vector(540, 420), Vector(300, 10), "rgb(127, 127, 127)")
    l1_platform_four       = Platform(window, Vector(940, 380), Vector(15, 10), "rgb(127, 127, 127)")
    l1_platform_five       = Platform(window, Vector(940, 300), Vector(15, 10), "rgb(127, 127, 127)")
    l1_platform_six        = Platform(window, Vector(1020, 300), Vector(600, 10), "rgb(127, 127, 127)")

    level_one.add_child(l1_player_character)
    level_one.add_child(l1_platform_start)
    level_one.add_child(l1_platform_one)
    level_one.add_child(l1_platform_two)
    level_one.add_child(l1_platform_three)
    level_one.add_child(l1_platform_four)
    level_one.add_child(l1_platform_five)
    level_one.add_child(l1_platform_six)
    level_one.add_child(l1_trap_one)
    level_one.add_child(l1_finish_one)

    l2_player_character    = Character(window, Vector(100, 100), Vector(10, 10))
    l2_trap_one            = Trap(window, Vector(1200, 270), Vector(80, 30), "rgb(180, 16, 16)")
    l2_finish_one          = Finish(window, Vector(1580, 180), Vector(40, 120), "rgb(255, 255, 255)")
    l2_platform_start      = Platform(window, Vector(50, 550), Vector(200, 10), "rgb(127, 127, 127)")
    l2_platform_one        = Platform(window, Vector(300, 550), Vector(100, 10), "rgb(127, 127, 127)")
    l2_platform_two        = Platform(window, Vector(420, 485), Vector(100, 10), "rgb(127, 127, 127)")
    l2_platform_three      = Platform(window, Vector(540, 420), Vector(300, 10), "rgb(127, 127, 127)")
    l2_platform_four       = Platform(window, Vector(940, 380), Vector(15, 10), "rgb(127, 127, 127)")
    l2_platform_five       = Platform(window, Vector(940, 300), Vector(15, 10), "rgb(127, 127, 127)")
    l2_platform_six        = Platform(window, Vector(1020, 300), Vector(600, 10), "rgb(127, 127, 127)")

    level_two.add_child(l2_player_character)
    level_two.add_child(l2_trap_one)
    level_two.add_child(l2_platform_one)
    level_two.add_child(l2_platform_two)
    level_two.add_child(l2_platform_three)
    level_two.add_child(l2_platform_four)
    level_two.add_child(l2_platform_five)
    level_two.add_child(l2_platform_six)
    level_two.add_child(l2_trap_one)
    level_two.add_child(l2_finish_one)

    window.handler = level_one
    window.show()


# Check we are running and not importing.
if __name__ == '__main__':
    main()
