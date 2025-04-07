from collections import Counter
from typing import List

class DataStatistics:
    """
    This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.
    """

    def mean(self, data: List[float]) -> float:
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data: list, data list
        :return: float, the mean value or None if data is empty.
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.0
        """
        if not data:
            return 0.0
        return round(sum(data) / len(data), 2)

    def median(self, data: List[float]) -> float:
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data: list, data list
        :return: float, the median value, or None if data is empty.
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.0
        """
        if not data:
            return 0.0
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            median = sorted_data[n // 2]
        return round(median, 2)

    def mode(self, data: List[float]) -> List[float]:
        """
        Calculate the mode of a set of data
        :param data: list, data list
        :return: list, the mode(s).  Returns an empty list if data is empty.
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        if not data:
            return []

        counts = Counter(data)
        max_count = max(counts.values())
        modes = [key for key, value in counts.items() if value == max_count]
        modes.sort()
        return modes