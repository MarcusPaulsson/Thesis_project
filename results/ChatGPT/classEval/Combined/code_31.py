import math
from statistics import mean, stdev

class DataStatistics:
    """
    A class that performs advanced mathematical calculations and statistics, 
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
        :raises ValueError: If the lengths of data1 and data2 are not equal.
        """
        if len(data1) != len(data2):
            raise ValueError("Data sets must have the same length.")
        
        n = len(data1)
        mean1, mean2 = mean(data1), mean(data2)
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
            return float('nan')

        mean_value = mean(data)
        std_dev = stdev(data)
        skew = (sum((x - mean_value) ** 3 for x in data) / n) / (std_dev ** 3)
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
            return float('nan')

        mean_value = mean(data)
        std_dev = stdev(data)
        kurt = (sum((x - mean_value) ** 4 for x in data) / n) / (std_dev ** 4) - 3
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
        coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
        return [coefficient * math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in data]