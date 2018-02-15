from datetime import datetime
from unittest import TestCase

from pyworks.utils.datetime_utils import DateTimeUtil


class TestDateTimeUtil(TestCase):
    def test_get_current_date_equals_datetime_now(self) -> None:
        self.assertTrue(DateTimeUtil.get_current_date() == datetime.now())

    def test_is_date_returns_true_on_correct_date_format(self) -> None:
        self.assertTrue(DateTimeUtil.is_date("11-01-2008"))

    def test_is_date_returns_false_on_incorrect_date_format(self) -> None:
        self.assertFalse(DateTimeUtil.is_date("january 11"))

    def test_to_date_converts_correct_date_to_datetime(self) -> None:
        self.assertTrue(isinstance(DateTimeUtil.to_date("11-01-2008"), datetime))

    def test_get_range_between_dates_returns_expected_list_of_dates(self) -> None:
        dates = [
            DateTimeUtil.to_date("11-01-2008"),
            DateTimeUtil.to_date("12-01-2008"),
            DateTimeUtil.to_date("13-01-2008"),
        ]
        self.assertEqual(dates, DateTimeUtil.get_range(DateTimeUtil.to_date("11-01-2008"), DateTimeUtil.to_date("13-01-2008")))

    def test_is_weekday_returns_true_on_weekday(self) -> None:
        self.assertTrue(DateTimeUtil.is_weekday(DateTimeUtil.to_date("16-2-2018")))

    def test_is_weekday_returns_false_on_weekend(self) -> None:
        self.assertFalse(DateTimeUtil.is_weekday(DateTimeUtil.to_date("17-2-2018")))
