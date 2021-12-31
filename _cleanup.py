import sdl2

def cleanup(self):
    sdl2.SDL_DestroyRenderer(self.renderer)
    sdl2.SDL_DestroyWindow(self.window)
    return