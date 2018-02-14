import pathlib
from commands.middleware.middleware_base import MiddlewareBase


class FolderMiddleware(MiddlewareBase):
    __type_name = "Folder"

    def get_type_name(self) -> str:
        return self.__type_name

    def check(self, input_variable) -> bool:
        path = pathlib.Path(input_variable)
        if path.is_dir():
            return True

    def process(self, input_variable) -> str:
        return input_variable
