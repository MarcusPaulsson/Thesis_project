class Manacher:
    """
    This is a class that implements the Manacher algorithm to find the longest palindromic substring in a given string.
    """

    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string
        self.transformed_string = self._transform_string(input_string)
        self.palindrome_lengths = [0] * len(self.transformed_string)

    def _transform_string(self, s: str) -> str:
        """
        Transforms the input string to a new format with separators to handle even-length palindromes.
        :param s: The original string, str.
        :return: The transformed string with separators, str.
        """
        return '|' + '|'.join(s) + '|'

    def palindromic_length(self, center: int, diff: int, string: str) -> int:
        """
        Recursively calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        """
        left = center - diff
        right = center + diff
        while left >= 0 and right < len(string) and string[left] == string[right]:
            diff += 1
            left -= 1
            right += 1
        return diff - 1

    def palindromic_string(self) -> str:
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        max_len = 0
        center_index = 0
        for i in range(len(self.transformed_string)):
            length = self.palindromic_length(i, 0, self.transformed_string)
            self.palindrome_lengths[i] = length
            if length > max_len:
                max_len = length
                center_index = i

        start = (center_index - max_len) // 2
        return self.input_string[start:start + max_len]