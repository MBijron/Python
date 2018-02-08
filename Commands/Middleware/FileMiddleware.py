import pathlib

from Commands.Middleware.MiddlewareBase import MiddlewareBase


class FileMiddleware(MiddlewareBase):
    __type_name = "File"

    def check(self, input_variable):
        path = pathlib.Path(input_variable)
        if path.is_file:
            return True

    def process(self, input_variable):
        return input_variable

    def get_type_name(self):
        return self.__type_name
