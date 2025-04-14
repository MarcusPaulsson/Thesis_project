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

    def match_in_pattern(self, char):
        """
        Finds the rightmost occurrence of a character in the pattern.
        :param char: The character to be searched for, str.
        :return: The index of the rightmost occurrence of the character in the pattern, int. Returns -1 if the character is not found.
        """
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] == char:
                return i
        return -1

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first mismatch between the pattern and the text, starting from currentPos in the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first mismatch between the pattern and the text, int. Returns -1 if there is no mismatch.
        """
        if not self.pattern:
            return -1

        for i in range(self.patLen):
            if currentPos + i >= self.textLen:
                return currentPos + i
            if self.pattern[i] != self.text[currentPos + i]:
                return currentPos + i
        return -1

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text using the bad character heuristic.
        :return: A list of all starting positions of the pattern in the text, list.
        """
        occurrences = []
        if not self.pattern:
            return list(range(self.textLen + 1))

        i = 0
        while i <= (self.textLen - self.patLen):
            mismatch_pos = self.mismatch_in_text(i)
            if mismatch_pos == -1:
                occurrences.append(i)
                i += 1
            else:
                if mismatch_pos >= self.textLen:
                    break
                char = self.text[mismatch_pos]
                pattern_index = self.match_in_pattern(char)
                if pattern_index == -1:
                    i = mismatch_pos + 1
                else:
                    shift = mismatch_pos - pattern_index
                    if shift <= 0:
                        i += 1
                    else:
                        i = shift
        return occurrences