import cv2


class BasicCamSetting(object):

    def __init__(self, cap, var):
        self.type = 'real'
        self.cap = cap
        self.var = var
        self.name = ""

    def set(self, val):
        self.cap.set(self.var, val)

    def get(self):
        return self.cap.get(self.var)


class BrightnessSetting(BasicCamSetting):
    def __init__(self, cap):
        super(self.__class__, self).__init__(cap, cv2.cv.CV_CAP_PROP_BRIGHTNESS)
        self.name = "BRIGHTNESS"

class ContrastSetting(BasicCamSetting):
    def __init__(self, cap):
        super(self.__class__, self).__init__(cap, cv2.cv.CV_CAP_PROP_CONTRAST)
        self.name = "CONTRAST"

class SaturationSetting(BasicCamSetting):
    def __init__(self, cap):
        super(self.__class__, self).__init__(cap, cv2.cv.CV_CAP_PROP_SATURATION)
        self.name = "SATURATION"

class HueSetting(BasicCamSetting):
    def __init__(self, cap):
        super(self.__class__, self).__init__(cap, cv2.cv.CV_CAP_PROP_HUE)
        self.name = "HUE"

        


