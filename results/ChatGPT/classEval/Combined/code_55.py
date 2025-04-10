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
        self.processed_string = self._preprocess(input_string)
        self.palindrome_lengths = self._manacher_algorithm()

    def _preprocess(self, string: str) -> str:
        """
        Preprocess the input string to insert special characters for palindrome checking.
        :param string: The string to be processed.
        :return: The processed string with separators.
        """
        return '|' + '|'.join(string) + '|'

    def _manacher_algorithm(self) -> list:
        """
        Implements the Manacher's algorithm to find the lengths of palindromes.
        :return: A list of lengths of the palindromes centered at each character.
        """
        n = len(self.processed_string)
        lengths = [0] * n
        center, right = 0, 0
        
        for i in range(n):
            mirror = 2 * center - i
            if i < right:
                lengths[i] = min(right - i, lengths[mirror])

            # Expand around the center
            left, right = i - (lengths[i] + 1), i + (lengths[i] + 1)
            while left >= 0 and right < n and self.processed_string[left] == self.processed_string[right]:
                lengths[i] += 1
                left -= 1
                right += 1

            # Update center and right boundary
            if i + lengths[i] > right:
                center, right = i, i + lengths[i]

        return lengths

    def palindromic_length(self, center: int, diff: int) -> int:
        """
        Returns the length of the palindromic substring based on a given center and difference.
        :param center: The center of the palindromic substring.
        :param diff: The difference between the center and the current position.
        :return: The length of the palindromic substring.
        """
        left = center - diff
        right = center + diff
        while left >= 0 and right < len(self.processed_string) and self.processed_string[left] == self.processed_string[right]:
            left -= 1
            right += 1
        return (right - 1) - (left + 1) + 1

    def palindromic_string(self) -> str:
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring.
        """
        max_length = max(self.palindrome_lengths)
        center_index = self.palindrome_lengths.index(max_length)
        
        # Calculate the start index of the palindrome in the original string
        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]


# Unit tests
import unittest

class ManacherTestPalindromicLength(unittest.TestCase):
    def test_palindromic_length(self):
        manacher = Manacher('ababa')
        self.assertEqual(manacher.palindromic_length(2, 1), 2)

    def test_palindromic_length_2(self):
        manacher = Manacher('ababaxse')
        self.assertEqual(manacher.palindromic_length(2, 1), 2)

    def test_palindromic_length_3(self):
        manacher = Manacher('ababax')
        self.assertEqual(manacher.palindromic_length(2, 3), 0)

    def test_palindromic_length_4(self):
        manacher = Manacher('ababax')
        self.assertEqual(manacher.palindromic_length(9, 2), 0)

    def test_palindromic_length_5(self):
        manacher = Manacher('ababax')
        self.assertEqual(manacher.palindromic_length(4, 1), 4)


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
        self.assertEqual(manacher.palindromic_length(2, 1), 2)
        self.assertEqual(manacher.palindromic_string(), 'ababa')

if __name__ == '__main__':
    unittest.main()