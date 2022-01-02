from sdl2 import *
import sdl2.ext
from sdl2.sdlmixer import *
from sdl2.surface import *
from sdl2.sdlimage import *

import random
import _balls


def load_content(self):
    #load content here initialy
    
    self.AM.load_image("rCircle","CircleR.png")
    self.AM.load_image("gCircle","CircleG.png")
    self.AM.load_image("bCircle","CircleB.png")
    self.AM.load_image("yCircle","CircleY.png")
    self.AM.load_image("pCircle","CircleP.png")
    self.bg = self.AM.load_image("title","title.png")
    self.AM.load_image("black","black.png")
    #self.AM.load_sound("t_sound","test.wav")
    #self.AM.play_sound("t_sound")
    #self.AM.load_music("t_music","test.mp3")
    #self.AM.play_music("t_music")
    
    random.seed(100)
    ball_count = 3200
    for i in range(0,ball_count):
        x = random.randint(50,300)
        y = random.randint(50,300)
        vx = random.randint(-400,400)
        vy = random.randint(-0,400)
        color = random.randint(0,4)
        b = _balls.Ball(x,y,vx,vy,color)
        self.balls.append(b)

    self.gt.set_timer()
    self.game_state = "intro"
    return