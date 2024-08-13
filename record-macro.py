import pyautogui


# Class to record new macros
class Recorder:
    def __init__(self):
        self.cur_mouse_x, self.cur_mouse_y = pyautogui.position()

