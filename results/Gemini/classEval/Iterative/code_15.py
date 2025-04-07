class BoyerMooreSearch:
    """
    Implements the Boyer-Moore algorithm for string searching.
    Finds occurrences of a pattern within a given text.
    """

    def __init__(self, text, pattern):
        """
        Initializes the BoyerMooreSearch class with the given text and pattern.

        Args:
            text (str): The text to be searched.
            pattern (str): The pattern to be searched for.
        """
        self.text = text
        self.pattern = pattern
        self.text_len = len(text)
        self.pattern_len = len(pattern)
        self.bad_char_table = self._build_bad_char_table()

    def _build_bad_char_table(self):
        """
        Builds the bad character table for the pattern.

        Returns:
            dict: A dictionary where keys are characters and values are the rightmost
                  index of that character in the pattern.
        """
        table = {}
        for i in range(self.pattern_len):
            table[self.pattern[i]] = i
        return table

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text using the bad character heuristic.

        Returns:
            list: A list of all starting positions where the pattern occurs in the text.
        """
        occurrences = []
        i = 0
        while i <= self.text_len - self.pattern_len:
            j = self.pattern_len - 1
            while j >= 0 and self.pattern[j] == self.text[i + j]:
                j -= 1

            if j < 0:
                occurrences.append(i)
                i += (1 if self.pattern_len == 0 else self.pattern_len - self.bad_char_heuristic_shift(self.text[i+self.pattern_len] if i + self.pattern_len < self.text_len else self.pattern[-1])) if self.pattern_len > 0 else 1

            else:
                bad_char = self.text[i + j]
                shift = max(1, j - self.bad_char_heuristic_shift(bad_char))
                i += shift

        return occurrences

    def bad_char_heuristic_shift(self, char):
        """
        Calculates the shift value based on the bad character heuristic.

        Args:
            char (str): The character from the text that caused the mismatch.

        Returns:
            int: The shift value.
        """
        if char in self.bad_char_table:
            return self.bad_char_table[char]
        else:
            return -1