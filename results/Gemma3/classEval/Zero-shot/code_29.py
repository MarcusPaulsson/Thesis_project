from collections import Counter

class DataStatistics:
    """
    This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.
    """

    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
        if not data:
            return 0.00
        mean_value = sum(data) / len(data)
        return float("{:.2f}".format(mean_value))

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        if not data:
            return 0.00
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            median_value = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            median_value = sorted_data[n // 2]
        return float("{:.2f}".format(median_value))

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        if not data:
            return []
        counts = Counter(data)
        max_count = max(counts.values())
        mode_list = [key for key, value in counts.items() if value == max_count]
        return mode_list
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