import sdl2

class Keyboard_Handler:
    
    def __init__(self):
        self.key_state = []
        self.clicked = []
        for x in range(0,255):
            self.key_state.append(0)
            self.clicked.append(0)
        return

    def set_state(self,key,state):
        self.key_state[key%256]=state
        self.clicked[key%256] = 1*(state==1)

    def is_pressed(self,key):
        return self.key_state[key%256]

    def was_clicked(self,key):
        return self.clicked[key%256]

    def reset_clicked(self,key):
        self.clicked[key%256]=0

    
    #Example use
    #if self.kbh.is_pressed(pygame.K_p):
    #    print("p is pressed")
    #if self.kbh.was_clicked(pygame.K_p):
    #    print("p was clicked")
    #    self.kbh.reset_clicked(pygame.K_p)
    