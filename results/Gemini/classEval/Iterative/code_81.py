import math

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
        data_sorted = sorted(data)
        n = len(data_sorted)
        if n % 2 == 0:
            mid1 = data_sorted[n // 2 - 1]
            mid2 = data_sorted[n // 2]
            median = (mid1 + mid2) / 2
        else:
            median = data_sorted[n // 2]
        return median

    @staticmethod
    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        """
        counts = {}
        for item in data:
            counts[item] = counts.get(item, 0) + 1

        max_count = 0
        modes = []
        for item, count in counts.items():
            if count > max_count:
                modes = [item]
                max_count = count
            elif count == max_count:
                modes.append(item)

        return modes

    @staticmethod
    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        """
        if len(x) != len(y) or len(x) <= 1:
            return None

        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x2 = sum(x[i] ** 2 for i in range(n))
        sum_y2 = sum(y[i] ** 2 for i in range(n))

        numerator = n * sum_xy - sum_x * sum_y
        denominator = math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

        if denominator == 0:
            return None

        return numerator / denominator

    @staticmethod
    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        """
        if not data:
            return None
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        """
        num_variables = len(data)
        correlation_matrix = [[None for _ in range(num_variables)] for _ in range(num_variables)]

        for i in range(num_variables):
            for j in range(num_variables):
                if len(data[i]) != len(data[j]):
                    correlation_matrix[i][j] = None
                else:
                    correlation = Statistics3.correlation(data[i], data[j])
                    correlation_matrix[i][j] = correlation if correlation is not None else (1.0 if len(data[i]) > 1 else None)

        return correlation_matrix

    @staticmethod
    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        """
        n = len(data)
        if n <= 1:
            return 0.0

        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / (n - 1)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        """
        n = len(data)
        if n <= 1:
            return None

        std_dev = Statistics3.standard_deviation(data)
        if std_dev == 0:
            return None

        mean = sum(data) / n
        z_scores = [(x - mean) / std_dev for x in data]
        return z_scores