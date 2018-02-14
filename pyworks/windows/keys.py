import win32api


class Keys:
    # noinspection PyProtectedMember
    @staticmethod
    def send_key(key_code) -> None:
        hwcode = win32api.MapVirtualKey(key_code._value_, 0)
        win32api.keybd_event(key_code._value_, hwcode)
