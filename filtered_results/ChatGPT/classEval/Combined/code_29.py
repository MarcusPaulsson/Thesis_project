from collections import Counter
from typing import List, Union
import statistics

class DataStatistics:
    """
    A class for performing data statistics, supporting calculation of mean, median, and mode of a given data set.
    """

    def mean(self, data: List[Union[int, float]]) -> float:
        """
        Calculate the average value of a group of data, accurate to two digits after the decimal separator.
        :param data: List of int or float, data list
        :return: float, the mean value
        """
        if not data:
            return 0.0
        return round(sum(data) / len(data), 2)

    def median(self, data: List[Union[int, float]]) -> float:
        """
        Calculate the median of a group of data, accurate to two digits after the decimal separator.
        :param data: List of int or float, data list
        :return: float, the median value
        """
        if not data:
            return 0.0
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return round((sorted_data[mid - 1] + sorted_data[mid]) / 2, 2)
        return round(sorted_data[mid], 2)

    def mode(self, data: List[Union[int, float]]) -> List[Union[int, float]]:
        """
        Calculate the mode of a set of data.
        :param data: List of int or float, data list
        :return: List of int or float, the mode(s)
        """
        if not data:
            return []
        frequency = Counter(data)
        max_count = max(frequency.values())
        modes = [key for key, count in frequency.items() if count == max_count]
        return sorted(modes)
