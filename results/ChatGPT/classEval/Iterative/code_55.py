class Manacher:
    """
    This is a class that implements the Manacher algorithm to find the longest palindromic substring in a given string.
    """

    def __init__(self, input_string: str) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

    def palindromic_length(self, center: int, diff: int, string: str) -> int:
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
        if string[left] == string[right]:
            return 1 + self.palindromic_length(center, diff + 1, string)
        else:
            return 0

    def palindromic_string(self) -> str:
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        transformed_string = "|" + "|".join(self.input_string) + "|"
        max_len = 0
        center_index = 0
        
        for i in range(len(transformed_string)):
            length = self.palindromic_length(i, 0, transformed_string)
            if length > max_len:
                max_len = length
                center_index = i
            
        start_index = (center_index - max_len) // 2  # Adjust to original string indices
        return self.input_string[start_index:start_index + max_len]

# Unit tests