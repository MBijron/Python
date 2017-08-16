import win32api


class Keys:
    @staticmethod
    def sendkey(keycode):
        hwcode = win32api.MapVirtualKey(keycode._value_, 0)
        win32api.keybd_event(keycode._value_, hwcode)