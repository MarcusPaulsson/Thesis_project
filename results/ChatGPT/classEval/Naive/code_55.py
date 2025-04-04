class Manacher:
    """
    This class implements the Manacher algorithm to find the longest palindromic substring in a given string.
    """

    def __init__(self, input_string: str) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input string to be searched, str.
        """
        self.input_string = input_string

    def preprocess_string(self) -> str:
        """
        Preprocesses the input string by inserting a delimiter between characters.
        :return: Preprocessed string, str.
        """
        return '|' + '|'.join(self.input_string) + '|'

    def longest_palindromic_substring(self) -> str:
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        processed = self.preprocess_string()
        n = len(processed)
        p = [0] * n
        center = right = 0

        for i in range(n):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            a, b = i + (1 + p[i]), i - (1 + p[i])
            while a < n and b >= 0 and processed[a] == processed[b]:
                p[i] += 1
                a += 1
                b -= 1

            if i + p[i] > right:
                center, right = i, i + p[i]

        max_length = max(p)
        center_index = p.index(max_length)

        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]

# Example usage:
# manacher = Manacher('ababa')
# print(manacher.longest_palindromic_substring())  # Output: 'ababa'