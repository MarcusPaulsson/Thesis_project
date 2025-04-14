class BoyerMooreSearch:
    """
    his is a class that implements the Boyer-Moore algorithm for string searching, which is used to find occurrences of a pattern within a given text.
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
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.match_in_pattern("A")
        0

        """
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] == char:
                return i
        return -1

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int,otherwise -1.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2

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
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.bad_character_heuristic()
        [0, 3]

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
                char = self.text[mismatch_pos]
                rightmost_occurrence = self.match_in_pattern(char)
                shift = mismatch_pos - i - rightmost_occurrence
                if rightmost_occurrence == -1:
                    i = mismatch_pos + 1
                else:
                    shift = mismatch_pos - i - rightmost_occurrence
                    if shift <= 0:
                        i += 1
                    else:
                        i += shift
        return occurrences