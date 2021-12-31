import sdl2
from ctypes import *

def gui_resize(self):
    w = c_int()
    h = c_int()
    sdl2.SDL_GetRendererOutputSize(self.renderer,w,h)
    self.width = w.value
    self.height = h.value
    self.screen_rect.w = self.width
    self.screen_rect.h = self.height