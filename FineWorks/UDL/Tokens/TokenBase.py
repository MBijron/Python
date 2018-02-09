from FineWorks.UDL.Tokens.TokenType import TokenType


class TokenBase:
    _type = TokenType.NULL
    _identifier: int
    _name: str

    def __init__(self, identifier: int, name: str):
        self._identifier = identifier
        self._name = name

    def get_type(self):
        return self._type

    def get_identifier(self):
        return self._identifier

    def get_name(self):
        return self._name
