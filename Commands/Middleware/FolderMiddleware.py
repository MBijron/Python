import pathlib

from Commands.Middleware import MiddlewareBase


class FolderMiddleware(MiddlewareBase):
    __type_name = "Folder"

    def get_type_name(self):
        return self.__type_name

    def check(self, input_variable):
        path = pathlib.Path(input_variable)
        if path.is_dir():
            return True

    def process(self, input_variable):
        return input_variable
