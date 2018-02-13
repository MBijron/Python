# coding=utf-8
from fineworks.udl.lexers.lexer_base import LexerBase
from fineworks.udl.tokens.class_token import ClassToken
from pyworks.utils.regex import Regex


class ContentsLexer(LexerBase):
    _regex = r"^(CONTENTS)(\s+[-]+\s+[A-Za-z_]+)+$"
    _token = None

    def __init__(self):
        self.set_requested_component_nr(-1)

    def matches(self, components: []):
        biggest_match = None
        used_components = 0
        mismatch_nr = 0
        for i in range(0, len(components), 1):
            if mismatch_nr > 3:
                break
            component = ' '.join(components[0:i])
            if Regex.match_string(component, self._regex):
                mismatch_nr = 0
                biggest_match = component
                used_components = i
            else:
                mismatch_nr += 1
        if biggest_match:
            self.create_token(biggest_match, used_components)
            return True
        return False

    def create_token(self, component, components_used):
        self.set_token(ClassToken(0, components_used, "CONTENTS", component))