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

class Sound:
    def __init__(self,sound=None):
        self.sound = sound
        return
    def cleanup(self):
        Mix_HaltChannel(-1) #makes sure no sound is being played
        Mix_FreeChunk(self.sound)
        return

class Music:
    def __init__(self,music=None):
        self.music = music
        return
    def cleanup(self):
        Mix_HaltMusic() #makes sure music is stopped
        Mix_FreeMusic(self.music)
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
        for x in self.assets:
            x.cleanup()
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
        fn = "assets/" + file_name
        snd = Sound(Mix_LoadWAV(fn.encode()))
        self.assets.append(snd)
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

    def remove_sound(self,name):                #should not be called while any sound is playing.
        self.assets[self.sounds.get(name)].cleanup()    
        self.assets.pop(self.sounds.get(name))
        self.sounds.pop(name)
        return

    def play_sound(self,name):
        r = self.sounds.get(name)
        if r:
            Mix_PlayChannel(-1,self.assets[r].sound,1)
        else:
            print("Sound: " + name + "doesn't exist")
        return
    #Music
    def load_music(self,name,file_name):
        fn = "assets/" + file_name
        ms = Music(Mix_LoadMUS(fn.encode()))
        self.assets.append(ms)
        index = len(self.assets)-1
        self.music[name]=index
        return index

    def get_music(self,name):
        r = self.music.get(name)
        if r:
            return self.assets[r]
        print("Sound: " + name + "doesn't exist")
        return

    def music_index(self,name):
        return self.music.get(name)    #will return Null if doesn't exist. Address out of range issue will usually occur

    def remove_music(self,name):                #should not be called while any music is playing.
        self.assets[self.music.get(name)].cleanup()
        self.assets.pop(self.music.get(name))
        self.sounds.pop(name)
        return

    def play_music(self,name):
        r = self.music.get(name)
        if r:
            Mix_PlayMusic(self.assets[r].music,1)
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
    

    