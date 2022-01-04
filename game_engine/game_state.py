from enum import Enum
#switch_u = {"intro":intro_u,"menu":menu_u,"options":options_u,"play":play_u,"credits":credits_u,"end":end_u}
class Game_State(Enum):
    INTRO = 1
    MAIN_MENU = 2
    OPTIONS = 3
    PLAY = 4
    CREDITS = 5
    END = 6

