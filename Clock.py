import time
import sys


class Clock:
    """ time is always in hours """

    def __init__(self, t):
        self.time_in_seconds = t * 60 * 60
        self.elapsed_time_in_hours = 0
        self.elapsed_time_in_minutes = 0
        self.elapsed_time_in_seconds = 0
        self.pause_elapsed_time_in_hours = 0
        self.pause_elapsed_time_in_minutes = 0
        self.pause_elapsed_time_in_seconds = 0
        self.current_time = 0
        self.elapsed_time = 0
        """ pause time always in minutes """
        self.pause_time = 60 * 60
        self.pause_rest_time = 25 * 60
        """ TODO: Delete this when finished """
        self.time_speed = 200

    def pause_clock(self, t):
        time.sleep(t)

    def start_clock(self):
        while self.current_time <= self.time_in_seconds:
            print(self.elapsed_time_in_hours, ":",
                  self.elapsed_time_in_minutes, ":", self.elapsed_time_in_seconds)
            self.elapsed_time_in_seconds += 1
            self.elapsed_time += 1
            self.current_time += 1
            time.sleep(1/self.time_speed)
            if(self.elapsed_time % 60 == 0):
                self.elapsed_time_in_seconds = 0
                self.elapsed_time_in_minutes += 1
            if(self.elapsed_time % 3600 == 0):
                self.elapsed_time_in_minutes = 0
                self.elapsed_time_in_hours += 1
            if((self.elapsed_time % self.pause_time == 0) and self.elapsed_time < self.time_in_seconds):
                print("--BREAK start--")
                pause_elapsed_time = 0
                self.pause_elapsed_time_in_hours = 0
                self.pause_elapsed_time_in_minutes = 0
                self.pause_elapsed_time_in_seconds = 0
                while pause_elapsed_time <= self.pause_rest_time:
                    print(self.pause_elapsed_time_in_hours, ":",
                          self.pause_elapsed_time_in_minutes, ":", self.pause_elapsed_time_in_seconds)
                    self.pause_elapsed_time_in_seconds += 1
                    pause_elapsed_time += 1
                    self.current_time += 1
                    time.sleep(1/self.time_speed)
                    if(pause_elapsed_time % 60 == 0 and pause_elapsed_time != 0):
                        self.pause_elapsed_time_in_seconds = 0
                        self.pause_elapsed_time_in_minutes += 1
                    if(pause_elapsed_time % 3600 == 0 and pause_elapsed_time != 0):
                        self.pause_elapsed_time_in_minutes = 0
                        self.pause_elapsed_time_in_hours += 1
                print("--BREAK end--")
        print("-- Terminaron la(s) ", self.time_in_seconds /
              60/60, " hora(s) de trabajo --")


clock = Clock(2)
clock.start_clock()
