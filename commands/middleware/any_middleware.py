from commands.middleware.middleware_base import MiddlewareBase


class AnyMiddleware(MiddlewareBase):
    __type_name = "Input type should be of any format"

    def get_type_name(self) -> str:
        return self.__type_name

    def check(self, input_variable) -> bool:
        return True

    def process(self, input_variable) -> str:
        return input_variable
