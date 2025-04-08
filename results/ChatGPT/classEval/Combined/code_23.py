import math
from typing import List

class CombinationCalculator:
    """
    A class that provides methods to calculate and generate combinations
    from a list of data.
    """

    def __init__(self, data: List[str]):
        """
        Initialize the calculator with a list of data.
        :param data: List of elements from which to generate combinations.
        """
        self.data = data

    @staticmethod
    def count(n: int, m: int) -> int:
        """
        Calculate the number of combinations (n choose m).
        :param n: Total number of elements.
        :param m: Number of elements in each combination.
        :return: Number of combinations.
        """
        if m < 0 or m > n:
            return 0
        return math.comb(n, m)

    @staticmethod
    def count_all(n: int) -> int:
        """
        Calculate the number of all possible combinations.
        :param n: Total number of elements.
        :return: Number of all possible combinations.
        """
        if n < 0:
            return 0
        if n > 63:
            return float("inf")
        return (1 << n) - 1  # 2^n - 1

    def select(self, m: int) -> List[List[str]]:
        """
        Generate combinations of a specified size.
        :param m: Number of elements in each combination.
        :return: List of combinations.
        """
        if m < 0:
            return []
        result = []
        self._select_helper(0, [], m, result)
        return result

    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations of selecting elements from the data list.
        :return: List of all combinations.
        """
        result = []
        for m in range(1, len(self.data) + 1):
            self._select_helper(0, [], m, result)
        return result

    def _select_helper(self, start: int, current_combination: List[str], size: int, result: List[List[str]]):
        """
        Helper method to generate combinations using recursion.
        :param start: Current index in the data list.
        :param current_combination: Current combination being built.
        :param size: Size of the combination to generate.
        :param result: List to store all generated combinations.
        """
        if len(current_combination) == size:
            result.append(current_combination.copy())
            return

        for i in range(start, len(self.data)):
            current_combination.append(self.data[i])
            self._select_helper(i + 1, current_combination, size, result)
            current_combination.pop()