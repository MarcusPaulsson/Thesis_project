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
        sum1 = sum(data1)
        sum2 = sum(data2)
        sum1_sq = sum(x ** 2 for x in data1)
        sum2_sq = sum(x ** 2 for x in data2)
        p_sum = sum(data1[i] * data2[i] for i in range(n))

        num = p_sum - (sum1 * sum2 / n)
        den = math.sqrt((sum1_sq - (sum1 ** 2) / n) * (sum2_sq - (sum2 ** 2) / n))
        return num / den if den != 0 else 0

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
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        sd = math.sqrt(variance)
        skew = (sum((x - mean) ** 3 for x in data) / n) / (sd ** 3)
        return skew

    @staticmethod
    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        >>> DataStatistics4.kurtosis([1, 20, 100])
        -1.5000000000000007
        """
        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        sd = math.sqrt(variance)
        kurt = (sum((x - mean) ** 4 for x in data) / n) / (sd ** 4) - 3
        return kurt

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
        pdf_values = [(1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in data]
        return pdf_values