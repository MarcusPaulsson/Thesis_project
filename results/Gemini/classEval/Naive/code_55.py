class Manacher:
    """
    his is a class that implements a manacher algorithm to find the Longest palindromic substring in a given string.
    """

    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        """
        Recursively calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        >>> manacher = Manacher('ababa')
        >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
        2

        """
        if (center - diff >= 0 and center + diff < len(string) and string[center - diff] == string[center + diff]):
            return 1 + self.palindromic_length(center, diff + 1, string)
        else:
            return 0

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        modified_string = '|'.join('$' + self.input_string + '#')
        length = len(modified_string)
        palindrome_radii = [0] * length
        center = 0
        right_boundary = 0

        for i in range(1, length - 1):
            mirror = 2 * center - i

            if right_boundary > i:
                palindrome_radii[i] = min(right_boundary - i, palindrome_radii[mirror])

            # Attempt to expand palindrome centered at i
            while modified_string[i + (1 + palindrome_radii[i])] == modified_string[i - (1 + palindrome_radii[i])]:
                palindrome_radii[i] += 1

            # If palindrome centered at i expands past right_boundary,
            # adjust center based on expanded palindrome.
            if i + palindrome_radii[i] > right_boundary:
                center = i
                right_boundary = i + palindrome_radii[i]

        # Find the maximum element in palindrome_radii
        max_len = max(palindrome_radii)

        # Find the center index of the longest palindrome
        center_index = palindrome_radii.index(max_len)

        start = (center_index - max_len) // 2
        return self.input_string[start:start + max_len]