from sdl2 import *
import sdl2.ext
from sdl2.sdlmixer import *
from sdl2.surface import *
from sdl2.sdlimage import *
from enum import Enum
from _gui_resize import gui_resize

#these two enum classes were necessary because of the way match case pattern matching works.
#It also required the value to work on end of each case.
#If you were to expand the event types in a large way it might be advised to put this in another file and import it.
#Thankfully the keyboard and mouse handler should eliminate a need for some of them.
class SDL_Events(Enum):
    SDL_KEYDOWN = SDL_KEYDOWN
    SDL_KEYUP = SDL_KEYUP
    SDL_QUIT = SDL_QUIT
    SDL_WINDOWEVENT = SDL_WINDOWEVENT
    SDL_MOUSEMOTION = SDL_MOUSEMOTION
    SDL_MOUSEBUTTONDOWN = SDL_MOUSEBUTTONDOWN
    SDL_MOUSEBUTTONUP = SDL_MOUSEBUTTONUP
    
class SDL_Keys(Enum):
    SDLK_F1 = SDLK_F1

def event_handler(self):
    while sdl2.SDL_PollEvent(self.event):
        match self.event.type:
            case SDL_Events.SDL_QUIT.value:
                self.run = 0

            case SDL_Events.SDL_WINDOWEVENT.value:
                if self.event.window.event == SDL_WINDOWEVENT_RESIZED or self.event.window.event == SDL_WINDOWEVENT_SIZE_CHANGED:
                    gui_resize(self)

            case SDL_Events.SDL_KEYDOWN.value:
                print("Key Down")
                self.kbh.set_state(self.event.key.keysym.sym,1)

            case SDL_Events.SDL_KEYUP.value:
                match self.event.key.keysym.sym:
                    case SDL_Keys.SDLK_F1.value:
                        self.full_screen = (not self.full_screen)
                        if self.full_screen:
                            SDL_SetWindowFullscreen(self.window,SDL_WINDOW_SHOWN|SDL_WINDOW_FULLSCREEN_DESKTOP)
                            self.swap_w = self.width
                            self.swap_h = self.height
                        else:
                            SDL_SetWindowFullscreen(self.window,SDL_WINDOW_SHOWN|SDL_WINDOW_RESIZABLE)
                            SDL_SetWindowResizable(self.window,SDL_TRUE)
                            self.width = self.swap_w
                            self.height = self.swap_h
                            SDL_SetWindowSize(self.window,self.width,self.height); 
                self.kbh.set_state(self.event.key.keysym.sym,0)
                
            case SDL_Events.SDL_MOUSEMOTION.value:
                self.mh.move_update()
            case SDL_Events.SDL_MOUSEBUTTONDOWN.value:
                self.mh.set_state(self.event.button.button-1,SDL_PRESSED)
            case SDL_Events.SDL_MOUSEBUTTONUP.value:
                self.mh.set_state(self.event.button.button-1,SDL_RELEASED)
    return