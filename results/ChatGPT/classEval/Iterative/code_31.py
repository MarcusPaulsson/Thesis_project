import math
from statistics import mean, pstdev

class DataStatistics4:
    """
    This is a class that performs advanced mathematical calculations and statistics,
    including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
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
            raise ValueError("Input lists must have the same non-zero length.")
        
        mean1 = mean(data1)
        mean2 = mean(data2)
        numerator = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2))
        denominator = math.sqrt(sum((x - mean1) ** 2 for x in data1) * sum((y - mean2) ** 2 for y in data2))
        
        if denominator == 0:
            return 0  # Handle case of constant data
        return numerator / denominator

    @staticmethod
    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        """
        n = len(data)
        if n < 2:
            return float('nan')  # Not enough data to calculate skewness
        
        mean_data = mean(data)
        std_dev = pstdev(data)
        
        if std_dev == 0:
            return float('nan')  # Handle case of constant data
        
        skewness = sum((x - mean_data) ** 3 for x in data) / (n * std_dev ** 3)
        return skewness

    @staticmethod
    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        """
        n = len(data)
        if n < 2:
            return float('nan')  # Not enough data to calculate kurtosis
        
        mean_data = mean(data)
        std_dev = pstdev(data)
        
        if std_dev == 0:
            return float('nan')  # Handle case of constant data
        
        kurtosis = sum((x - mean_data) ** 4 for x in data) / (n * std_dev ** 4) - 3
        return kurtosis

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
        
        pdf_values = [(1 / (sigma * math.sqrt(2 * math.pi))) * 
                      math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in data]
        return pdf_values