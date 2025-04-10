import math
from typing import List

class CombinationCalculator:
    """
    A class that provides methods to calculate the number of combinations 
    and generate combinations from a specified list of elements.
    """

    def __init__(self, datas: List[str]):
        """
        Initialize the calculator with a list of data.
        :param datas: List of elements to generate combinations from.
        """
        self.datas = datas

    @staticmethod
    def count(n: int, m: int) -> int:
        """
        Calculate the number of combinations of n items taken m at a time.
        :param n: Total number of elements.
        :param m: Number of elements in each combination.
        :return: The number of combinations.
        """
        if m < 0 or m > n:
            return 0
        return math.comb(n, m)

    @staticmethod
    def count_all(n: int) -> int:
        """
        Calculate the number of all possible combinations.
        :param n: Total number of elements.
        :return: The number of all possible combinations.
        """
        if n < 0:
            return 0
        if n > 63:
            return float("inf")
        return (1 << n) - 1  # 2^n - 1

    def select(self, m: int) -> List[List[str]]:
        """
        Generate combinations with a specified number of elements.
        :param m: The number of elements in each combination.
        :return: A list of combinations.
        """
        result = []
        self._select(0, [], m, result)
        return result

    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations from the given data list.
        :return: A list of all combinations.
        """
        result = []
        for m in range(1, len(self.datas) + 1):
            result.extend(self.select(m))
        return result

    def _select(self, dataIndex: int, currentCombination: List[str], m: int, result: List[List[str]]):
        """
        Helper method to generate combinations recursively.
        :param dataIndex: Current index in the data list to consider.
        :param currentCombination: Current combination being built.
        :param m: Number of elements to select.
        :param result: List to store all combinations.
        """
        if len(currentCombination) == m:
            result.append(currentCombination.copy())
            return
        
        for i in range(dataIndex, len(self.datas)):
            currentCombination.append(self.datas[i])
            self._select(i + 1, currentCombination, m, result)
            currentCombination.pop()