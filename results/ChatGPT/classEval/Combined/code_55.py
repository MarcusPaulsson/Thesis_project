class Manacher:
    """
    This class implements the Manacher algorithm to find the longest palindromic substring in a given string.
    """

    def __init__(self, input_string: str) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input string to be searched.
        """
        self.input_string = input_string
        self.processed_string = self._preprocess(input_string)
        self.palindrome_lengths = self._manacher_algorithm()

    def _preprocess(self, string: str) -> str:
        """
        Preprocess the input string to insert special characters for palindrome checking.
        :param string: The string to be processed.
        :return: The processed string with separators.
        """
        return '|' + '|'.join(string) + '|'

    def _manacher_algorithm(self) -> list:
        """
        Implements the Manacher's algorithm to find the lengths of palindromes.
        :return: A list of lengths of the palindromes centered at each character.
        """
        n = len(self.processed_string)
        lengths = [0] * n
        center, right = 0, 0
        
        for i in range(n):
            mirror = 2 * center - i
            if i < right:
                lengths[i] = min(right - i, lengths[mirror])

            # Expand around the center
            left, right = i - (lengths[i] + 1), i + (lengths[i] + 1)
            while left >= 0 and right < n and self.processed_string[left] == self.processed_string[right]:
                lengths[i] += 1
                left -= 1
                right += 1

            # Update center and right boundary
            if i + lengths[i] > right:
                center, right = i, i + lengths[i]

        return lengths

    def palindromic_length(self, center: int, diff: int) -> int:
        """
        Returns the length of the palindromic substring based on a given center and difference.
        :param center: The center of the palindromic substring.
        :param diff: The difference between the center and the current position.
        :return: The length of the palindromic substring.
        """
        left = center - diff
        right = center + diff
        while left >= 0 and right < len(self.processed_string) and self.processed_string[left] == self.processed_string[right]:
            left -= 1
            right += 1
        return (right - 1) - (left + 1) + 1

    def palindromic_string(self) -> str:
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring.
        """
        max_length = max(self.palindrome_lengths)
        center_index = self.palindrome_lengths.index(max_length)
        
        # Calculate the start index of the palindrome in the original string
        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]

