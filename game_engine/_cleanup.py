from sdl2 import *
import sdl2.ext
from sdl2.sdlmixer import *
from sdl2.surface import *
from sdl2.sdlimage import *


def cleanup(self):
    print("cleaning up")
    self.AM.cleanup()
    Mix_CloseAudio()
    SDL_DestroyRenderer(self.renderer)
    SDL_DestroyWindow(self.window)
    return