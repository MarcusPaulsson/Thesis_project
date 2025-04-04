class BoyerMooreSearch:
    """
    This is a class that implements the Boyer-Moore algorithm for string searching, which is used to find occurrences of a pattern within a given text.
    """

    def __init__(self, text, pattern):
        """
        Initializes the BoyerMooreSearch class with the given text and pattern.
        :param text: The text to be searched, str.
        :param pattern: The pattern to be searched for, str.
        """
        self.text = text
        self.pattern = pattern
        self.textLen = len(text)
        self.patLen = len(pattern)
        self.bad_char_shift = self.bad_character_heuristic()

    def match_in_pattern(self, char):
        """
        Finds the rightmost occurrence of a character in the pattern.
        :param char: The character to be searched for, str.
        :return: The index of the rightmost occurrence of the character in the pattern, int.
        """
        return self.pattern.rfind(char)

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first mismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first mismatch between the pattern and the text, int, otherwise -1.
        """
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] != self.text[currentPos + i]:
                return i
        return -1

    def bad_character_heuristic(self):
        """
        Creates a bad character shift table.
        :return: A dictionary containing the shift values for each character in the pattern.
        """
        bad_char_shift = {}
        for i in range(self.patLen):
            bad_char_shift[self.pattern[i]] = i
        return bad_char_shift

    def search(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        positions = []
        s = 0  # s is the shift of the pattern with respect to text
        while s <= self.textLen - self.patLen:
            j = self.mismatch_in_text(s)
            if j == -1:  # A match is found
                positions.append(s)
                s += (self.patLen - self.bad_char_shift.get(self.text[s + self.patLen], -1)) if s + self.patLen < self.textLen else 1
            else:
                s += max(1, j - self.bad_char_shift.get(self.text[s + j], -1))
        return positions