class Manacher:
    """
    Finds the Longest Palindromic Substring in a given string using the Manacher's algorithm.
    """

    def __init__(self, input_string: str) -> None:
        """
        Initializes the Manacher class with the given input_string.

        Args:
            input_string: The input string to be searched.
        """
        self.input_string = input_string

    def _preprocess_string(self) -> str:
        """
        Preprocesses the input string by inserting '|' between characters and at the beginning and end.

        Returns:
            The preprocessed string.
        """
        return '^' + '|'.join(list(self.input_string)) + '$'

    def find_longest_palindrome(self) -> str:
        """
        Finds the longest palindromic substring in the given string using Manacher's algorithm.

        Returns:
            The longest palindromic substring. Returns an empty string if the input string is empty.
        """

        if not self.input_string:
            return ""

        processed_string = self._preprocess_string()
        n = len(processed_string)
        palindrome_radii = [0] * n  # Length of palindrome centered at each index
        center = 0  # Center of the rightmost palindrome found so far
        right_boundary = 0  # Right boundary of the rightmost palindrome found so far
        max_length = 0
        center_index = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i  # Mirror index of i with respect to center

            if i < right_boundary:
                palindrome_radii[i] = min(right_boundary - i, palindrome_radii[mirror])

            # Attempt to expand palindrome centered at i
            while processed_string[i + (1 + palindrome_radii[i])] == processed_string[i - (1 + palindrome_radii[i])]:
                palindrome_radii[i] += 1

            # If palindrome centered at i expands past right_boundary, adjust center and right_boundary
            if i + palindrome_radii[i] > right_boundary:
                center = i
                right_boundary = i + palindrome_radii[i]

            # Update maximum palindrome length and its center
            if palindrome_radii[i] > max_length:
                max_length = palindrome_radii[i]
                center_index = i

        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]