import pathlib

from commands.middleware.middleware_base import MiddlewareBase


class PathMiddleware(MiddlewareBase):
    __type_name = "Path"

    def get_type_name(self) -> str:
        return self.__type_name

    def check(self, input_variable) -> bool:
        path = pathlib.Path(input_variable)
        if path.is_dir() or path.is_file():
            return True

    def process(self, input_variable) -> str:
        return input_variable
