from sdl2 import *
import sdl2.ext
from sdl2.sdlmixer import *
from sdl2.surface import *
from sdl2.sdlimage import *
from game_state import *

def update(self):
    match self.game_state:
        case Game_State.INTRO:
            if self.gt.elapsed_time()>3000000:
                self.gt.set_timer()
                self.game_state = Game_State.PLAY
                #change background
                self.bg = self.AM.image_index("black")
            return

        case Game_State.MAIN_MENU:
            return

        case Game_State.OPTIONS:
            return

        case Game_State.PLAY:
            t = self.gt.elapsed_time()
            #if self.fps_trap==10:
            #    print("fps:",1000000/t)
            #    self.fps_trap=0
            #self.fps_trap += 1
            self.gt.set_timer()
            for i in self.balls:
                i.update(self.width,self.height,t)
            return

        case Game_State.CREDITS:
            return

        case Game_State.END.value:
            return
    return