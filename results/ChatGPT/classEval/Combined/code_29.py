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

# Test cases remain unchanged.
import unittest

class DataStatisticsTestMean(unittest.TestCase):
    def test_mean_1(self):
        ds = DataStatistics()
        res = ds.mean([1, 2, 3, 4, 5])
        self.assertEqual(res, 3.00)

    def test_mean_2(self):
        ds = DataStatistics()
        res = ds.mean([1, 2, 3, 4, 5, 6])
        self.assertEqual(res, 3.50)

    def test_mean_3(self):
        ds = DataStatistics()
        res = ds.mean([1, 2, 4, 5, 6, 7])
        self.assertEqual(res, 4.17)

    def test_mean_4(self):
        ds = DataStatistics()
        res = ds.mean([1, 2, 4, 5, 6, 7, 8])
        self.assertEqual(res, 4.71)

    def test_mean_5(self):
        ds = DataStatistics()
        res = ds.mean([1, 2, 4, 5, 6, 7, 8, 9])
        self.assertEqual(res, 5.25)


class DataStatisticsTestMedian(unittest.TestCase):
    def test_median_1(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 3, 4])
        self.assertEqual(res, 3.00)

    def test_median_2(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 3, 4, 6])
        self.assertEqual(res, 3.50)

    def test_median_3(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 4, 6, 7])
        self.assertEqual(res, 4.50)

    def test_median_4(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 4, 6, 7, 8])
        self.assertEqual(res, 5.00)

    def test_median_5(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 4, 6, 7, 8, 9])
        self.assertEqual(res, 5.50)


class DataStatisticsTestMode(unittest.TestCase):
    def test_mode_1(self):
        ds = DataStatistics()
        res = ds.mode([2, 2, 3, 3, 4])
        self.assertEqual(res, [2, 3])

    def test_mode_2(self):
        ds = DataStatistics()
        res = ds.mode([2, 2, 2, 3, 3, 4])
        self.assertEqual(res, [2])

    def test_mode_3(self):
        ds = DataStatistics()
        res = ds.mode([2, 2, 3, 3, 4, 4])
        self.assertEqual(res, [2, 3, 4])

    def test_mode_4(self):
        ds = DataStatistics()
        res = ds.mode([2, 2, 3, 3, 4, 4, 4])
        self.assertEqual(res, [4])

    def test_mode_5(self):
        ds = DataStatistics()
        res = ds.mode([2, 2, 3, 3, 4, 4, 4, 5])
        self.assertEqual(res, [4])


class DataStatisticsTest(unittest.TestCase):
    def test_datastatistics(self):
        ds = DataStatistics()
        res = ds.mean([1, 2, 3, 4, 5])
        self.assertEqual(res, 3.00)
        res = ds.median([2, 5, 1, 3, 4])
        self.assertEqual(res, 3.00)
        res = ds.mode([2, 2, 3, 3, 4])
        self.assertEqual(res, [2, 3])