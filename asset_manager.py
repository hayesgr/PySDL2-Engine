from os import path
import sys
from sdl2 import *
import sdl2.ext
from sdl2.surface import *
from sdl2.sdlimage import *
from sdl2.sdlmixer import *
from ctypes import *
#The asset manager allows using store assets by their names
#You can access assets by name or by index
#Calling assets by name may be useful for visual novels or when a lot of assets exit and you can't remember the index location

class Texture:
    def __init__(self,image=None,rect=(0,0,0,0)):
        self.image = image
        self.rect = rect
        return
    def cleanup(self):
        SDL_DestroyTexture(self.image)
        return

class Asset_Manager:
    def __init__(self,renderer):
        self.assets = []
        self.images = {}
        self.videos = {}
        self.music = {}
        self.sounds = {}
        self.renderer = renderer
        return

    def cleanup(self):

        return

    #images
    def load_image(self,name,file_name):
        s = "assets/" + file_name
        tex = sdl2.ext.load_image(s.encode())
        i = SDL_CreateTextureFromSurface(self.renderer,tex)
        if not i:
            print ("Failed to load Image:",s)
        SDL_FreeSurface(tex)
        tw = c_int()
        th = c_int()
        SDL_QueryTexture(i,None,None,tw,th)
        tr = SDL_Rect(0,0,tw,th)
        t = Texture(i,tr)
        self.assets.append(t)
        index = len(self.assets)-1
        self.images[name]=index
        return index

    def get_image(self,name):
        r = self.images.get(name)
        if r:
            return self.assets[r]
        print("Image: " + name + "doesn't exist")
        return 

    def image_index(self,name):
        return self.images.get(name)    #will return Null if doesn't exist. Address out of range issue will usually occur

    def remove_image(self,name):
        self.assets.pop(self.images.get(name))
        self.images.pop(name)
        return
    
    #sounds
    def load_sound(self,name,file_name):
        #Need to change to SDL
        self.assets.append(Mix_LoadWAV("assets/" + file_name))
        index = len(self.assets)-1
        self.sounds[name]=index
        return index

    def get_sound(self,name):
        r = self.sounds.get(name)
        if r:
            return self.assets[r]
        print("Sound: " + name + "doesn't exist")
        return

    def sound_index(self,name):
        return self.sounds.get(name)    #will return Null if doesn't exist. Address out of range issue will usually occur

    def remove_sound(self,name):
        self.assets.pop(self.sounds.get(name))
        self.sounds.pop(name)
        return

    def play_sound(self,name):
        r = self.sounds.get(name)
        if r:
            Mix_PlayChannel(-1,r,1)
        else:
            print("Sound: " + name + "doesn't exist")
        return
    #Music
    def load_music(self,name,file_name):
        #Need to change to SDL
        self.assets.append(Mix_LoadMUS("assets/" + file_name))
        index = len(self.assets)-1
        self.sounds[name]=index
        return index

    def get_music(self,name):
        r = self.sounds.get(name)
        if r:
            return self.assets[r]
        print("Sound: " + name + "doesn't exist")
        return

    def music_index(self,name):
        return self.sounds.get(name)    #will return Null if doesn't exist. Address out of range issue will usually occur

    def remove_music(self,name):
        self.assets.pop(self.sounds.get(name))
        self.sounds.pop(name)
        return

    def play_music(self,name):
        r = self.sounds.get(name)
        if r:
            Mix_PlayMusic(r,1)
        else:
            print("Sound: " + name + "doesn't exist")
        return
    
    def pause_music(self):
        Mix_PauseMusic()
        return
    def resume_music(self):
        Mix_ResumeMusic()
        return
    def rewind_music(self):
        Mix_RewindMusic()
        return
    def halt_music(self):
        Mix_HaltMusic()
        return
    

    