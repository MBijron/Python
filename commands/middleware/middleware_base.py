from typing import Any


class MiddlewareBase:
    def check(self, input_variable) -> bool:
        raise NotImplementedError

    def process(self, input_variable) -> Any:
        raise NotImplementedError

    def get_exception_message(self) -> str:
        return "Attribute should be of type " + self.get_type_name()

    def get_type_name(self) -> str:
        raise NotImplementedError
