import math
from typing import List

class CombinationCalculator:
    """
    A class that provides methods to calculate combinations and generate combinations from a list of data.
    """

    def __init__(self, datas: List[str]):
        """
        Initialize the calculator with a list of data.
        :param datas: List of strings to generate combinations from.
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
        return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))

    @staticmethod
    def count_all(n: int) -> int:
        """
        Calculate the number of all possible combinations from n elements.
        :param n: Total number of elements.
        :return: The number of all possible combinations.
        """
        if n < 0:
            return False
        if n > 63:
            return float("inf")
        return (1 << n) - 1  # 2^n - 1

    def select(self, m: int) -> List[List[str]]:
        """
        Generate combinations with a specified number of elements.
        :param m: The number of elements in each combination.
        :return: A list of combinations.
        """
        if m < 0 or m > len(self.datas):
            return []
        result = []
        self._select(0, [None] * m, 0, result)
        return result

    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations of selecting elements from the given data list.
        :return: A list of combinations.
        """
        result = []
        for m in range(1, len(self.datas) + 1):
            result.extend(self.select(m))
        return result

    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
        """
        Generate combinations recursively.
        :param dataIndex: The index of the data to be selected.
        :param resultList: The current combination being built.
        :param resultIndex: The index of the current position in the combination.
        :param result: The list of all combinations generated.
        """
        if resultIndex == len(resultList):
            result.append(resultList.copy())
            return
        
        for i in range(dataIndex, len(self.datas)):
            resultList[resultIndex] = self.datas[i]
            self._select(i + 1, resultList, resultIndex + 1, result)