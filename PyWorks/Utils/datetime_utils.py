import datetime


class DateTimeUtil:
    date_format = '%d-%m-%Y'

    @staticmethod
    def is_date(string):
        try:
            datetime.datetime.strptime(string, DateTimeUtil.date_format)
            return True
        except ValueError:
            return False

    @staticmethod
    def to_date(string):
        return datetime.datetime.strptime(string, DateTimeUtil.date_format)

    @staticmethod
    def get_range(from_date, to_date):
        range_array = []
        dd = [from_date + datetime.timedelta(days=x) for x in range((to_date - from_date).days + 1)]
        for d in dd:
            range_array.append(d)
        return range_array

    @staticmethod
    def is_weekday(date):
        return date.isoweekday() in range(1, 6)
