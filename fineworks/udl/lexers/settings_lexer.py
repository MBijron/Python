# coding=utf-8
from fineworks.udl.lexers.lexer_base import LexerBase
from fineworks.udl.tokens.setting_token import SettingToken
from pyworks.utils.regex import Regex


class SettingsLexer(LexerBase):
    _regex = r"^!([\w_]+)(?:=([\S]+))?$"
    _token = None

    def matches(self, components: []) -> bool:
        if Regex.match_string(components[0], self._regex):
            self.create_token(components[0])
            return True
        return False

    def create_token(self, component) -> None:
        values = Regex.find_in_string(component, self._regex)
        self.set_token(SettingToken(0, 1, values[0], values[1] if values[1] else "true"))
