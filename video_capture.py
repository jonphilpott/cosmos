import numpy as np
import cv2


class Capture(object):

    def start(self):
        self.cap = cv2.VideoCapture(0)
	return self.cap

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame

    def end(self):
        self.cap.release();

    def get(self, var):
        return self.cap.get(var)

    def set(self, var, val):
        self.cap.set(var, val)
