import math
from typing import List

class CombinationCalculator:
    """
    This is a class that provides methods to calculate the number of combinations for a specific count,
    calculate all possible combinations, and generate combinations with a specified number of elements.
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
        :param n: The total number of elements.
        :param m: The number of elements in each combination.
        :return: The number of combinations.
        >>> CombinationCalculator.count(4, 2)
        6
        """
        if m > n or m < 0:
            return 0
        return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))

    @staticmethod
    def count_all(n: int) -> int:
        """
        Calculate the number of all possible combinations.
        :param n: The total number of elements.
        :return: The number of all possible combinations.
        >>> CombinationCalculator.count_all(4)
        15
        """
        total_combinations = 0
        for m in range(1, n + 1):
            total_combinations += CombinationCalculator.count(n, m)
        
        return total_combinations if total_combinations <= (2**63 - 1) else float("inf")

    def select(self, m: int) -> List[List[str]]:
        """
        Generate combinations with a specified number of elements.
        :param m: The number of elements in each combination.
        :return: A list of combinations.
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select(2)
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]
        """
        result = []
        self._select(0, [], m, result)
        return result

    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations of selecting elements from the given data list.
        :return: A list of combinations.
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> calc.select_all()
        [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]
        """
        result = []
        for m in range(1, len(self.datas) + 1):
            result.extend(self.select(m))
        return result

    def _select(self, dataIndex: int, resultList: List[str], m: int, result: List[List[str]]):
        """
        Generate combinations with a specified number of elements by recursion.
        :param dataIndex: The index of the data to be selected.
        :param resultList: The list of elements in the combination.
        :param m: The number of elements in each combination.
        :param result: The list of combinations.
        :return: None.
        >>> calc = CombinationCalculator(["A", "B", "C", "D"])
        >>> result = []
        >>> calc._select(0, [], 2, result)
        >>> result
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]
        """
        if len(resultList) == m:
            result.append(resultList.copy())
            return
        
        for i in range(dataIndex, len(self.datas)):
            resultList.append(self.datas[i])
            self._select(i + 1, resultList, m, result)
            resultList.pop()