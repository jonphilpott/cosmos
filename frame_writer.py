import cv2
import os
import shutil
import time
import threading
import Queue

class FrameWriterThread(threading.Thread):
    def __init__(self, q, path, tmp_path):
        threading.Thread.__init__(self)
        self.q = q
        self.path = path
	self.tmp_path = tmp_path

    def run(self):
        while True:
            frame = self.q.get()
            cv2.imwrite(self.tmp_path, frame)
	    os.rename(self.tmp_path, self.path)
            self.q.task_done()

class FrameWriter(object):

    def __init__(self, filename):
        self.path = "/run/shm/%s.png" % filename
        self.tmp_path = "/run/shm/%s.tmp.png" % filename
        self.last = time.time();
        self.q = Queue.Queue()
        self.thread = FrameWriterThread(self.q, self.path, self.tmp_path)
        self.thread.setDaemon(True)
        self.thread.start()
        self.name = "SAVE IMAGES?"
        self.type = "bool"
        self.run = True


    def get(self):
        return self.run

    def set(self, val):
        self.run = val
    

    def process(self, frame):
        if self.run:
            now = time.time()
            if (int(self.last) < int(now)):
                self.q.put(frame)
                self.last = now
        return frame
