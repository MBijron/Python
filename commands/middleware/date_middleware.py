from pyworks.utils import DateTimeUtil
from commands.middleware import MiddlewareBase


class DateMiddleware(MiddlewareBase):
    __type_name = "Input type should be of date format"

    def get_type_name(self):
        return self.__type_name

    def check(self, input_variable):
        if DateTimeUtil.is_date(input_variable):
            return True

    def process(self, input_variable):
        return DateTimeUtil.to_date(input_variable)
