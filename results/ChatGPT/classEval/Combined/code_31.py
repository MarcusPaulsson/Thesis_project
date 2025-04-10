import math
from typing import List, Union

class DataStatistics4:
    """
    A class to perform advanced statistical calculations including correlation coefficient,
    skewness, kurtosis, and the probability density function (PDF) for a normal distribution.
    """

    @staticmethod
    def correlation_coefficient(data1: List[float], data2: List[float]) -> float:
        """
        Calculate the correlation coefficient of two sets of data.
        :param data1: The first set of data.
        :param data2: The second set of data.
        :return: The correlation coefficient.
        """
        n = len(data1)
        if n == 0:
            return float('nan')
        
        mean1, mean2 = sum(data1) / n, sum(data2) / n
        numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
        denominator = math.sqrt(sum((data1[i] - mean1) ** 2 for i in range(n)) * 
                                 sum((data2[i] - mean2) ** 2 for i in range(n)))
        return numerator / denominator if denominator != 0 else 0.0

    @staticmethod
    def skewness(data: List[float]) -> float:
        """
        Calculate the skewness of a set of data.
        :param data: The input data list.
        :return: The skewness.
        """
        n = len(data)
        if n < 2:
            return float('nan')

        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        if variance == 0:
            return 0.0
        
        skew = (sum((x - mean) ** 3 for x in data) / n) / (variance ** 1.5)
        return skew

    @staticmethod
    def kurtosis(data: List[float]) -> float:
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list.
        :return: The kurtosis.
        """
        n = len(data)
        if n < 2:
            return float('nan')

        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        if variance == 0:
            return float('nan')

        kurt = (sum((x - mean) ** 4 for x in data) / n) / (variance ** 2) - 3
        return kurt

    @staticmethod
    def pdf(data: List[float], mu: float, sigma: float) -> List[float]:
        """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.
        :param data: The input data list.
        :param mu: The mean of the normal distribution.
        :param sigma: The standard deviation of the normal distribution.
        :return: The probability density function values.
        :raises ValueError: If sigma is non-positive.
        """
        if sigma <= 0:
            raise ValueError("Standard deviation must be positive.")
        
        return [(1 / (sigma * math.sqrt(2 * math.pi))) * 
                math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in data]