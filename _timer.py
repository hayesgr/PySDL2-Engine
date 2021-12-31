import time

class Timer:
    #ticks = 0 #microseconds
    def __init__(self):
        self.ticks = int(round(time.time() * 1000000))
    def set_timer(self):
        self.ticks = int(round(time.time() * 1000000))
    def elapsed_time(self):
        return int(round(time.time() * 1000000)) - self.ticks 