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
        if center - diff < 0 or center + diff >= len(string):
            return 0

        if string[center - diff] == string[center + diff]:
            return diff
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
        s = '#'.join(self.input_string)
        s = '#' + s + '#'
        n = len(s)
        p = [0] * n
        center = 0
        right = 0
        max_len = 0
        max_center = 0

        for i in range(1, n):
            if i < right:
                mirror = 2 * center - i
                p[i] = min(right - i, p[mirror])

            # Attempt to expand palindrome centered at i
            left = i - (1 + p[i])
            right_side = i + (1 + p[i])
            while left >= 0 and right_side < n and s[left] == s[right_side]:
                p[i] += 1
                left -= 1
                right_side += 1

            # If palindrome centered at i expands past right,
            # adjust center based on expanded palindrome.
            if i + p[i] > right:
                center = i
                right = i + p[i]

            # Update max_len and max_center if needed
            if p[i] > max_len:
                max_len = p[i]
                max_center = i

        start = (max_center - max_len) // 2
        return self.input_string[start:start + max_len]