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
    def get_range(fromDate, toDate):
        rangeArray = []
        dd = [fromDate + datetime.timedelta(days=x) for x in range((toDate-fromDate).days + 1)]
        for d in dd:
            rangeArray.append(d)
        return rangeArray

    @staticmethod
    def is_weekday(date):
        return date.isoweekday() in range(1, 6)