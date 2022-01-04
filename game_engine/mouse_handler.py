from sdl2 import *
from ctypes import *

class Mouse_Handler:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.old_x = 0
        self.old_y = 0
        self.num_buttons = 5
        self.b_state = []
        self.b_clicked = []
        for x in range(0,self.num_buttons):
            self.b_state.append(0)
            self.b_clicked.append(0)
        return

    def move_update(self):
        self.old_x,self.old_y = self.x,self.y
        x = c_int()
        y = c_int()
        SDL_GetMouseState(x,y)
        self.x = x
        self.y = y
        return

    def set_state(self,b,state):
        self.b_state[b] = state
        self.b_clicked[b] = 1*(self.b_state[b]==1)
        return

    def is_pressed(self,Button):
        return self.b_state[Button]

    def was_clicked(self,Button):
        return self.b_clicked[Button]

    def reset_clicked(self,Button):
        self.b_clicked[Button]=0

    #Example Use
    #if self.mh.is_pressed(0):
    #    print("Button 0 pressed")
    #if self.mh.was_clicked(0):
    #    print("Button 0 was clicked")
    #    self.mh.reset_clicked(0)