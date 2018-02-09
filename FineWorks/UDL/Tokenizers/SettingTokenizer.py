# coding=utf-8
from FineWorks.UDL.Tokenizers.TokenizerBase import TokenizerBase
from FineWorks.UDL.Tokens import SettingToken
from PyWorks.Utils import Regex


class SettingTokenizer(TokenizerBase):
    _regex = r"^!([\w_]+)(?:=([\S]+))?$"
    _token = None

    def matches(self, components: []):
        if Regex.match_string(components[0], self._regex):
            self.create_token(components[0])
            return True
        return False

    def create_token(self, component):
        values = Regex.find_in_string(component, self._regex)
        self.set_token(SettingToken(0, 1, values[0], values[1] if values[1] else "true"))
