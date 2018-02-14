from typing import Any

from commands.middleware.middleware_base import MiddlewareBase


class CommandParameter:
    _name: str
    _middleware: MiddlewareBase
    _optional: bool
    _value: str
    _default_value: str

    def __init__(self, name: str, middleware: MiddlewareBase, optional=False):
        self._name = name
        self._middleware = middleware
        self._optional = optional
        self._value = None

    def is_optional(self) -> bool:
        return self._optional

    def get_name(self) -> str:
        return self._name

    def set_value(self, value) -> None:
        self._value = value

    def get_value(self) -> Any:
        return self._middleware.process(self._value)

    def has_value(self) -> bool:
        return self._value is not None

    def check(self) -> bool:
        if not self._optional and not self.has_value():
            raise Exception("The parameter " + self._name + " cannot be None")
        return self._middleware.check(self._value)
