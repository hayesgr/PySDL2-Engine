This is a game Engine built around pySDL2

You will need to install pysdl2 to make use of the engine as it is. See pysdl2s documentation on that for your system

F1 lets you toggle full screen mode. The screen is otherwise resizable

The engine is a work in progress. The engine is being modeled after my C++ Engine. The engine is Object orientated and state machine based. In place of switch statements a dictionary is used to call functions based on the game_state The event handler is also done in a state based way.
I first tried converting using pygame. Pygame is less than 1/3rd the performance of pySDL2. That is because you don't have access to hardware exceleration and textures.
SDL2 textures are different from SDL surfaces in that they are buffered objects. See SDL2 documentation on that.

Pygame has better support for playing movies, and sound files. Less so for storing music your option there is play it from source.
Not sure why they didn't do movies the same way if they really were just trying to conserve memory as the documentation suggests.
pySDL2 documentation is lacking when it comes to mixer/audio and there isn't any direct support for movies.

The state system means avoiding large number of if else statements that kill performance.

There is a keyboard and mouse handler built in. This gives access to key and mouse actions you can carry into the update section. Example: code for using them is in comments at the bottom of each perspective file.

There is an asset manager built in. The demo shows how it is used in place of standard methods. Transformations and scaling of images should only be done based on event changes. Example: if you rotate a ship based on a key being pressed. Use the keyboard handler to detect the key press in the update function. Then make the scale or rotation change in the update area. Never make rotation changes in the renderer. Only keys that apply regardless of what screen you are in should be handled inside the envent function. All other keys should be handled using the keyboard handler in the update area. The same goes for mouse.

There is a proper game timer built in that does not use pysdl2s. The timer has microsecond time. Example use of it is in the demo for updating the ball movement.

