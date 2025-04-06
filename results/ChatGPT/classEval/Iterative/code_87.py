import datetime

class TimeUtils:
    """
    A utility class for handling time and date operations including
    getting the current time and date, adding seconds to a datetime,
    converting between strings and datetime objects, calculating time 
    differences, and formatting datetime objects.
    """

    def __init__(self):
        """
        Initialize TimeUtils and get the current datetime.
        """
        self.current_datetime = datetime.datetime.now()

    def get_current_time(self):
        """
        Return the current time in the format '%H:%M:%S'.
        :return: string
        """
        return self.current_datetime.strftime('%H:%M:%S')

    def get_current_date(self):
        """
        Return the current date in the format '%Y-%m-%d'.
        :return: string
        """
        return self.current_datetime.strftime('%Y-%m-%d')

    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time.
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        """
        new_time = self.current_datetime + datetime.timedelta(seconds=seconds)
        return new_time.strftime('%H:%M:%S')

    @staticmethod
    def string_to_datetime(string):
        """
        Convert a time string to a datetime instance.
        :param string: string, the time string in format '%Y-%m-%d %H:%M:%S'
        :return: datetime instance
        """
        return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def datetime_to_string(dt):
        """
        Convert a datetime instance to a string.
        :param dt: datetime instance to convert
        :return: string, converted time string in format '%Y-%m-%d %H:%M:%S'
        """
        return dt.strftime('%Y-%m-%d %H:%M:%S')

    def get_minutes(self, string_time1, string_time2):
        """
        Calculate the number of minutes between two times.
        :param string_time1: string, first time in format '%Y-%m-%d %H:%M:%S'
        :param string_time2: string, second time in format '%Y-%m-%d %H:%M:%S'
        :return: int, the number of minutes between the two times
        """
        dt1 = self.string_to_datetime(string_time1)
        dt2 = self.string_to_datetime(string_time2)
        delta = dt2 - dt1
        return round(delta.total_seconds() / 60)

    @staticmethod
    def get_format_time(year, month, day, hour, minute, second):
        """
        Get formatted time string.
        :param year: int
        :param month: int
        :param day: int
        :param hour: int
        :param minute: int
        :param second: int
        :return: string, formatted time string in "YYYY-MM-DD HH:MM:SS" format
        """
        return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"