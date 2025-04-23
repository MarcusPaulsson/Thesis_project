import datetime

class TimeUtils:
    """
    A utility class for handling various time and date operations.
    """

    def __init__(self):
        """
        Initialize the TimeUtils instance with the current datetime.
        """
        self.current_datetime = datetime.datetime.now()

    def get_current_time(self) -> str:
        """
        Return the current time in the format of '%H:%M:%S'.
        :return: string
        """
        return self.current_datetime.strftime('%H:%M:%S')

    def get_current_date(self) -> str:
        """
        Return the current date in the format of "%Y-%m-%d".
        :return: string
        """
        return self.current_datetime.strftime('%Y-%m-%d')

    def add_seconds(self, seconds: int) -> str:
        """
        Add the specified number of seconds to the current time.
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        """
        new_time = self.current_datetime + datetime.timedelta(seconds=seconds)
        return new_time.strftime('%H:%M:%S')

    @staticmethod
    def string_to_datetime(time_string: str) -> datetime.datetime:
        """
        Convert the time string to a datetime instance.
        :param time_string: string, string before converting format
        :return: datetime instance
        """
        return datetime.datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def datetime_to_string(dt: datetime.datetime) -> str:
        """
        Convert a datetime instance to a string.
        :param dt: the datetime instance to convert
        :return: string, converted time string
        """
        return dt.strftime('%Y-%m-%d %H:%M:%S')

    def get_minutes(self, time_string1: str, time_string2: str) -> int:
        """
        Calculate how many minutes have passed between two times, and round the results to the nearest minute.
        :param time_string1: string, first time string
        :param time_string2: string, second time string
        :return: int, the number of minutes between two times, rounded off
        """
        dt1 = self.string_to_datetime(time_string1)
        dt2 = self.string_to_datetime(time_string2)
        return round((dt2 - dt1).total_seconds() / 60)

    @staticmethod
    def get_format_time(year: int, month: int, day: int, hour: int, minute: int, second: int) -> str:
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
        return dt.strftime('%Y-%m-%d %H:%M:%S')