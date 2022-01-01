from sdl2 import *
import sdl2.ext
from sdl2.sdlmixer import *
from sdl2.surface import *
from sdl2.sdlimage import *


#renderer

def intro_r(self):
    SDL_RenderCopy(self.renderer,self.AM.assets[self.AM.image_index("title")].image,None,self.screen_rect)
    return

def menu_r(self):
    return

def options_r(self):
    return

def play_r(self):
    for b in self.balls:
        SDL_RenderCopy(self.renderer,self.AM.assets[b.color].image,None,b.b_rect)
    return

def credits_r(self):
    return

def end_r(self):
    return
switch_r = {"intro":intro_r,"menu":menu_r,"options":options_r,"play":play_r,"credits":credits_r,"end":end_r}
def render(self):
    SDL_RenderClear(self.renderer)
    SDL_SetRenderDrawColor(self.renderer,0,0,0,255)
    r = switch_r.get(self.game_state)
    if r:
        r(self)
    SDL_RenderPresent(self.renderer)
    return

