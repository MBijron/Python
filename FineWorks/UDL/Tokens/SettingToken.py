from FineWorks.UDL.Tokens import TokenBase
from FineWorks.UDL.Tokens.TokenType import TokenType


class SettingToken(TokenBase):
    _type = TokenType.SETTING
    _value: str

    def __init__(self, identifier: int, components_used: int,  name: str, value: str):
        super().__init__(identifier, components_used, name)
        self._value = value
