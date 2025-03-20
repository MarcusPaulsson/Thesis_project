import math
from typing import List

class CombinationCalculator:
    """
    This is a class that provides methods to calculate the number of combinations for a specific count, calculate all possible combinations, and generate combinations with a specified number of elements.
    """

    def __init__(self, datas: List[str]):
        """
        Initialize the calculator with a list of data.
        """
        self.datas = datas

    @staticmethod
    def count(n: int, m: int) -> int:
        """
        Calculate the number of combinations for a specific count.
        :param n: The total number of elements,int.
        :param m: The number of elements in each combination,int.
        :return: The number of combinations,int.
        >>> CombinationCalculator.count(4, 2)
        6
        """
        if m < 0 or m > n:
            return 0
        if m == 0 or m == n:
            return 1
        if m > n // 2:
            m = n - m
        result = 1
        for i in range(m):
            result = result * (n - i) // (i + 1)
        return result

    @staticmethod
    def count_all(n: int) -> int:
        """
        Calculate the number of all possible combinations.
        :param n: The total number of elements,int.
        :return: The number of all possible combinations,int,if the number of combinations is greater than 2^63-1,return float("inf").
        >>> CombinationCalculator.count_all(4)
        15
        """
        if n > 62:
            return float("inf")
        return (1 << n) - 1

    def select(self, m: int) -> List[List[str]]:
        """
        Generate combinations with a specified number of elements.
        :param m: The number of elements in each combination,int.
        :return: A list of combinations,List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select(2)
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

        """
        result = []
        self._select(0, [None] * m, 0, result)
        return result

    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations of  selecting elements from the given data list,and it uses the select method.
        :return: A list of combinations,List[List[str]].
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select_all()
        [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]

        """
        result = []
        for i in range(1, len(self.datas) + 1):
            result.extend(self.select(i))
        return result

    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
        """
        Generate combinations with a specified number of elements by recursion.
        :param dataIndex: The index of the data to be selected,int.
        :param resultList: The list of elements in the combination,List[str].
        :param resultIndex: The index of the element in the combination,int.
        :param result: The list of combinations,List[List[str]].
        :return: None.
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> result = []
        >>> calc._select(0, [None] * 2, 0, result)
        >>> result
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]

        """
        if resultIndex == len(resultList):
            result.append([item for item in resultList])
            return

        for i in range(dataIndex, len(self.datas)):
            resultList[resultIndex] = self.datas[i]
            self._select(i + 1, resultList, resultIndex + 1, result)