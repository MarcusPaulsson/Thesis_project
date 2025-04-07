from typing import List
import math

class CombinationCalculator:
    """
    This class provides methods to calculate combinations.
    """

    def __init__(self, data: List[str]):
        """
        Initializes the CombinationCalculator with a list of data.
        """
        if not isinstance(data, list):
            raise TypeError("Data must be a list.")
        if not all(isinstance(item, str) for item in data):
            raise TypeError("All elements in data must be strings.")
        self.data = data

    @staticmethod
    def count(n: int, k: int) -> int:
        """
        Calculates the number of combinations (n choose k).
        """
        if not isinstance(n, int) or not isinstance(k, int):
            raise TypeError("n and k must be integers.")
        if n < 0 or k < 0:
            raise ValueError("n and k must be non-negative.")
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        if k > n // 2:
            k = n - k

        result = 1
        for i in range(k):
            result = result * (n - i) // (i + 1)
        return result

    @staticmethod
    def count_all(n: int) -> int:
        """
        Calculates the total number of combinations (excluding the empty set).
        """
        if not isinstance(n, int):
            raise TypeError("n must be an integer.")
        if n < 0:
            raise ValueError("n must be non-negative.")

        if n > 62:
            return float('inf')
        return (1 << n) - 1

    def select(self, k: int) -> List[List[str]]:
        """
        Generates all combinations of k elements from the data.
        """
        if not isinstance(k, int):
            raise TypeError("k must be an integer.")
        if k <= 0 or k > len(self.data):
            return []

        combinations: List[List[str]] = []
        self._generate_combinations(0, k, [], combinations)
        return combinations

    def select_all(self) -> List[List[str]]:
        """
        Generates all possible combinations (excluding the empty set).
        """
        all_combinations: List[List[str]] = []
        for k in range(1, len(self.data) + 1):
            all_combinations.extend(self.select(k))
        return all_combinations

    def _generate_combinations(self, start_index: int, k: int, current_combination: List[str], all_combinations: List[List[str]]):
        """
        Recursive helper function to generate combinations.
        """
        if len(current_combination) == k:
            all_combinations.append(current_combination.copy())  # Append a copy
            return

        for i in range(start_index, len(self.data)):
            current_combination.append(self.data[i])
            self._generate_combinations(i + 1, k, current_combination, all_combinations)
            current_combination.pop()  # Backtrack