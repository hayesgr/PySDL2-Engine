import sdl2
from _gui_resize import gui_resize

def quit(self):
    self.run = 0
    return

def window_event(self):
    if self.event.window.event == sdl2.SDL_WINDOWEVENT_RESIZED or self.event.window.event == sdl2.SDL_WINDOWEVENT_SIZE_CHANGED:
        gui_resize(self)
    return

def mouse_move(self):
    self.mh.move_update()
    return
def mouse_button_up(self):
    self.mh.set_state(self.event.button.button-1,sdl2.SDL_RELEASED)

    return
def mouse_button_down(self):
    self.mh.set_state(self.event.button.button-1,sdl2.SDL_PRESSED)
    return

#Only Keys that should effect every screen should be handled in here.
#All Other keys should make use of the keyboard_handler
def key_down(self):
    self.kbh.set_state(self.event.key.keysym.sym,1)
    return

def f1(self):
    self.full_screen = (not self.full_screen)
    if self.full_screen:
        sdl2.SDL_SetWindowFullscreen(self.window,sdl2.SDL_WINDOW_SHOWN|sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP)
        self.swap_w = self.width
        self.swap_h = self.height
        
    else:
        sdl2.SDL_SetWindowFullscreen(self.window,sdl2.SDL_WINDOW_SHOWN|sdl2.SDL_WINDOW_RESIZABLE)
        sdl2.SDL_SetWindowResizable(self.window,sdl2.SDL_TRUE)
        self.width = self.swap_w
        self.height = self.swap_h
        sdl2.SDL_SetWindowSize(self.window,self.width,self.height);
        
    return
key_switch = {sdl2.SDLK_F1:f1}

def key_up(self):
    rs = key_switch.get(self.event.key.keysym.sym)#event.key)
    if rs:
        rs(self)
    self.kbh.set_state(self.event.key.keysym.sym,0)
    return

switch = {sdl2.SDL_QUIT:quit,sdl2.SDL_WINDOWEVENT:window_event,sdl2.SDL_KEYDOWN:key_down,sdl2.SDL_KEYUP:key_up,sdl2.SDL_MOUSEMOTION:mouse_move,
    sdl2.SDL_MOUSEBUTTONDOWN:mouse_button_down,sdl2.SDL_MOUSEBUTTONUP:mouse_button_up}

def event_handler(self):
    #for event in pygame.event.get():
    while sdl2.SDL_PollEvent(self.event):
        self.event_holder = self.event
        r = switch.get(self.event.type)
        if r:
            r(self)