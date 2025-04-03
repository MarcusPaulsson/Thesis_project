import datetime

class TimeUtils:
    """
    This is a time util class, including getting the current time and date, adding seconds to a datetime, 
    converting between strings and datetime objects, calculating the time difference in minutes, 
    and formatting a datetime object.
    """

    def __init__(self):
        """
        Get the current datetime
        """
        self.datetime = datetime.datetime.now()

    def get_current_time(self):
        """
        Return the current time in the format of '%H:%M:%S'
        :return: string
        >>> timeutils = TimeUtils()
        >>> timeutils.get_current_time()
        "19:19:22"
        """
        return self.datetime.strftime('%H:%M:%S')

    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        >>> timeutils = TimeUtils()
        >>> timeutils.get_current_date()
        "2023-06-14"
        """
        return self.datetime.strftime('%Y-%m-%d')

    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        >>> timeutils = TimeUtils()
        >>> timeutils.add_seconds(600)
        "19:29:22"
        """
        new_time = self.datetime + datetime.timedelta(seconds=seconds)
        return new_time.strftime('%H:%M:%S')

    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils = TimeUtils()
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        datetime.datetime(2001, 7, 18, 1, 1, 1)
        """
        return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

    def datetime_to_string(self, dt):
        """
        Convert a datetime instance to a string
        :param dt: the datetime instance to convert
        :return: string, converted time string
        >>> timeutils = TimeUtils()
        >>> timeutils.datetime_to_string(timeutils.datetime)
        "2023-06-14 19:30:03"
        """
        return dt.strftime('%Y-%m-%d %H:%M:%S')

    def get_minutes(self, string_time1, string_time2):
        """
        Calculate how many minutes have passed between two times, and round the results to the nearest
        :return: int, the number of minutes between two times, rounded off
        >>> timeutils = TimeUtils()
        >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
        60
        """
        dt1 = self.string_to_datetime(string_time1)
        dt2 = self.string_to_datetime(string_time2)
        delta = dt2 - dt1
        return round(delta.total_seconds() / 60)

    def get_format_time(self, year, month, day, hour, minute, second):
        """
        get format time
        :param year: int
        :param month: int
        :param day: int
        :param hour: int
        :param minute: int
        :param second: int
        :return: formatted time string
        >>> timeutils = TimeUtils()
        >>> timeutils.get_format_time(2001, 7, 18, 1, 1, 1)
        "2001-07-18 01:01:01"
        """
        dt = datetime.datetime(year, month, day, hour, minute, second)
        return dt.strftime('%Y-%m-%d %H:%M:%S')