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
        # Transform the string to avoid even/odd length issues
        transformed = '|' + '|'.join(self.input_string) + '|'
        n = len(transformed)
        max_length = 0
        max_center = 0
        
        for center in range(n):
            length = self.palindromic_length(center, 0, transformed)
            if length > max_length:
                max_length = length
                max_center = center
        
        start = (max_center - max_length) // 2
        return self.input_string[start:start + max_length]
