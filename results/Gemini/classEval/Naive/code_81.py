import math
from collections import Counter

class Statistics3:
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        """
        calculates the median of the given list.
        :param data: the given list, list.
        :return: the median of the given list, float.
        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            # Even number of elements, median is the average of the middle two
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            median = (mid1 + mid2) / 2
        else:
            # Odd number of elements, median is the middle element
            median = sorted_data[n // 2]
        return median

    @staticmethod
    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        """
        counts = Counter(data)
        max_count = max(counts.values())
        modes = [key for key, value in counts.items() if value == max_count]
        return modes

    @staticmethod
    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        """
        if not data:
            return 0.0
        return sum(data) / len(data)

    @staticmethod
    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        """
        if not data:
            return 0.0

        n = len(data)
        if n < 2:
            return 0.0

        mean = Statistics3.mean(data)
        variance = sum([(x - mean) ** 2 for x in data]) / (n - 1)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        """
        if not data:
            return []

        mean = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)

        if std_dev == 0:
            return [0.0] * len(data)

        return [(x - mean) / std_dev for x in data]
    
    @staticmethod
    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        """
        if not x or not y or len(x) != len(y):
            return None

        n = len(x)
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)

        numerator = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(n)])
        denominator = Statistics3.standard_deviation(x) * Statistics3.standard_deviation(y) * (n - 1)

        if denominator == 0:
            return 0.0  # Handle the case where standard deviations are zero

        return numerator / denominator

    @staticmethod
    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        """
        if not data:
            return []

        num_variables = len(data)
        correlation_matrix = [[0.0] * num_variables for _ in range(num_variables)]

        for i in range(num_variables):
            for j in range(num_variables):
                correlation_matrix[i][j] = Statistics3.correlation(data[i], data[j])
        return correlation_matrix