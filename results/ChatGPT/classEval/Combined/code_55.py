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
        self.processed_string = self._preprocess_string(input_string)
        self.palindrome_lengths = [0] * len(self.processed_string)

    def _preprocess_string(self, string: str) -> str:
        """
        Preprocesses the input string to insert separators for uniform palindrome length calculation.
        :param string: The original input string.
        :return: The processed string with separators.
        """
        return '|' + '|'.join(string) + '|'

    def _expand_around_center(self, center: int, diff: int) -> int:
        """
        Expands around the given center and difference to find the length of the palindromic substring.
        :param center: The center of the palindromic substring.
        :param diff: The difference between the center and the current position.
        :return: The length of the palindromic substring.
        """
        left = center - diff
        right = center + diff
        while left >= 0 and right < len(self.processed_string) and self.processed_string[left] == self.processed_string[right]:
            left -= 1
            right += 1
        return (right - left - 1) // 2

    def find_longest_palindromic_substring(self) -> str:
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring.
        """
        max_length = 0
        start_index = 0

        for i in range(len(self.processed_string)):
            length = self._expand_around_center(i, 0)
            self.palindrome_lengths[i] = length

            if length > max_length:
                max_length = length
                start_index = i - length

        # Extract the longest palindromic substring from the original string
        start = (start_index - max_length) // 2
        return self.input_string[start:start + max_length]