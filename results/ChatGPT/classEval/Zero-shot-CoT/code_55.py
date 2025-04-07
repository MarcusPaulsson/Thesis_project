class Manacher:
    """
    This is a class that implements a manacher algorithm to find the Longest palindromic substring in a given string.
    """

    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string
        self.processed_string = self._preprocess(input_string)
        self.palindrome_lengths = self._manacher_algorithm()

    def _preprocess(self, s):
        """
        Preprocess the string to insert separators.
        :param s: The original input string.
        :return: The processed string with separators.
        """
        return '|' + '|'.join(s) + '|'

    def _manacher_algorithm(self):
        """
        Implements the Manacher's algorithm to find the lengths of palindromes.
        :return: A list of lengths of palindromes centered at each character.
        """
        n = len(self.processed_string)
        lengths = [0] * n
        center = 0
        right = 0

        for i in range(n):
            mirror = 2 * center - i
            
            if i < right:
                lengths[i] = min(right - i, lengths[mirror])

            a, b = i + (1 + lengths[i]), i - (1 + lengths[i])
            while a < n and b >= 0 and self.processed_string[a] == self.processed_string[b]:
                lengths[i] += 1
                a += 1
                b -= 1

            if i + lengths[i] > right:
                center = i
                right = i + lengths[i]

        return lengths

    def palindromic_length(self, center, diff, string):
        """
        Recursively calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        """
        left = center - diff
        right = center + diff
        
        if left < 0 or right >= len(string):
            return 0
        
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1

        return (right - left - 1) // 2

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        max_length = max(self.palindrome_lengths)
        center_index = self.palindrome_lengths.index(max_length)
        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]

# Example for testing the implementation
if __name__ == "__main__":
    import unittest

    class ManacherTestPalindromicLength(unittest.TestCase):
        def test_palindromic_length(self):
            manacher = Manacher('ababa')
            self.assertEqual(manacher.palindromic_length(2, 1, 'a|b|a|b|a'), 2)

        def test_palindromic_length_2(self):
            manacher = Manacher('ababaxse')
            self.assertEqual(manacher.palindromic_length(2, 1, 'a|b|a|b|a|x|s|e'), 2)

        def test_palindromic_length_3(self):
            manacher = Manacher('ababax')
            self.assertEqual(manacher.palindromic_length(2, 3, 'a|b|a|b|a|x'), 0)

        def test_palindromic_length_4(self):
            manacher = Manacher('ababax')
            self.assertEqual(manacher.palindromic_length(9, 2, 'a|b|a|b|a|x'), 0)

        def test_palindromic_length_5(self):
            manacher = Manacher('ababax')
            self.assertEqual(manacher.palindromic_length(4, 1, 'a|b|a|b|a|x'), 4)

    class ManacherTestPalindromicString(unittest.TestCase):
        def test_palindromic_string(self):
            manacher = Manacher('ababaxse')
            self.assertEqual(manacher.palindromic_string(), 'ababa')

        def test_palindromic_string_2(self):
            manacher = Manacher('ababax')
            self.assertEqual(manacher.palindromic_string(), 'ababa')

        def test_palindromic_string_3(self):
            manacher = Manacher('ababax')
            self.assertEqual(manacher.palindromic_string(), 'ababa')

        def test_palindromic_string_4(self):
            manacher = Manacher('ababaxssss')
            self.assertEqual(manacher.palindromic_string(), 'ababa')

        def test_palindromic_string_5(self):
            manacher = Manacher('abab')
            self.assertEqual(manacher.palindromic_string(), 'aba')

    class ManacherTestMain(unittest.TestCase):
        def test_main(self):
            manacher = Manacher('ababa')
            self.assertEqual(manacher.palindromic_length(2, 1, 'a|b|a|b|a'), 2)
            self.assertEqual(manacher.palindromic_string(), 'ababa')

    unittest.main()