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
        self.text, self.pattern = text, pattern
        self.textLen, self.patLen = len(text), len(pattern)

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
        for i in range(self.patLen):
            if currentPos + i >= self.textLen or self.pattern[i] != self.text[currentPos + i]:
                return i
        return -1

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        occurrences = []
        pos = 0

        while pos <= self.textLen - self.patLen:
            mismatch_index = self.mismatch_in_text(pos)
            if mismatch_index == -1:
                occurrences.append(pos)
                pos += self.patLen  # Shift the pattern completely to the right
            else:
                char = self.text[pos + mismatch_index]
                bad_char_index = self.match_in_pattern(char)
                if bad_char_index == -1:
                    pos += mismatch_index + 1  # Shift pattern past the mismatched character
                else:
                    pos += max(1, mismatch_index - bad_char_index)  # Shift the pattern to align with the bad character
        return occurrences