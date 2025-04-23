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
        """
        if m < 0 or m > n:
            return 0
        if m == 0 or m == n:
            return 1
        m = min(m, n - m)  # Optimization: C(n, m) = C(n, n-m)
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
        """
        if n < 0 or n > 63:
            return False
        if n == 63:
            return float("inf")
        return (1 << n) - 1 if n > 0 else 0

    def select(self, m: int) -> List[List[str]]:
        """
        Generate combinations with a specified number of elements.
        :param m: The number of elements in each combination,int.
        :return: A list of combinations,List[List[str]].
        """
        if m < 0 or m > len(self.datas):
            return []

        result = []
        self._select(0, [], m, result)
        return result

    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations of selecting elements from the given data list.
        :return: A list of combinations,List[List[str]].
        """
        result = []
        for i in range(1, len(self.datas) + 1):
            result.extend(self.select(i))
        return result

    def _select(self, start_index: int, current_combination: List[str], remaining: int, result: List[List[str]]):
        """
        Recursive helper function to generate combinations.
        :param start_index: The index to start selecting from.
        :param current_combination: The current combination being built.
        :param remaining: The number of elements remaining to be selected.
        :param result: The list to store the resulting combinations.
        """
        if remaining == 0:
            result.append(current_combination[:])  # Append a copy to avoid modification
            return

        if start_index >= len(self.datas):
            return

        # Include the current element
        current_combination.append(self.datas[start_index])
        self._select(start_index + 1, current_combination, remaining - 1, result)
        current_combination.pop()  # Backtrack: Remove the current element

        # Exclude the current element
        self._select(start_index + 1, current_combination, remaining, result)