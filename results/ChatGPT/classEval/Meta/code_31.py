import math
from typing import List

class DataStatistics4:
    """
    This is a class that performs advanced mathematical calculations and statistics,
    including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
    """

    @staticmethod
    def correlation_coefficient(data1: List[float], data2: List[float]) -> float:
        n = len(data1)
        if n != len(data2):
            raise ValueError("Data sets must have the same length.")
        
        mean1 = sum(data1) / n
        mean2 = sum(data2) / n
        
        numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
        denominator = math.sqrt(sum((data1[i] - mean1) ** 2 for i in range(n)) * sum((data2[i] - mean2) ** 2 for i in range(n)))
        
        if denominator == 0:
            raise ValueError("Denominator is zero, correlation cannot be computed.")
        
        return numerator / denominator

    @staticmethod
    def skewness(data: List[float]) -> float:
        n = len(data)
        mean = sum(data) / n
        m3 = sum((x - mean) ** 3 for x in data) / n
        m2 = sum((x - mean) ** 2 for x in data) / n
        
        if m2 == 0:
            raise ValueError("Variance is zero, skewness cannot be computed.")
        
        return m3 / (m2 ** (3/2))

    @staticmethod
    def kurtosis(data: List[float]) -> float:
        n = len(data)
        mean = sum(data) / n
        m4 = sum((x - mean) ** 4 for x in data) / n
        m2 = sum((x - mean) ** 2 for x in data) / n
        
        if m2 == 0:
            raise ValueError("Variance is zero, kurtosis cannot be computed.")
        
        return (m4 / (m2 ** 2)) - 3

    @staticmethod
    def pdf(data: List[float], mu: float, sigma: float) -> List[float]:
        if sigma <= 0:
            raise ValueError("Standard deviation must be positive.")
        
        pdf_values = []
        for x in data:
            coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
            exponent = -0.5 * ((x - mu) / sigma) ** 2
            pdf_values.append(coefficient * math.exp(exponent))
        
        return pdf_values