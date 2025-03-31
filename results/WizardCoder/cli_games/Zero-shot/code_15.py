class BoyerMooreSearch:
    """This class implements the Boyer-Moore algorithm for string searching."""

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
        >>> BoyerMooreSearch("ABAABA", "AB").match_in_pattern("A")
        0
        """
        return self.pattern[::-1].index(char)

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.

        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int, otherwise -1.
        >>> BoyerMooreSearch("ABAABA", "ABC").mismatch_in_text(0)
        2
        """
        i = 0
        while (currentPos + self.patLen - 1) < self.textLen:
            if self.text[currentPos : currentPos+self.patLen] == self.pattern:
                return currentPos
            else:
                currentPos += 1
        return -1

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.

        :return: A list of all positions of the pattern in the text, list.
        >>> BoyerMooreSearch("ABAABA", "AB").bad_character_heuristic()
        [0, 3]
        """
        matches = []
        i = 0
        while (i + self.patLen) <= self.textLen:
            if self.match(self.pattern, i):
                matches.append(i)
            i += 1
        return matches

    def match(self, currentPos):
        """
        Checks if the pattern occurs at the given position in the text.

        :param currentPos: The current position in the text, int.
        :return: True if the pattern occurs at the given position, otherwise False.
        >>> BoyerMooreSearch("ABAABA", "AB").match(0)
        True
        """
        for i in range(self.patLen):
            if self.text[currentPos+i] != self.pattern[i]:
                return False
        return True