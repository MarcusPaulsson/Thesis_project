import math
from statistics import mean, stdev

class DataStatistics4:
    """
    This is a class that performs advanced mathematical calculations and statistics,
    including correlation coefficient, skewness, kurtosis, and probability density function (PDF) 
    for a normal distribution.
    """

    @staticmethod
    def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
        :param data1: The first set of data, list.
        :param data2: The second set of data, list.
        :return: The correlation coefficient, float.
        """
        if len(data1) != len(data2) or len(data1) == 0:
            raise ValueError("Input lists must be of the same non-zero length.")
        
        n = len(data1)
        mean1 = mean(data1)
        mean2 = mean(data2)
        numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
        denominator = math.sqrt(sum((data1[i] - mean1) ** 2 for i in range(n)) * 
                                 sum((data2[i] - mean2) ** 2 for i in range(n)))
        return numerator / denominator if denominator != 0 else 0.0

    @staticmethod
    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        """
        n = len(data)
        if n < 3:
            raise ValueError("Skewness requires at least three data points.")
        
        mean_data = mean(data)
        stdev_data = stdev(data)
        skew = (n / ((n - 1) * (n - 2))) * sum(((x - mean_data) / stdev_data) ** 3 for x in data)
        return skew

    @staticmethod
    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        """
        n = len(data)
        if n < 4:
            raise ValueError("Kurtosis requires at least four data points.")
        
        mean_data = mean(data)
        stdev_data = stdev(data)
        kurt = (n * (n + 1) * sum(((x - mean_data) / stdev_data) ** 4 for x in data) - 
               3 * (n - 1) ** 2) / ((n - 1) * (n - 2) * (n - 3))
        return kurt

    @staticmethod
    def pdf(data, mu, sigma):
        """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.
        :param data: The input data list, list.
        :param mu: The mean of the normal distribution, float.
        :param sigma: The standard deviation of the normal distribution, float.
        :return: The probability density function (PDF), list.
        """
        if sigma <= 0:
            raise ValueError("Standard deviation must be positive.")
        
        return [1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in data]