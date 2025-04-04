import math
from statistics import mean, stdev

class DataStatistics4:
    """
    This class performs advanced mathematical calculations and statistics,
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
        n = len(data1)
        if n != len(data2):
            raise ValueError("Data lists must have the same length.")
        
        mean1, mean2 = mean(data1), mean(data2)
        numerator = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2))
        denominator = math.sqrt(sum((x - mean1) ** 2 for x in data1) * sum((y - mean2) ** 2 for y in data2))
        
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
            raise ValueError("At least three data points are required.")
        
        mean_val = mean(data)
        std_dev = stdev(data)
        skew = (n / ((n - 1) * (n - 2))) * sum(((x - mean_val) / std_dev) ** 3 for x in data)
        
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
            raise ValueError("At least four data points are required.")
        
        mean_val = mean(data)
        std_dev = stdev(data)
        kurt = (n * (n + 1) * sum(((x - mean_val) / std_dev) ** 4 for x in data) - 3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
        
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
        
        pdf_values = [(1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) for x in data]
        
        return pdf_values