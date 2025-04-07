import datetime

class TimeUtils:
    """
    A utility class for time-related operations.
    """

    DEFAULT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    DEFAULT_TIME_FORMAT = "%H:%M:%S"
    DEFAULT_DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, now=None):
        """
        Initializes the TimeUtils object.

        Args:
            now (datetime, optional):  A datetime object to use as the current time.
                Defaults to None, which uses datetime.datetime.now().  Useful for testing.
        """
        self.now = now if now else datetime.datetime.now()


    def get_current_time(self, fmt=None):
        """
        Returns the current time in the specified format.  If no format is specified,
        uses DEFAULT_TIME_FORMAT.

        Args:
            fmt (str, optional): The format string for the time. Defaults to None.

        Returns:
            str: The current time as a string.

        Examples:
            >>> timeutils = TimeUtils(datetime.datetime(2023, 1, 1, 10, 30, 0))
            >>> timeutils.get_current_time()
            '10:30:00'
            >>> timeutils.get_current_time("%I:%M %p")
            '10:30 AM'
        """
        fmt = fmt or self.DEFAULT_TIME_FORMAT
        return self.now.strftime(fmt)


    def get_current_date(self, fmt=None):
        """
        Returns the current date in the specified format.  If no format is specified,
        uses DEFAULT_DATE_FORMAT.

        Args:
            fmt (str, optional): The format string for the date. Defaults to None.

        Returns:
            str: The current date as a string.

        Examples:
            >>> timeutils = TimeUtils(datetime.datetime(2023, 1, 1, 10, 30, 0))
            >>> timeutils.get_current_date()
            '2023-01-01'
            >>> timeutils.get_current_date("%m/%d/%Y")
            '01/01/2023'
        """
        fmt = fmt or self.DEFAULT_DATE_FORMAT
        return self.now.strftime(fmt)


    def add_seconds(self, seconds, fmt=None):
        """
        Adds the specified number of seconds to the current time and returns the
        result as a string in the specified format.  If no format is specified,
        uses DEFAULT_TIME_FORMAT.

        Args:
            seconds (int): The number of seconds to add.
            fmt (str, optional): The format string for the time. Defaults to None.

        Returns:
            str: The time after adding the seconds, as a string.

        Examples:
            >>> timeutils = TimeUtils(datetime.datetime(2023, 1, 1, 10, 30, 0))
            >>> timeutils.add_seconds(600)
            '10:40:00'
            >>> timeutils.add_seconds(600, "%I:%M %p")
            '10:40 AM'
        """
        fmt = fmt or self.DEFAULT_TIME_FORMAT
        new_datetime = self.now + datetime.timedelta(seconds=seconds)
        return new_datetime.strftime(fmt)


    def string_to_datetime(self, string, fmt=None):
        """
        Converts a time string to a datetime object.  If no format is specified,
        uses DEFAULT_DATETIME_FORMAT.

        Args:
            string (str): The time string to convert.
            fmt (str, optional): The format string for the time. Defaults to None.

        Returns:
            datetime: A datetime object representing the time string.

        Raises:
            ValueError: If the string does not match the format.

        Examples:
            >>> timeutils = TimeUtils()
            >>> timeutils.string_to_datetime("2023-01-01 10:30:00")
            datetime.datetime(2023, 1, 1, 10, 30, 0)
            >>> timeutils.string_to_datetime("01/01/2023 10:30:00", "%m/%d/%Y %H:%M:%S")
            datetime.datetime(2023, 1, 1, 10, 30, 0)
        """
        fmt = fmt or self.DEFAULT_DATETIME_FORMAT
        return datetime.datetime.strptime(string, fmt)


    def datetime_to_string(self, dt_obj, fmt=None):
        """
        Converts a datetime object to a string.  If no format is specified,
        uses DEFAULT_DATETIME_FORMAT.

        Args:
            dt_obj (datetime): The datetime object to convert.
            fmt (str, optional): The format string for the time. Defaults to None.

        Returns:
            str: The datetime object as a string.

        Examples:
            >>> timeutils = TimeUtils()
            >>> dt = datetime.datetime(2023, 1, 1, 10, 30, 0)
            >>> timeutils.datetime_to_string(dt)
            '2023-01-01 10:30:00'
            >>> timeutils.datetime_to_string(dt, "%m/%d/%Y %H:%M:%S")
            '01/01/2023 10:30:00'
        """
        fmt = fmt or self.DEFAULT_DATETIME_FORMAT
        return dt_obj.strftime(fmt)


    def get_minutes_difference(self, string_time1, string_time2, fmt=None):
        """
        Calculates the difference in minutes between two times represented as strings.
        Rounds the result to the nearest minute.  If no format is specified, uses
        DEFAULT_DATETIME_FORMAT.

        Args:
            string_time1 (str): The first time string.
            string_time2 (str): The second time string.
            fmt (str, optional): The format string for the times. Defaults to None.

        Returns:
            int: The difference in minutes between the two times, rounded to the nearest minute.

        Raises:
            ValueError: If either time string does not match the format.

        Examples:
            >>> timeutils = TimeUtils()
            >>> timeutils.get_minutes_difference("2023-01-01 01:01:01", "2023-01-01 02:01:01")
            60
            >>> timeutils.get_minutes_difference("01/01/2023 01:01:01", "01/01/2023 02:01:01", "%m/%d/%Y %H:%M:%S")
            60
        """
        fmt = fmt or self.DEFAULT_DATETIME_FORMAT
        time1 = datetime.datetime.strptime(string_time1, fmt)
        time2 = datetime.datetime.strptime(string_time2, fmt)
        difference = time2 - time1
        minutes = round(difference.total_seconds() / 60)
        return minutes


    def get_formatted_time(self, year, month, day, hour, minute, second, fmt=None):
        """
        Creates a datetime object from the given components and returns it as a
        formatted string.  If no format is specified, uses DEFAULT_DATETIME_FORMAT.

        Args:
            year (int): The year.
            month (int): The month.
            day (int): The day.
            hour (int): The hour.
            minute (int): The minute.
            second (int): The second.
            fmt (str, optional): The format string for the time. Defaults to None.

        Returns:
            str: The formatted time string.

        Raises:
            ValueError: If the date components are invalid.

        Examples:
            >>> timeutils = TimeUtils()
            >>> timeutils.get_formatted_time(2023, 1, 1, 10, 30, 0)
            '2023-01-01 10:30:00'
            >>> timeutils.get_formatted_time(2023, 1, 1, 10, 30, 0, "%m/%d/%Y %H:%M:%S")
            '01/01/2023 10:30:00'
        """
        fmt = fmt or self.DEFAULT_DATETIME_FORMAT
        dt = datetime.datetime(year, month, day, hour, minute, second)
        return dt.strftime(fmt)