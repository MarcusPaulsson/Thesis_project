class Manacher:
    """
    This class implements the Manacher algorithm to find the Longest Palindromic Substring in a given string.
    """

    def __init__(self, input_string: str) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input string to be searched, str.
        """
        self.input_string = input_string

    def _palindromic_length(self, center: int, diff: int, string: str) -> int:
        """
        Calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        """
        left = center - diff
        right = center + diff
        length = 0
        
        while left >= 0 and right < len(string) and string[left] == string[right]:
            length += 1
            left -= 1
            right += 1
        
        return length

    def longest_palindromic_substring(self) -> str:
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        # Pre-process the input string to handle even-length palindromes
        modified_string = '#' + '#'.join(self.input_string) + '#'
        n = len(modified_string)
        max_len = 0
        center_index = 0

        for i in range(n):
            current_length = self._palindromic_length(i, 0, modified_string)

            if current_length > max_len:
                max_len = current_length
                center_index = i

        start = (center_index - max_len) // 2
        return self.input_string[start:start + max_len]

