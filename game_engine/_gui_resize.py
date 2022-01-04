from sdl2 import *
import sdl2.ext
from sdl2.sdlmixer import *
from sdl2.surface import *
from sdl2.sdlimage import *

from ctypes import *

def gui_resize(self):
    w = c_int()
    h = c_int()
    SDL_GetRendererOutputSize(self.renderer,w,h)
    self.width = w.value
    self.height = h.value
    self.screen_rect.w = self.width
    self.screen_rect.h = self.height