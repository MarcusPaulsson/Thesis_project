class Manacher:
    """
    Finds the longest palindromic substring in a given string using the Manacher's algorithm.
    """

    def __init__(self, input_string: str) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

    def _preprocess_string(self) -> str:
        """
        Preprocesses the input string by inserting a special character '|' between each character and at the beginning and end.
        This ensures that palindromes of even length are also handled correctly.
        :return: The preprocessed string.
        """
        return '|'.join(['^'] + list(self.input_string) + ['$'])

    def palindromic_length(self, center: int, diff: int, string: str) -> int:
        """
         Calculates the length of the palindromic substring centered at a given position in a string.

         This function iteratively expands outwards from the center, checking if the characters at equal distances
         from the center are the same.  It stops when it encounters the boundaries of the string or when the
         characters are no longer equal.

         :param center: The index of the center of the potential palindrome in the string.
         :param diff:  The offset from the center to compare characters.  It starts at 1 and increments in each iteration.
         :param string: The string in which to check for the palindromic length.
         :return: The length of the palindrome centered at the given position.  Returns 0 if the input is invalid,
                  or if no palindrome can be formed at the given center.
         >>> manacher = Manacher('ababa')
         >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
         2
         """
        left = center - diff
        right = center + diff

        if left < 0 or right >= len(string):
            return 0

        if string[left] == string[right]:
            return self.palindromic_length(center, diff + 1, string) + 1
        else:
            return 0

    def palindromic_string(self) -> str:
        """
        Finds the longest palindromic substring in the given string using Manacher's Algorithm.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'
        """
        processed_string = self._preprocess_string()
        n = len(processed_string)
        palindrome_radii = [0] * n
        center = 0
        right_boundary = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right_boundary:
                palindrome_radii[i] = min(right_boundary - i, palindrome_radii[mirror])

            # Attempt to expand palindrome centered at i
            while processed_string[i + (1 + palindrome_radii[i])] == processed_string[i - (1 + palindrome_radii[i])]:
                palindrome_radii[i] += 1

            # If palindrome centered at i expands past right_boundary,
            # adjust center based on expanded palindrome.
            if i + palindrome_radii[i] > right_boundary:
                center = i
                right_boundary = i + palindrome_radii[i]

        # Find the maximum element in palindrome_radii
        max_len = max(palindrome_radii)
        center_index = palindrome_radii.index(max_len)

        start = (center_index - max_len) // 2
        return self.input_string[start: start + max_len]