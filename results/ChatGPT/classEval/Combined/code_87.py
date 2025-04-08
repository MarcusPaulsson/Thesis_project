import datetime

class TimeUtils:
    """
    A utility class for handling various time-related operations, including
    getting the current date and time, adding seconds, converting between
    strings and datetime objects, calculating time differences in minutes,
    and formatting datetime objects.
    """

    def __init__(self):
        """
        Initialize the TimeUtils instance and store the current datetime.
        """
        self.current_datetime = datetime.datetime.now()

    def get_current_time(self) -> str:
        """
        Return the current time formatted as '%H:%M:%S'.
        :return: Current time as a string
        """
        return self.current_datetime.strftime("%H:%M:%S")

    def get_current_date(self) -> str:
        """
        Return the current date formatted as '%Y-%m-%d'.
        :return: Current date as a string
        """
        return self.current_datetime.strftime("%Y-%m-%d")

    def add_seconds(self, seconds: int) -> str:
        """
        Add a specified number of seconds to the current time and return the
        new time formatted as '%H:%M:%S'.
        :param seconds: Number of seconds to add
        :return: New time as a string
        """
        new_time = self.current_datetime + datetime.timedelta(seconds=seconds)
        return new_time.strftime("%H:%M:%S")

    def string_to_datetime(self, time_string: str) -> datetime.datetime:
        """
        Convert a formatted time string to a datetime instance.
        :param time_string: Time string to convert
        :return: Corresponding datetime instance
        """
        return datetime.datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')

    def datetime_to_string(self, dt: datetime.datetime) -> str:
        """
        Convert a datetime instance to a formatted string.
        :param dt: Datetime instance to convert
        :return: Formatted time string
        """
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def get_minutes(self, time_string1: str, time_string2: str) -> int:
        """
        Calculate the number of minutes between two time strings.
        :param time_string1: First time string
        :param time_string2: Second time string
        :return: Number of minutes between the two times
        """
        dt1 = self.string_to_datetime(time_string1)
        dt2 = self.string_to_datetime(time_string2)
        return round((dt2 - dt1).total_seconds() / 60)

    def get_format_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int) -> str:
        """
        Get a formatted time string from individual date and time components.
        :param year: Year
        :param month: Month
        :param day: Day
        :param hour: Hour
        :param minute: Minute
        :param second: Second
        :return: Formatted time string
        """
        return datetime.datetime(year, month, day, hour, minute, second).strftime("%Y-%m-%d %H:%M:%S")