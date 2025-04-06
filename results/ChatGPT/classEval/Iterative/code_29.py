from collections import Counter

class DataStatistics:
    """
    This is a class for performing data statistics, supporting the calculation of mean, median, and mode of a given data set.
    """

    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the decimal separator.
        :param data: list, data list
        :return: float, the mean value
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.0
        >>> ds.mean([])
        0.0
        """
        if not data:
            return 0.0
        return round(sum(data) / len(data), 2)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the decimal separator.
        :param data: list, data list
        :return: float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.0
        >>> ds.median([])
        0.0
        """
        if not data:
            return 0.0
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        median_value = (sorted_data[mid - 1] + sorted_data[mid]) / 2 if n % 2 == 0 else sorted_data[mid]
        return round(median_value, 2)

    def mode(self, data):
        """
        Calculate the mode of a set of data.
        :param data: list, data list
        :return: list, the mode(s)
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        >>> ds.mode([])
        []
        """
        if not data:
            return []
        count = Counter(data)
        max_count = max(count.values())
        mode_values = [key for key, value in count.items() if value == max_count]
        return mode_values if len(mode_values) < len(data) else []