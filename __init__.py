from game_engine.game_engine import *

def main():
    g = Game(960,540,TITLE)
    g.main_loop()
    SDL_Quit()
    return

if not PROFILE:
    if __name__ == "__main__":
        main()
else:
    profile()