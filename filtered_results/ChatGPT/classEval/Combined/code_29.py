from collections import Counter
import statistics

class DataStatistics:
    """
    A class for performing basic statistical operations on a data set,
    including mean, median, and mode calculations.
    """

    def mean(self, data):
        """
        Calculate the mean of a dataset, rounded to two decimal places.
        :param data: list of numerical values
        :return: float, the mean value or 0.00 if data is empty
        """
        if not data:
            return 0.00
        return round(sum(data) / len(data), 2)

    def median(self, data):
        """
        Calculate the median of a dataset, rounded to two decimal places.
        :param data: list of numerical values
        :return: float, the median value or 0.00 if data is empty
        """
        if not data:
            return 0.00
        return round(statistics.median(data), 2)

    def mode(self, data):
        """
        Calculate the mode of a dataset.
        :param data: list of numerical values
        :return: list, the mode(s) or an empty list if data is empty
        """
        if not data:
            return []
        count = Counter(data)
        max_freq = max(count.values())
        return sorted(num for num, freq in count.items() if freq == max_freq)

# Unit tests for DataStatistics class
import unittest

class TestDataStatistics(unittest.TestCase):

    def setUp(self):
        self.ds = DataStatistics()

    def test_mean(self):
        self.assertEqual(self.ds.mean([1, 2, 3, 4, 5]), 3.00)
        self.assertEqual(self.ds.mean([1, 2, 3, 4, 5, 6]), 3.50)
        self.assertEqual(self.ds.mean([1, 2, 4, 5, 6, 7]), 4.17)
        self.assertEqual(self.ds.mean([1, 2, 4, 5, 6, 7, 8]), 4.71)
        self.assertEqual(self.ds.mean([1, 2, 4, 5, 6, 7, 8, 9]), 5.25)

    def test_median(self):
        self.assertEqual(self.ds.median([2, 5, 1, 3, 4]), 3.00)
        self.assertEqual(self.ds.median([2, 5, 1, 3, 4, 6]), 3.50)
        self.assertEqual(self.ds.median([2, 5, 1, 4, 6, 7]), 4.50)
        self.assertEqual(self.ds.median([2, 5, 1, 4, 6, 7, 8]), 5.00)
        self.assertEqual(self.ds.median([2, 5, 1, 4, 6, 7, 8, 9]), 5.50)

    def test_mode(self):
        self.assertEqual(self.ds.mode([2, 2, 3, 3, 4]), [2, 3])
        self.assertEqual(self.ds.mode([2, 2, 2, 3, 3, 4]), [2])
        self.assertEqual(self.ds.mode([2, 2, 3, 3, 4, 4]), [2, 3, 4])
        self.assertEqual(self.ds.mode([2, 2, 3, 3, 4, 4, 4]), [4])
        self.assertEqual(self.ds.mode([2, 2, 3, 3, 4, 4, 4, 5]), [4])

if __name__ == "__main__":
    unittest.main()