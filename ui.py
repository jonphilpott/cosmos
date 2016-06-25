import cv2
import numpy as np

UI_COLOR = (128, 128, 128)

class UI(object):
    
    def __init__(self, cap):
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.cap  = cap
        self.state = 'running'
        self.uis = []
        self.ui_idx = 0
        self.show_ui = False

    def add_ui(self, ui):
        self.uis.append(ui)

    def keep_running(self):
        return (self.state != 'stop')

    def check_keys(self):
        key = cv2.waitKey(1)
        plain_key = key & 0xFF
        cur = self.get_current_ui()

        if (plain_key == ord('q')):
            self.state = 'stop'

            
        if (self.show_ui and (key == 65361 or key == 65363)):
            if cur.type == 'real':
                b = cur.get();
                incr = 0.1
                if (key == 65361):
                    incr = -0.1
                b = (b + incr) % 1
                cur.set(b)
            elif cur.type == 'bool':
                cur.set(not cur.get())
                
                
        if (self.show_ui and key == 65364):
            self.ui_idx = (self.ui_idx + 1) % len(self.uis)

        if (self.show_ui and key == 65362):
            self.ui_idx = (self.ui_idx - 1) % len(self.uis)

                
        if (plain_key == ord(' ')):
            self.show_ui = not self.show_ui
            
        return key

    def get_current_ui(self):
        return self.uis[self.ui_idx]

    def draw(self, frame):
        if self.show_ui:
            cur = self.get_current_ui()
            val = cur.get()
            cv2.putText(frame, cur.name,(10,240), self.font, 1,UI_COLOR,2)
            if cur.type == 'real':
                cv2.line(frame, (30, 300), (30 + int(val * 500), 300), UI_COLOR, 20)
            elif cur.type == 'bool':
                cv2.putText(frame, "ON" if val else "OFF", (10,300), self.font, 1, UI_COLOR,2)
