import time

class gesture_response:
    def __init__(self, cam):
        
        self.busy_state = False
        self.cam = cam

    # processes gesture and confidence level
    def gesture_action(self, gesture):
        self.gesture = gesture
        if not self.busy_state:
            self.delay_capture()

    # function for delaying image capture
    def delay_capture(self):
        self.busy_state = True
        print("Picture taking in ",int(self.gesture))
        for i in range(1, self.gesture):
            time.sleep(1)
            print(str(int(self.gesture)-i))
        # capture_image(insert image capture function)       
        self.cam.capture_file("../images/{}.jpeg".format(int(time.time())))
        self.busy_state = False
