import time
import sys


class Clock:
    def __init__(self, t):
        self.time = t * 60
        self.current_time = 0
        self.elapsed_time = 0
        self.pause_time = 1 * 60
        """ TODO: Delete this when finished """
        self.time_speed = 20

    def pause_clock(self, t):
        time.sleep(t)

    def start_clock(self):
        while self.current_time <= self.time:
            print(self.elapsed_time)
            self.elapsed_time += 1
            self.current_time += 1
            time.sleep(1/self.time_speed)
            if((self.elapsed_time % self.pause_time == 0)):
                print("--BREAK start--")
                pause_elapsed_time = 0
                while pause_elapsed_time <= self.pause_time:
                    print(pause_elapsed_time)
                    time.sleep(1/self.time_speed)
                    pause_elapsed_time += 1
                    self.current_time += 1
                print("--BREAK end--")


clock = Clock(30)
clock.start_clock()
