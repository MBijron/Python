from fineworks.udl.tokens.token_base import TokenBase


class LexerBase:
    _requested_component_nr = 1
    _token = None

    def matches(self, components: []) -> bool:
        raise NotImplementedError

    def get_token(self) -> TokenBase:
        if not self._token:
            raise Exception("No match was found, can not create token")
        return self._token

    def get_requested_component_nr(self) -> int:
        return self._requested_component_nr

    def set_requested_component_nr(self, amount) -> None:
        self._requested_component_nr = amount

    def set_token(self, token) -> None:
        self._token = token
