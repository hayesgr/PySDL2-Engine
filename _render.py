import sdl2

#renderer

def intro_r(self):
    #self.window.blit(self.scaled_background,(0,0))
    #print("Render Intro",self.AM.image_index("title"),self.AM.assets[self.bg].rect)
    sdl2.SDL_RenderCopy(self.renderer,self.AM.assets[self.AM.image_index("title")].image,None,self.screen_rect)
    return

def menu_r(self):
    #self.window.fill((0,0,255))
    return

def options_r(self):
    return

def play_r(self):
    for b in self.balls:

        sdl2.SDL_RenderCopy(self.renderer,self.AM.assets[b.color].image,None,b.b_rect)
        #self.window.blit(self.images[b.color],(b.x-32,b.y-32))
        #self.window.blit(self.AM.assets[b.color],(b.x-32,b.y-32))
    return

def credits_r(self):
    return

def end_r(self):
    return
switch_r = {"intro":intro_r,"menu":menu_r,"options":options_r,"play":play_r,"credits":credits_r,"end":end_r}
def render(self):
    sdl2.SDL_RenderClear(self.renderer)
    sdl2.SDL_SetRenderDrawColor(self.renderer,0,0,0,255)
    r = switch_r.get(self.game_state)
    if r:
        r(self)
    sdl2.SDL_RenderPresent(self.renderer)
    #pygame.display.update()
    return

