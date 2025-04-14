class Manacher:
    """
    This is a class that implements the Manacher algorithm to find the longest palindromic substring in a given string.
    """

    def __init__(self, input_string: str) -> None:
        """
        Initializes the Manacher class with the given input_string.

        :param input_string: The input string to be searched, str.
        """
        self.input_string = input_string

    def palindromic_length(self, center: int, diff: int, string: str) -> int:
        """
        Calculates the length of the palindromic substring based on a given center and difference.
        This iterative approach avoids recursion and potential stack overflow issues.

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

    def palindromic_string(self) -> str:
        """
        Finds the longest palindromic substring in the given string using the Manacher's algorithm.

        :return: The longest palindromic substring, str.
        """
        # Preprocess the string to handle even length palindromes
        processed_string = '#' + '#'.join(self.input_string) + '#'
        n = len(processed_string)
        palindrome_radii = [0] * n  # Array to store palindrome radii centered at each index
        center = 0  # Center of the current rightmost palindrome
        right = 0  # Right boundary of the current rightmost palindrome
        max_len = 0  # Length of the longest palindrome found so far
        max_center = 0  # Center of the longest palindrome found so far

        for i in range(n):
            # Utilize symmetry to initialize palindrome_radii[i]
            mirror = 2 * center - i
            if right > i:
                palindrome_radii[i] = min(right - i, palindrome_radii[mirror])

            # Expand palindrome centered at i
            left = i - (1 + palindrome_radii[i])
            right_bound = i + (1 + palindrome_radii[i])
            while left >= 0 and right_bound < n and processed_string[left] == processed_string[right_bound]:
                palindrome_radii[i] += 1
                left -= 1
                right_bound += 1

            # Update center and right boundary if palindrome centered at i expands past right
            if i + palindrome_radii[i] > right:
                center = i
                right = i + palindrome_radii[i]

            # Update max_len and max_center
            if palindrome_radii[i] > max_len:
                max_len = palindrome_radii[i]
                max_center = i

        # Extract the longest palindromic substring from the original string
        start = (max_center - max_len) // 2
        return self.input_string[start: start + max_len]