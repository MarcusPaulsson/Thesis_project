import math
from typing import List, Optional

class DataStatistics4:
    """
    This class performs advanced mathematical calculations and statistics,
    including correlation coefficient, skewness, kurtosis, and probability density
    function (PDF) for a normal distribution.
    """

    @staticmethod
    def correlation_coefficient(data1: List[float], data2: List[float]) -> float:
        n = len(data1)
        if n != len(data2) or n == 0:
            raise ValueError("Input data must be of the same length and non-empty.")
        
        mean1, mean2 = sum(data1) / n, sum(data2) / n
        numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
        denominator = math.sqrt(sum((data1[i] - mean1) ** 2 for i in range(n)) * 
                                 sum((data2[i] - mean2) ** 2 for i in range(n)))
        return numerator / denominator if denominator != 0 else 0.0

    @staticmethod
    def skewness(data: List[float]) -> float:
        n = len(data)
        if n < 3:
            return float('nan')

        mean = sum(data) / n
        m3 = sum((x - mean) ** 3 for x in data) / n
        m2 = sum((x - mean) ** 2 for x in data) / n
        return (n * m3) / ((n - 1) * (n - 2) * (m2 ** (3/2))) if m2 != 0 else 0.0

    @staticmethod
    def kurtosis(data: List[float]) -> float:
        n = len(data)
        if n < 4:
            return float('nan')

        mean = sum(data) / n
        m4 = sum((x - mean) ** 4 for x in data) / n
        m2 = sum((x - mean) ** 2 for x in data) / n
        return (n * (n + 1) * m4) / ((n - 1) * (n - 2) * (n - 3) * (m2 ** 2)) - (3 * ((n - 1) ** 2)) / ((n - 2) * (n - 3))

    @staticmethod
    def pdf(data: List[float], mu: float, sigma: float) -> List[float]:
        if sigma <= 0:
            raise ValueError("Standard deviation must be positive.")

        coeff = 1 / (sigma * math.sqrt(2 * math.pi))
        return [coeff * math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in data]