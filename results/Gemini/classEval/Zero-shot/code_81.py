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
        n = len(data)
        data = sorted(data)
        if n % 2 == 0:
            return (data[n // 2 - 1] + data[n // 2]) / 2
        else:
            return data[n // 2]

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
        counts = {}
        for x in data:
            counts[x] = counts.get(x, 0) + 1
        max_count = 0
        modes = []
        for x, count in counts.items():
            if count > max_count:
                max_count = count
                modes = [x]
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
        n = len(x)
        if n != len(y):
            raise ValueError("x and y must have the same length")

        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)

        if mean_x is None or mean_y is None:
          return None

        std_dev_x = Statistics3.standard_deviation(x)
        std_dev_y = Statistics3.standard_deviation(y)

        if std_dev_x == 0 or std_dev_y == 0:
            return None

        covariance = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(n)]) / n
        return covariance / (std_dev_x * std_dev_y)

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
        num_variables = len(data)
        correlation_matrix = []
        for i in range(num_variables):
            row = []
            for j in range(num_variables):
                if num_variables == 1:
                  row.append(None)
                else:
                  row.append(Statistics3.correlation(data[i], data[j]))
            correlation_matrix.append(row)

        if num_variables == 1:
          result = [[None for _ in data[0]] for _ in data[0]]
          return [result[0], result[0], result[0]]

        return correlation_matrix

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
        n = len(data)
        if n == 0:
            return 0.0
        mean = Statistics3.mean(data)
        if mean is None:
          return 0.0
        return math.sqrt(sum([(x - mean) ** 2 for x in data]) / n)

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
        n = len(data)
        if n <= 1:
            return None

        mean = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)

        if std_dev == 0:
            return None

        return [(x - mean) / std_dev for x in data]