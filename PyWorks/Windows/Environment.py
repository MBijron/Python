import os
import win32con
import win32gui
from winreg import *


class Environment:

    @staticmethod
    def get_environment_variable(name):
        path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        key = OpenKey(reg, path, 0, KEY_ALL_ACCESS)
        for i in range(1024):
            try:
                n, v, t = EnumValue(key, i)
                if n.lower() == name.lower():
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
                if n.lower() == name.lower():
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

        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')

        CloseKey(key)
        CloseKey(reg)

    @staticmethod
    def delete_environment_variable(name):
        path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        key = OpenKey(reg, path, 0, KEY_ALL_ACCESS)

        DeleteValue(key, name)

        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')

        CloseKey(key)
        CloseKey(reg)

    @staticmethod
    def expand_variables(string):
        return os.path.expandvars(string)
