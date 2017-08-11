from winreg import *
import os, sys, win32gui, win32con

class Environment:

    @staticmethod
    def query_value(key, name):
        value, type_id = QueryValueEx(key, name)
        return value

    @staticmethod
    def get_environment_variable(name):
        path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        key = OpenKey(reg, path, 0, KEY_ALL_ACCESS)
        for i in range(1024):
            try:
                n, v, t = EnumValue(key, i)
                if (n.lower() == name.lower()):
                    return v
            except EnvironmentError:
                break
        raise Exception("The environment variable was not found")

    @staticmethod
    def environment_variable_exists(name):
        path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        key = OpenKey(reg, path, 0, KEY_ALL_ACCESS)
        for i in range(1024):
            try:
                n, v, t = EnumValue(key, i)
                if(n.lower() == name.lower()):
                    return True
            except EnvironmentError:
                break
        return False

    @staticmethod
    def set_environment_variable(name, value):
        path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        key = OpenKey(reg, path, 0, KEY_ALL_ACCESS)

        if value:
            SetValueEx(key, name, 0, REG_EXPAND_SZ, value)
        else:
            DeleteValue(key, name)

        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')

        CloseKey(key)
        CloseKey(reg)