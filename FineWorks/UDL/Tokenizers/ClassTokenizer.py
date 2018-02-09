# coding=utf-8
from FineWorks.UDL.Tokenizers import TokenizerBase
from FineWorks.UDL.Tokens import ClassToken
from PyWorks.Utils import Regex


class ClassTokenizer(TokenizerBase):
    _regex = r"^([A-Z_]+)(?<!:)(?:-([\S]+))?:?$"
    _token = None

    def __init__(self):
        self.set_requested_component_nr(3)

    def matches(self, components: []):
        for i in range(len(components), 1, -1):
            component = ''.join(components[0:i])
            if Regex.match_string(component, self._regex):
                self.create_token(component)
                return True
        return False

    def create_token(self, component):
        values = Regex.find_in_string(component, self._regex)
        self.set_token(ClassToken(0, values[0], values[1]))