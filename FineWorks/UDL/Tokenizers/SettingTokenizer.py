# coding=utf-8
from PyWorks.Utils import Regex

class SettingTokenizer:
    _regex = r"^![\w_]+(\([\w\d_]+\))?$"

    @staticmethod
    def matches(component):
        return Regex.match_string(component, SettingTokenizer._regex)

    @staticmethod
    def get_token(component):
        return {}
