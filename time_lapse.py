import cv2
import os
import time
import math

class TimeLapse(object):
    def __init__(self):
        self.interval = 0
        self.next_time = 0
        self.name = "TIME LAPSE DURATION"
        self.type = "real"

    def get(self):
        return self.interval

    def set(self,i):
        self.interval = i;
        self.set_next_time();

    def set_next_time(self):
        self.next_time = time.time() + self.get_interval()

    def get_interval(self):
        return math.floor(self.interval * 10)

    def should_capture(self):
        if (self.get_interval() > 0 and
            time.time() > self.next_time):
            self.set_next_time()
            return True
