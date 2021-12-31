import sdl2

#this is where all updates are done


def intro_u(self):
    if self.gt.elapsed_time()>3000000:
        self.gt.set_timer()
        self.game_state = "play"
        #change background
        self.bg = self.AM.image_index("black")
    return

def menu_u(self):
        #main menu 
    return

def options_u(self):
        #options menu
    return

def play_u(self):
    t = self.gt.elapsed_time()
    #if self.fps_trap==10:
    #    print("fps:",1000000/t)
    #    self.fps_trap=0
    #self.fps_trap += 1
    self.gt.set_timer()
    for i in self.balls:
        i.update(self.width,self.height,t)
    return

def credits_u(self):
        #Credits
    return

def end_u(self):
    return

switch_u = {"intro":intro_u,"menu":menu_u,"options":options_u,"play":play_u,"credits":credits_u,"end":end_u}
def update(self):
    #Where nested code used to be.
    r = switch_u.get(self.game_state)
    if r:
        r(self)
    return