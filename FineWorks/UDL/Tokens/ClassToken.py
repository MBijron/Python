from FineWorks.UDL.Tokens import TokenBase
from FineWorks.UDL.Tokens.TokenType import TokenType


class ClassToken(TokenBase):
    _type = TokenType.CLASS
    _data: str

    def __init__(self, identifier: int, name: str, data: str):
        super().__init__(identifier, name)
        self._data = data

