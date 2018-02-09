class TokenizerBase:
    _requested_component_nr = 1
    _token = None

    def matches(self, components: []):
        raise NotImplementedError

    def get_token(self):
        if not self._token:
            raise Exception("No match was found, can not create token")
        return self._token

    def get_requested_component_nr(self):
        return self._requested_component_nr

    def set_requested_component_nr(self, amount):
        self._requested_component_nr = amount

    def set_token(self, token):
        self._token = token
