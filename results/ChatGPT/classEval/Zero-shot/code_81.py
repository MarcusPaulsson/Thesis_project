import math
from collections import Counter

class Statistics3:
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        if not data:
            return None
        sorted_data = sorted(data)
        mid = len(sorted_data) // 2
        if len(sorted_data) % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    @staticmethod
    def mode(data):
        if not data:
            return []
        counts = Counter(data)
        max_count = max(counts.values())
        return [num for num, count in counts.items() if count == max_count]

    @staticmethod
    def correlation(x, y):
        if len(x) != len(y) or len(x) < 2:
            return None
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        denominator_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
        denominator_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))
        if denominator_x == 0 or denominator_y == 0:
            return None
        return numerator / (denominator_x * denominator_y)

    @staticmethod
    def mean(data):
        if not data:
            return None
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        if not data or not all(len(row) == len(data[0]) for row in data):
            return [[None] * len(data) for _ in range(len(data))]
        n = len(data)
        matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    matrix[i][j] = 1.0
                else:
                    matrix[i][j] = Statistics3.correlation(data[i], data[j])
        return matrix

    @staticmethod
    def standard_deviation(data):
        if not data:
            return None
        mean_value = Statistics3.mean(data)
        variance = sum((xi - mean_value) ** 2 for xi in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        if not data or len(data) == 1:
            return None
        mean_value = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(xi - mean_value) / std_dev for xi in data]