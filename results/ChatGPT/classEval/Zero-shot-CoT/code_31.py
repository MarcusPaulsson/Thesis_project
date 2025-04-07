import math
from statistics import mean, stdev

class DataStatistics4:
    """
    This is a class that performs advanced mathematical calculations and statistics, including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
    """

    @staticmethod
    def correlation_coefficient(data1, data2):
        """Calculate the correlation coefficient of two sets of data."""
        n = len(data1)
        if n != len(data2):
            raise ValueError("Data sets must have the same length.")
        
        mean1, mean2 = mean(data1), mean(data2)
        numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
        denominator = math.sqrt(sum((data1[i] - mean1) ** 2 for i in range(n)) * 
                                 sum((data2[i] - mean2) ** 2 for i in range(n)))
        return numerator / denominator if denominator != 0 else 0

    @staticmethod
    def skewness(data):
        """Calculate the skewness of a set of data."""
        n = len(data)
        if n < 3:
            return float('nan')

        mean_value = mean(data)
        stdev_value = stdev(data)
        skewness_value = (sum((x - mean_value) ** 3 for x in data) / n) / (stdev_value ** 3)
        return skewness_value

    @staticmethod
    def kurtosis(data):
        """Calculate the kurtosis of a set of data."""
        n = len(data)
        if n < 3:
            return float('nan')

        mean_value = mean(data)
        stdev_value = stdev(data)
        kurtosis_value = (sum((x - mean_value) ** 4 for x in data) / n) / (stdev_value ** 4) - 3
        return kurtosis_value

    @staticmethod
    def pdf(data, mu, sigma):
        """Calculate the probability density function (PDF) of a set of data under a normal distribution."""
        pdf_values = [(1 / (sigma * math.sqrt(2 * math.pi))) * 
                      math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in data]
        return pdf_values