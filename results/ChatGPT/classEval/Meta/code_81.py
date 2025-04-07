import math
from collections import Counter

class Statistics3:
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        """calculates the median of the given list."""
        if not data:
            return None
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
        else:
            return float(sorted_data[mid])

    @staticmethod
    def mode(data):
        """calculates the mode of the given list."""
        if not data:
            return []
        count = Counter(data)
        max_count = max(count.values())
        return [num for num, cnt in count.items() if cnt == max_count]

    @staticmethod
    def correlation(x, y):
        """calculates the correlation of the given list."""
        if len(x) != len(y) or len(x) < 2:
            return None
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        covariance = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        std_x = Statistics3.standard_deviation(x)
        std_y = Statistics3.standard_deviation(y)
        if std_x == 0 or std_y == 0:
            return None
        return covariance / (std_x * std_y)

    @staticmethod
    def mean(data):
        """calculates the mean of the given list."""
        if not data:
            return None
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        """calculates the correlation matrix of the given list."""
        if not data or not all(len(row) == len(data[0]) for row in data):
            return None
        n = len(data[0])
        matrix = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    matrix[i][j] = 1.0
                else:
                    matrix[i][j] = Statistics3.correlation([row[i] for row in data], [row[j] for row in data])
        return matrix

    @staticmethod
    def standard_deviation(data):
        """calculates the standard deviation of the given list."""
        if not data:
            return None
        mean_value = Statistics3.mean(data)
        variance = sum((xi - mean_value) ** 2 for xi in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """calculates the z-score of the given list."""
        if not data or len(set(data)) == 1:
            return None
        mean_value = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(xi - mean_value) / std_dev for xi in data]