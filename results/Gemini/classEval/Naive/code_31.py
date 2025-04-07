import math

class DataStatistics4:
    """
    This is a class that performs advanced mathematical calculations and statistics, including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
    """


    @staticmethod
    def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
        :param data1: The first set of data,list.
        :param data2: The second set of data,list.
        :return: The correlation coefficient, float.
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
        0.9999999999999998

        """
        n = len(data1)
        if n != len(data2):
            raise ValueError("Data sets must have the same length")

        sum_x = sum(data1)
        sum_y = sum(data2)
        sum_x_squared = sum(x**2 for x in data1)
        sum_y_squared = sum(y**2 for y in data2)
        sum_xy = sum(data1[i] * data2[i] for i in range(n))

        numerator = n * sum_xy - sum_x * sum_y
        denominator = math.sqrt((n * sum_x_squared - sum_x**2) * (n * sum_y_squared - sum_y**2))

        if denominator == 0:
            return 0.0  # Handle the case where the denominator is zero to avoid division by zero
        else:
            return numerator / denominator

    @staticmethod
    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463

        """
        n = len(data)
        if n < 3:
            return 0.0

        mean = sum(data) / n
        variance = sum((x - mean)**2 for x in data) / (n - 1)
        std_dev = math.sqrt(variance)

        if std_dev == 0:
            return 0.0

        skewness = sum((x - mean)**3 for x in data) / ((n - 1) * std_dev**3)
        return skewness

    @staticmethod
    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        >>> DataStatistics4.kurtosis([1, 20,100])
        -1.5000000000000007

        """
        n = len(data)
        if n < 4:
            return float('NaN')

        mean = sum(data) / n
        variance = sum((x - mean)**2 for x in data) / (n - 1)
        std_dev = math.sqrt(variance)
        
        if std_dev == 0:
            return float('NaN')

        kurtosis = sum((x - mean)**4 for x in data) / ((n - 1) * std_dev**4) - 3
        return kurtosis

    @staticmethod
    def pdf(data, mu, sigma):
        """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.
        :param data: The input data list, list.
        :param mu: The mean of the normal distribution, float.
        :param sigma: The standard deviation of the normal distribution, float.
        :return: The probability density function (PDF), list.
        >>> DataStatistics4.pdf([1, 2, 3], 1, 1)
        [0.3989422804014327, 0.24197072451914337, 0.05399096651318806]

        """
        pdf_values = []
        for x in data:
            exponent = -((x - mu)**2) / (2 * sigma**2)
            coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
            pdf = coefficient * math.exp(exponent)
            pdf_values.append(pdf)
        return pdf_values