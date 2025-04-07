import math
from collections import Counter

class Statistics3:
    @staticmethod
    def median(data):
        if not data:
            return None
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
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
        if len(x) != len(y) or len(x) == 0:
            return None
        n = len(x)
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(n))) * math.sqrt(sum((y[i] - mean_y) ** 2 for i in range(n)))
        return numerator / denominator if denominator != 0 else None

    @staticmethod
    def mean(data):
        return sum(data) / len(data) if data else None

    @staticmethod
    def correlation_matrix(data):
        if not data or not data[0]:
            return [[None] * len(data[0]) for _ in range(len(data))]
        n = len(data)
        m = len(data[0])
        matrix = [[0.0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
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
        variance = sum((x - mean_value) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        if not data or len(set(data)) == 1:
            return None
        mean_value = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(x - mean_value) / std_dev for x in data]