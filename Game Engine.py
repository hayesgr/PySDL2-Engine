import sdl2
import sdl2.ext
from _eventhandler import event_handler
from _load_content import load_content
from _update import update
from _render import render
from _cleanup import cleanup
from _timer import Timer
from keyboard_handler import Keyboard_Handler
from mouse_handler import Mouse_Handler
from asset_manager import Asset_Manager
from _profile import profile
PROFILE = True          #Set to true to profile game, false to not profile game
TITLE = "Game Engine"


class Game:
    def __init__(self,width,height,title):
        self.title = title.encode()
        self.game_state = "intro"
        self.full_screen = 0
        self.screen_w = 1920    #Monitor width
        self.screen_h = 1080    #Monitor height
        self.screen_rect = sdl2.SDL_Rect(0,0,width,height)
        self.event_holder = None   #holds events to share across engine
        self.run = 1   
        self.swap_w = 0         #for swapping from FS to window
        self.swap_h = 0         #for swapping from FS to window
        self.width = width
        self.height = height

        sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
        self.event = sdl2.SDL_Event()
        #SDL_WINDOW_SHOW| SDL_WINDOW_FULLSCREEN_DESKTOP | SDL_WINDOW_RESIZABLE
        self.window = sdl2.SDL_CreateWindow(self.title,sdl2.SDL_WINDOWPOS_CENTERED,sdl2.SDL_WINDOWPOS_CENTERED,width,height,(sdl2.SDL_WINDOW_SHOWN | sdl2.SDL_WINDOW_RESIZABLE))
        self.renderer = sdl2.SDL_CreateRenderer(self.window,-1,sdl2.SDL_RENDERER_ACCELERATED)
        
        self.gt = Timer()       #game timer
        self.kbh = Keyboard_Handler()
        self.mh = Mouse_Handler()
        self.AM = Asset_Manager(self.renderer)
        
        
        #game content
        self.balls = []                 #list of balls
        self.bg = 0                     #determines what background is in use
        self.fps_trap = 0


    def main_loop(self):
        load_content(self)
        event = sdl2.SDL_Event()
        while self.run:
            event_handler(self)
            #if sdl2.SDL_PollEvent(event) !=0:
            #    if event.type == sdl2.SDL_QUIT:
            #        self.run = 0
            #    if event.type == sdl2.SDL_KEYDOWN:
            #        if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
            #            self.run = 0
            update(self)
            render(self)
        cleanup(self)
        return

def main():
    g = Game(960,540,TITLE)
    g.main_loop()
    sdl2.SDL_Quit()
    return

if not PROFILE:
    if __name__ == "__main__":
        main()
else:
    profile()