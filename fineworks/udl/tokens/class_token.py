from fineworks.udl.tokens import TokenBase
from fineworks.udl.tokens import TokenType


class ClassToken(TokenBase):
    _type = TokenType.CLASS
    _data: str

    def __init__(self, identifier: int, components_used: int, name: str, data: str):
        super().__init__(identifier, components_used, name)
        self._data = data

