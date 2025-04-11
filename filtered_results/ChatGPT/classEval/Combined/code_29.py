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
