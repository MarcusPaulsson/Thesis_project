import math
from typing import List

class CombinationCalculator:
    """
    This class provides methods to calculate combinations.
    """

    def __init__(self, datas: List[str]):
        """
        Initializes the calculator with a list of data.

        Args:
            datas: The list of data elements.
        """
        self.datas = datas

    @staticmethod
    def count(n: int, m: int) -> int:
        """
        Calculates the number of combinations (n choose m).

        Args:
            n: The total number of elements.
            m: The number of elements to choose.

        Returns:
            The number of combinations.
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
        Calculates the total number of combinations (including the empty set).

        Args:
            n: The total number of elements.

        Returns:
            The total number of combinations (2^n - 1).  Returns float("inf") if n is 63. Returns False if n < 0 or n > 63.
        """
        if n < 0 or n > 63:
            return False
        if n == 63:
            return float("inf")
        return (1 << n) - 1

    def select(self, m: int) -> List[List[str]]:
        """
        Generates all combinations of size m from the data.

        Args:
            m: The size of the combinations to generate.

        Returns:
            A list of lists, where each inner list is a combination.
        """
        if m < 0 or m > len(self.datas):
            return []

        result = []
        self._select_recursive(0, m, [], result)
        return result

    def select_all(self) -> List[List[str]]:
        """
        Generates all possible non-empty combinations from the data.

        Returns:
            A list of lists, where each inner list is a combination.
        """
        result = []
        for i in range(1, len(self.datas) + 1):
            result.extend(self.select(i))
        return result

    def _select_recursive(self, start_index: int, m: int, current_combination: List[str], result: List[List[str]]):
        """
        Recursive helper function to generate combinations.

        Args:
            start_index: The starting index in the data list.
            m: The remaining number of elements to choose.
            current_combination: The current combination being built.
            result: The list to store the resulting combinations.
        """
        if m == 0:
            result.append(current_combination[:])  # Append a copy
            return

        for i in range(start_index, len(self.datas)):
            current_combination.append(self.datas[i])
            self._select_recursive(i + 1, m - 1, current_combination, result)
            current_combination.pop()
    
    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
        """
        Generate combinations with a specified number of elements by recursion.
        :param dataIndex: The index of the data to be selected,int.
        :param resultList: The list of elements in the combination,List[str].
        :param resultIndex: The index of the element in the combination,int.
        :param result: The list of combinations,List[List[str]].
        :return: None.
        """
        if resultIndex == len(resultList):
            temp = resultList[:]
            temp2 = []
            for i in temp:
                if i is not None:
                  temp2.append(i)
            if len(temp2) > 0:
              result.append(temp2)
            return

        if dataIndex >= len(self.datas):
            return
        
        resultList[resultIndex] = self.datas[dataIndex]
        self._select(dataIndex + 1, resultList, resultIndex + 1, result)
        resultList[resultIndex] = None
        self._select(dataIndex + 1, resultList, resultIndex, result)