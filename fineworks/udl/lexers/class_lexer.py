# coding=utf-8
from fineworks.udl.lexers import LexerBase
from fineworks.udl.tokens import ClassToken
from pyworks.utils import Regex


class ClassLexer(LexerBase):
    _regex = r"^([A-Z_]{2,})(?<!:)(?:\s+-\s+([\S]+))?:?$"
    _token = None

    def __init__(self):
        self.set_requested_component_nr(3)

    def matches(self, components: []):
        for i in range(len(components), 0, -1):
            component = ' '.join(components[0:i])
            if Regex.match_string(component, self._regex):
                self.create_token(component, i)
                return True
        return False

    def create_token(self, component, components_used):
        values = Regex.find_in_string(component, self._regex)
        self.set_token(ClassToken(0, components_used, values[0], values[1]))