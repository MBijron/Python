from FineWorks.UDL.Tokens.TokenType import TokenType


class TokenBase:
    _type = TokenType.NULL
    _identifier: int
    _name: str
    _components_used: int

    def __init__(self, identifier: int, components_used: int, name: str):
        self._identifier = identifier
        self._name = name
        self._components_used = components_used

    def get_type(self):
        return self._type

    def get_identifier(self):
        return self._identifier

    def get_name(self):
        return self._name

    def get_components_used(self) -> int:
        return self._components_used
