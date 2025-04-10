class BoyerMooreSearch:
    """
    This class implements the Boyer-Moore algorithm for string searching,
    used to find occurrences of a pattern within a given text.
    """

    def __init__(self, text: str, pattern: str):
        """
        Initializes the BoyerMooreSearch class with the given text and pattern.
        :param text: The text to be searched, str.
        :param pattern: The pattern to be searched for, str.
        """
        self.text = text
        self.pattern = pattern
        self.text_len = len(text)
        self.pattern_len = len(pattern)

    def match_in_pattern(self, char: str) -> int:
        """
        Finds the rightmost occurrence of a character in the pattern.
        :param char: The character to be searched for, str.
        :return: The index of the rightmost occurrence of the character in the pattern, int.
        """
        return self.pattern.rfind(char)

    def mismatch_in_text(self, current_pos: int) -> int:
        """
        Determines the position of the first mismatch between the pattern and the text.
        :param current_pos: The current position in the text, int.
        :return: The position of the first mismatch between the pattern and the text, int, otherwise -1.
        """
        if current_pos + self.pattern_len > self.text_len:
            return -1
        
        for i in range(self.pattern_len):
            if self.text[current_pos + i] != self.pattern[i]:
                return current_pos + i
        
        return -1

    def bad_character_heuristic(self) -> list:
        """
        Finds all occurrences of the pattern in the text using the bad character heuristic.
        :return: A list of all positions of the pattern in the text, list.
        """
        positions = []
        current_pos = 0

        while current_pos <= self.text_len - self.pattern_len:
            mismatch_pos = self.mismatch_in_text(current_pos)
            if mismatch_pos == -1:
                positions.append(current_pos)
                current_pos += 1
            else:
                bad_char = self.text[mismatch_pos]
                shift = self.match_in_pattern(bad_char)

                if shift == -1:
                    shift = self.pattern_len
                else:
                    shift = max(1, mismatch_pos - current_pos + self.pattern_len - shift)

                current_pos += shift

        return positions