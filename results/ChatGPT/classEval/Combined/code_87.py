import datetime
import unittest

class TimeUtils:
    """
    Utility class for time-related operations including current time/date retrieval,
    adding seconds to a datetime, converting between strings and datetime objects,
    calculating time differences in minutes, and formatting datetime objects.
    """

    def __init__(self):
        """
        Initialize with the current datetime.
        """
        self.current_datetime = datetime.datetime.now()

    def get_current_time(self):
        """
        Return the current time in the format of '%H:%M:%S'.
        :return: str
        """
        return self.current_datetime.strftime('%H:%M:%S')

    def get_current_date(self):
        """
        Return the current date in the format of '%Y-%m-%d'.
        :return: str
        """
        return self.current_datetime.strftime('%Y-%m-%d')

    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time.
        :param seconds: int, number of seconds to add
        :return: str, time after adding seconds in the format '%H:%M:%S'
        """
        new_time = self.current_datetime + datetime.timedelta(seconds=seconds)
        return new_time.strftime('%H:%M:%S')

    @staticmethod
    def string_to_datetime(time_string):
        """
        Convert a time string to a datetime instance.
        :param time_string: str, time in the format '%Y-%m-%d %H:%M:%S'
        :return: datetime instance
        """
        return datetime.datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def datetime_to_string(dt):
        """
        Convert a datetime instance to a string.
        :param dt: datetime instance to convert
        :return: str, formatted datetime string
        """
        return dt.strftime('%Y-%m-%d %H:%M:%S')

    def get_minutes(self, time_string1, time_string2):
        """
        Calculate the number of minutes between two times.
        :param time_string1: str, first time in the format '%Y-%m-%d %H:%M:%S'
        :param time_string2: str, second time in the format '%Y-%m-%d %H:%M:%S'
        :return: int, number of minutes between the two times
        """
        dt1 = self.string_to_datetime(time_string1)
        dt2 = self.string_to_datetime(time_string2)
        return round((dt2 - dt1).total_seconds() / 60)

    @staticmethod
    def get_formatted_time(year, month, day, hour, minute, second):
        """
        Get formatted time string from individual date and time components.
        :param year: int
        :param month: int
        :param day: int
        :param hour: int
        :param minute: int
        :param second: int
        :return: str, formatted time string
        """
        return datetime.datetime(year, month, day, hour, minute, second).strftime('%Y-%m-%d %H:%M:%S')


class TimeUtilsTest(unittest.TestCase):
    def setUp(self):
        self.timeutils = TimeUtils()

    def test_get_current_time(self):
        self.assertEqual(self.timeutils.get_current_time(), self.timeutils.current_datetime.strftime("%H:%M:%S"))

    def test_get_current_date(self):
        self.assertEqual(self.timeutils.get_current_date(), self.timeutils.current_datetime.strftime("%Y-%m-%d"))

    def test_add_seconds(self):
        self.assertEqual(self.timeutils.add_seconds(600),
                         (self.timeutils.current_datetime + datetime.timedelta(seconds=600)).strftime("%H:%M:%S"))

    def test_string_to_datetime(self):
        self.assertEqual(self.timeutils.string_to_datetime('2001-07-18 01:01:01'), datetime.datetime(2001, 7, 18, 1, 1, 1))

    def test_datetime_to_string(self):
        self.assertEqual(self.timeutils.datetime_to_string(self.timeutils.current_datetime),
                         self.timeutils.current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

    def test_get_minutes(self):
        self.assertEqual(self.timeutils.get_minutes("2001-07-18 01:01:01", "2001-07-18 02:01:01"), 60)

    def test_get_formatted_time(self):
        self.assertEqual(self.timeutils.get_formatted_time(2001, 7, 18, 1, 1, 1), "2001-07-18 01:01:01")


if __name__ == "__main__":
    unittest.main()