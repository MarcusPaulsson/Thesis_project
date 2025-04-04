import datetime

class TimeUtils:
    """
    A utility class for handling various time-related operations.
    """

    def __init__(self):
        """
        Initialize TimeUtils and set the current datetime.
        """
        self.datetime = datetime.datetime.now()

    def get_current_time(self):
        """
        Return the current time in the format of '%H:%M:%S'.
        :return: string
        """
        return self.datetime.strftime('%H:%M:%S')

    def get_current_date(self):
        """
        Return the current date in the format of '%Y-%m-%d'.
        :return: string
        """
        return self.datetime.strftime('%Y-%m-%d')

    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time.
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        """
        future_time = self.datetime + datetime.timedelta(seconds=seconds)
        return future_time.strftime('%H:%M:%S')

    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance.
        :param string: string, string before converting format
        :return: datetime instance
        """
        return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

    def datetime_to_string(self, dt):
        """
        Convert a datetime instance to a string.
        :param dt: the datetime instance to convert
        :return: string, converted time string
        """
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def get_minutes(self, string_time1, string_time2):
        """
        Calculate how many minutes have passed between two times, and round the results to the nearest minute.
        :return: int, the number of minutes between two times, rounded off
        """
        time1 = self.string_to_datetime(string_time1)
        time2 = self.string_to_datetime(string_time2)
        return round((time2 - time1).total_seconds() / 60)

    def get_format_time(self, year, month, day, hour, minute, second):
        """
        Get formatted time.
        :param year: int
        :param month: int
        :param day: int
        :param hour: int
        :param minute: int
        :param second: int
        :return: formatted time string
        """
        dt = datetime.datetime(year, month, day, hour, minute, second)
        return dt.strftime("%Y-%m-%d %H:%M:%S")