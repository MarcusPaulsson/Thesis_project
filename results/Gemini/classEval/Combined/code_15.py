class BoyerMooreSearch:
    """
    Implements the Boyer-Moore algorithm for string searching to find occurrences of a pattern within a given text.
    """

    def __init__(self, text, pattern):
        """
        Initializes the BoyerMooreSearch class with the text and pattern to search for.

        :param text: The text to be searched (string).
        :param pattern: The pattern to be searched for (string).
        """
        self.text = text
        self.pattern = pattern
        self.textLen = len(text)
        self.patLen = len(pattern)

    def match_in_pattern(self, char):
        """
        Finds the rightmost occurrence of a character within the pattern.

        :param char: The character to search for (string).
        :return: The index of the rightmost occurrence of the character in the pattern, or -1 if not found (integer).
        """
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] == char:
                return i
        return -1

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first mismatch between the pattern and the text, starting from a given position.

        :param currentPos: The starting position in the text (integer).
        :return: The index of the first mismatch, or -1 if there is a match (integer).
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
        Finds all occurrences of the pattern within the text using the bad character heuristic.

        :return: A list of starting positions where the pattern is found in the text (list of integers).
        """
        occurrences = []
        if not self.pattern:
            return list(range(self.textLen + 1))

        i = 0
        while i <= self.textLen - self.patLen:
            mismatch_pos = self.mismatch_in_text(i)
            if mismatch_pos == -1:
                occurrences.append(i)
                i += 1
            else:
                if mismatch_pos >= self.textLen:
                    break

                bad_char = self.text[mismatch_pos]
                pattern_index = self.match_in_pattern(bad_char)

                shift = mismatch_pos - i - pattern_index if pattern_index != -1 else 1
                if shift <= 0:
                    shift = 1
                i += shift

        return occurrences