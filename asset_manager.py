import sdl2
from sdl2 import rect
import sdl2.ext
from sdl2.surface import SDL_LoadBMP
from sdl2.sdlimage import *
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
        sdl2.SDL_DestroyTexture(self.image)
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
        #self.assets.append((pygame.image.load("assets/" + file_name).convert_alpha()))
        s = "assets/" + file_name
        tex = sdl2.ext.load_image(s.encode())
        #surf = sdl2.SDL_LoadBMP(s.encode())
        i = sdl2.SDL_CreateTextureFromSurface(self.renderer,tex)
        if not i:
            print ("Failed to load Image:",s)
        #sdl2.SDL_FreeSurface(surf)
        tw = c_int()
        th = c_int()
        sdl2.SDL_QueryTexture(i,None,None,tw,th)
        tr = sdl2.SDL_Rect(0,0,tw,th)
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
    #movies
    def load_movie(self,name,file_name):
        #need to change to SDL
        #self.assets.append((pygame.movie.Movie("assets/"+ file_name)))
        index = len(self.assets)-1
        self.videos[name]=index
        return index

    def get_movie(self,name):
        r = self.videos.get(name)
        if r:
            return self.assets[r]
        print("Movie: " + name + "doesn't exist")
        return

    def movie_index(self,name):
        return self.videos.get(name)    #will return Null if doesn't exist. Address out of range issue will usually occur

    def remove_movie(self,name):
        self.assets.pop(self.videos.get(name))
        self.videos.pop(name)
        return
    #sounds
    def load_sound(self,name,file_name):
        #Need to change to SDL
        #self.assets.append(pygame.mixer.Sound("assets/" + file_name))
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

    #pygame doesn't load music into an object just memory
    #So all that can be stored is the file name
    #That can be stored directly in the dictionary and doesn't need the asset array
    #


    