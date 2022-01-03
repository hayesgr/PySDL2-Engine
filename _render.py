from sdl2 import *
import sdl2.ext
from sdl2.sdlmixer import *
from sdl2.surface import *
from sdl2.sdlimage import *
from Game_State import *

def render(self):
    SDL_RenderClear(self.renderer)
    SDL_SetRenderDrawColor(self.renderer,0,0,0,255)
    match self.game_state:
        case Game_State.INTRO:
            SDL_RenderCopy(self.renderer,self.AM.assets[self.AM.image_index("title")].image,None,self.screen_rect)

        case Game_State.MAIN_MENU:
            pass

        case Game_State.OPTIONS:
            pass

        case Game_State.PLAY:
            for b in self.balls:
                SDL_RenderCopy(self.renderer,self.AM.assets[b.color].image,None,b.b_rect)
        
        case Game_State.CREDITS:
            pass

        case Game_State.END:
            pass
        
    SDL_RenderPresent(self.renderer)
    return