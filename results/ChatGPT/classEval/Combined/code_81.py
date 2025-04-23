import math
from collections import Counter

class Statistics3:
    """
    A class that implements methods for calculating statistical indicators such as median, mode, correlation, 
    correlation matrix, standard deviation, and Z-score.
    """

    @staticmethod
    def median(data):
        """Calculates the median of the given list."""
        if not data:
            return None
        sorted_data = sorted(data)
        mid = len(sorted_data) // 2
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2 if len(sorted_data) % 2 == 0 else sorted_data[mid]

    @staticmethod
    def mode(data):
        """Calculates the mode of the given list."""
        if not data:
            return []
        frequency = Counter(data)
        max_count = max(frequency.values())
        return [num for num, count in frequency.items() if count == max_count]

    @staticmethod
    def mean(data):
        """Calculates the mean of the given list."""
        return sum(data) / len(data) if data else None

    @staticmethod
    def standard_deviation(data):
        """Calculates the standard deviation of the given list."""
        if not data:
            return None
        mean_value = Statistics3.mean(data)
        variance = sum((xi - mean_value) ** 2 for xi in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """Calculates the Z-score of the given list."""
        if not data or len(set(data)) == 1:
            return None
        mean_value = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(xi - mean_value) / std_dev for xi in data]

    @staticmethod
    def correlation(x, y):
        """Calculates the correlation coefficient between two lists."""
        if len(x) != len(y) or len(x) < 2:
            return None
        mean_x, mean_y = Statistics3.mean(x), Statistics3.mean(y)
        numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        denominator = math.sqrt(sum((xi - mean_x) ** 2 for xi in x) * sum((yi - mean_y) ** 2 for yi in y))
        return numerator / denominator if denominator != 0 else None

    @staticmethod
    def correlation_matrix(data):
        """Calculates the correlation matrix for a list of lists."""
        if not data or not all(len(row) == len(data[0]) for row in data):
            return [[None] * len(data[0]) for _ in range(len(data[0]))]
        return [[Statistics3.correlation(row_i, row_j) for row_j in zip(*data)] for row_i in zip(*data)]