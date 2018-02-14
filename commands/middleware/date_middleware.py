from datetime import datetime
from pyworks.utils.datetime_utils import DateTimeUtil
from commands.middleware.middleware_base import MiddlewareBase


class DateMiddleware(MiddlewareBase):
    __type_name = "Input type should be of date format"

    def get_type_name(self) -> str:
        return self.__type_name

    def check(self, input_variable) -> bool:
        if DateTimeUtil.is_date(input_variable):
            return True

    def process(self, input_variable) -> datetime:
        return DateTimeUtil.to_date(input_variable)
