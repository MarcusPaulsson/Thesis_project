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
        if currentPos + self.patLen > self.textLen:
            return -1
        
        for i in range(self.patLen):
            if self.pattern[self.patLen - 1 - i] != self.text[currentPos + self.patLen - 1 - i]:
                return currentPos + self.patLen - 1 - i
        return -1

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        positions = []
        currentPos = 0
        
        while currentPos <= self.textLen - self.patLen:
            mismatchPos = self.mismatch_in_text(currentPos)
            if mismatchPos == -1:
                positions.append(currentPos)
                currentPos += 1
            else:
                char = self.text[mismatchPos]
                lastOccurrence = self.match_in_pattern(char)
                if lastOccurrence == -1:
                    currentPos += mismatchPos + 1
                else:
                    currentPos += mismatchPos - lastOccurrence

        return positions