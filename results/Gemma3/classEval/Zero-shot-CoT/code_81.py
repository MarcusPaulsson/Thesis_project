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
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5

        """
        if not data:
            return None
        data.sort()
        n = len(data)
        if n % 2 == 0:
            return (data[n // 2 - 1] + data[n // 2]) / 2
        else:
            return float(data[n // 2])

    @staticmethod
    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """
        if not data:
            return []
        counts = {}
        for x in data:
            counts[x] = counts.get(x, 0) + 1
        max_count = 0
        modes = []
        for x, count in counts.items():
            if count > max_count:
                modes = [x]
                max_count = count
            elif count == max_count:
                modes.append(x)
        return modes

    @staticmethod
    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
        1.0

        """
        if len(x) != len(y) or len(x) == 0:
            return None
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_x_squared = sum(xi**2 for xi in x)
        sum_y_squared = sum(yi**2 for yi in y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))

        numerator = n * sum_xy - sum_x * sum_y
        denominator = math.sqrt((n * sum_x_squared - sum_x**2) * (n * sum_y_squared - sum_y**2))

        if denominator == 0:
            return None
        else:
            return numerator / denominator

    @staticmethod
    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.mean([1, 2, 3])
        2.0

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
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """
        if not data or len(data[0]) == 0:
            return []
        n = len(data)
        matrix = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = Statistics3.correlation(data[i], data[j])
        return matrix

    @staticmethod
    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0

        """
        if not data:
            return None
        mean = Statistics3.mean(data)
        variance = sum((x - mean)**2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.z_score([1, 2, 3, 4])
        [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]

        """
        if not data:
            return []
        mean = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        if std_dev == 0:
            return None
        return [(x - mean) / std_dev for x in data]