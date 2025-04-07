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
        textIndex = 0
        
        while textIndex <= self.textLen - self.patLen:
            mismatchIndex = self.mismatch_in_text(textIndex)
            if mismatchIndex == -1:
                positions.append(textIndex)
                textIndex += 1
            else:
                char = self.text[mismatchIndex]
                badCharIndex = self.match_in_pattern(char)
                shift = max(1, mismatchIndex - textIndex - badCharIndex) if badCharIndex != -1 else self.patLen
                textIndex += shift

        return positions