class BoyerMooreSearch:
    """
    This class implements the Boyer-Moore algorithm for string searching, which is used to find occurrences of a pattern within a given text.
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
        self.badChar = self.bad_character_heuristic()

    def match_in_pattern(self, char):
        """
        Finds the rightmost occurrence of a character in the pattern.
        :param char: The character to be searched for, str.
        :return: The index of the rightmost occurrence of the character in the pattern, int.
        """
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] == char:
                return i
        return -1

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first mismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first mismatch between the pattern and the text, int, otherwise -1.
        """
        for i in range(self.patLen - 1, -1, -1):
            if currentPos + i >= self.textLen or self.text[currentPos + i] != self.pattern[i]:
                return i
        return -1

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text using the bad character heuristic.
        :return: A list of all positions of the pattern in the text, list.
        """
        positions = []
        skip = 0
        
        while skip <= self.textLen - self.patLen:
            mismatch_index = self.mismatch_in_text(skip)
            if mismatch_index == -1:
                positions.append(skip)
                skip += self.patLen - self.match_in_pattern(self.text[skip + self.patLen - 1]) if skip + self.patLen < self.textLen else 1
            else:
                char_index = self.match_in_pattern(self.text[skip + mismatch_index])
                skip += max(1, mismatch_index - char_index)
        
        return positions