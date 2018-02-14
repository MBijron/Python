from datetime import datetime, timedelta


class DateTimeUtil:
    date_format = '%d-%m-%Y'

    @staticmethod
    def get_current_date() -> datetime:
        return datetime.now()

    @staticmethod
    def is_date(string) -> bool:
        try:
            datetime.strptime(string, DateTimeUtil.date_format)
            return True
        except ValueError:
            return False

    @staticmethod
    def to_date(string) -> datetime:
        return datetime.strptime(string, DateTimeUtil.date_format)

    @staticmethod
    def get_range(from_date, to_date) -> [ datetime ]:
        range_array : [ datetime ] = []
        dd = [from_date + timedelta(days=x) for x in range((to_date - from_date).days + 1)]
        for d in dd:
            range_array.append(d)
        return range_array

    @staticmethod
    def is_weekday(date) -> bool:
        return date.isoweekday() in range(1, 6)
