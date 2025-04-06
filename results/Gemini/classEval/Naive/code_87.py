import datetime
import time


class TimeUtils:
    """
    This is a time util class, including getting the current time and date, adding seconds to a datetime, converting between strings and datetime objects, calculating the time difference in minutes, and formatting a datetime object.
    """

    def __init__(self):
        """
        Initialize with the current datetime.
        """
        self.datetime = datetime.datetime.now()

    def get_current_time(self):
        """
        Return the current time in the format of '%H:%M:%S'
        :return: string
        """
        now = datetime.datetime.now()
        return now.strftime('%H:%M:%S')

    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        """
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d')

    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        """
        new_time = self.datetime + datetime.timedelta(seconds=seconds)
        return new_time.strftime('%H:%M:%S')

    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        """
        return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

    def datetime_to_string(self, datetime_obj):
        """
        Convert a datetime instance to a string
        :param datetime_obj: the datetime instance to convert
        :return: string, converted time string
        """
        return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

    def get_minutes(self, string_time1, string_time2):
        """
        Calculate how many minutes have passed between two times, and round the results to the nearest
        :return: int, the number of minutes between two times, rounded off
        """
        time1 = datetime.datetime.strptime(string_time1, "%Y-%m-%d %H:%M:%S")
        time2 = datetime.datetime.strptime(string_time2, "%Y-%m-%d %H:%M:%S")
        difference = time2 - time1
        minutes = round(difference.total_seconds() / 60)
        return minutes

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
        """
        dt = datetime.datetime(year, month, day, hour, minute, second)
        return dt.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    timeutils = TimeUtils()

    # Example usage of get_current_time
    current_time = timeutils.get_current_time()
    print(f"Current Time: {current_time}")

    # Example usage of get_current_date
    current_date = timeutils.get_current_date()
    print(f"Current Date: {current_date}")

    # Example usage of add_seconds
    time_after_seconds = timeutils.add_seconds(600)
    print(f"Time after adding 600 seconds: {time_after_seconds}")

    # Example usage of string_to_datetime
    datetime_obj = timeutils.string_to_datetime("2001-7-18 1:1:1")
    print(f"Datetime Object: {datetime_obj}")

    # Example usage of datetime_to_string
    datetime_string = timeutils.datetime_to_string(timeutils.datetime)
    print(f"Datetime String: {datetime_string}")

    # Example usage of get_minutes
    minutes_difference = timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
    print(f"Minutes Difference: {minutes_difference}")

    # Example usage of get_format_time
    formatted_time = timeutils.get_format_time(2001, 7, 18, 1, 1, 1)
    print(f"Formatted Time: {formatted_time}")