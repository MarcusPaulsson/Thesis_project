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
        index = -1
        for i in range(self.patLen):
            if self.pattern[i] == char:
                index = i
        return index

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first mismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first mismatch between the pattern and the text, int, otherwise -1.
        """
        for i in range(self.patLen):
            if currentPos + i >= self.textLen or self.text[currentPos + i] != self.pattern[i]:
                return currentPos + i
        return -1

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        positions = []
        n = self.textLen
        m = self.patLen
        s = 0  # shift of the pattern with respect to text
        while s <= n - m:
            j = m - 1
            
            while j >= 0 and self.pattern[j] == self.text[s + j]:
                j -= 1

            if j < 0:
                positions.append(s)
                s += (m - self.match_in_pattern(self.text[s + m]) if s + m < n else 1)
            else:
                s += max(1, j - self.match_in_pattern(self.text[s + j]))

        return positions