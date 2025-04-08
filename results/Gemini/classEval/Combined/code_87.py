import datetime

class TimeUtils:
    """
    A utility class for common time-related operations.
    """

    def __init__(self):
        """
        Initializes the TimeUtils with the current datetime.
        """
        self.datetime = datetime.datetime.now()

    def get_current_time(self):
        """
        Returns the current time in HH:MM:SS format.

        Returns:
            str: The current time.
        """
        return self.datetime.strftime("%H:%M:%S")

    def get_current_date(self):
        """
        Returns the current date in YYYY-MM-DD format.

        Returns:
            str: The current date.
        """
        return self.datetime.strftime("%Y-%m-%d")

    def add_seconds(self, seconds):
        """
        Adds a specified number of seconds to the current time and returns the result in HH:MM:SS format.

        Args:
            seconds (int): The number of seconds to add.

        Returns:
            str: The updated time.
        """
        new_datetime = self.datetime + datetime.timedelta(seconds=seconds)
        return new_datetime.strftime("%H:%M:%S")

    def string_to_datetime(self, time_string):
        """
        Converts a time string in YYYY-MM-DD HH:MM:SS format to a datetime object.

        Args:
            time_string (str): The time string to convert.

        Returns:
            datetime: A datetime object representing the time string.
        """
        return datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")

    def datetime_to_string(self, datetime_object):
        """
        Converts a datetime object to a string in YYYY-MM-DD HH:MM:SS format.

        Args:
            datetime_object (datetime): The datetime object to convert.

        Returns:
            str: The formatted time string.
        """
        return datetime_object.strftime("%Y-%m-%d %H:%M:%S")

    def get_minutes_difference(self, time_string1, time_string2):
        """
        Calculates the difference in minutes between two time strings (YYYY-MM-DD HH:MM:SS).

        Args:
            time_string1 (str): The first time string.
            time_string2 (str): The second time string.

        Returns:
            int: The difference in minutes, rounded to the nearest minute.
        """
        datetime_time1 = self.string_to_datetime(time_string1)
        datetime_time2 = self.string_to_datetime(time_string2)
        difference = datetime_time2 - datetime_time1
        minutes = round(difference.total_seconds() / 60)
        return minutes

    def format_time(self, year, month, day, hour, minute, second):
        """
        Creates a formatted time string (YYYY-MM-DD HH:MM:SS) from individual time components.

        Args:
            year (int): The year.
            month (int): The month.
            day (int): The day.
            hour (int): The hour.
            minute (int): The minute.
            second (int): The second.

        Returns:
            str: The formatted time string.
        """
        return datetime.datetime(year, month, day, hour, minute, second).strftime("%Y-%m-%d %H:%M:%S")