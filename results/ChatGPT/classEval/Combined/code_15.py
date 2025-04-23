class BoyerMooreSearch:
    """
    This class implements the Boyer-Moore algorithm for string searching,
    which is used to find occurrences of a pattern within a given text.
    """

    def __init__(self, text: str, pattern: str):
        """
        Initializes the BoyerMooreSearch class with the given text and pattern.
        :param text: The text to be searched.
        :param pattern: The pattern to be searched for.
        """
        self.text = text
        self.pattern = pattern
        self.text_len = len(text)
        self.pattern_len = len(pattern)

    def match_in_pattern(self, char: str) -> int:
        """
        Finds the rightmost occurrence of a character in the pattern.
        :param char: The character to be searched for.
        :return: The index of the rightmost occurrence of the character in the pattern, or -1 if not found.
        """
        return self.pattern.rfind(char)

    def mismatch_in_text(self, current_pos: int) -> int:
        """
        Determines the position of the first mismatch between the pattern and the text.
        :param current_pos: The current position in the text.
        :return: The position of the first mismatch between the pattern and the text, or -1 if no mismatch.
        """
        if current_pos + self.pattern_len > self.text_len:
            return -1
        
        for i in range(self.pattern_len):
            if self.pattern[self.pattern_len - 1 - i] != self.text[current_pos + self.pattern_len - 1 - i]:
                return current_pos + self.pattern_len - 1 - i
        return -1

    def bad_character_heuristic(self) -> list:
        """
        Finds all occurrences of the pattern in the text using the bad character heuristic.
        :return: A list of all positions of the pattern in the text.
        """
        positions = []
        text_index = 0

        while text_index <= self.text_len - self.pattern_len:
            mismatch_index = self.mismatch_in_text(text_index)

            if mismatch_index == -1:
                positions.append(text_index)
                text_index += 1
            else:
                bad_char_index = self.match_in_pattern(self.text[mismatch_index])
                shift = max(1, mismatch_index - text_index + 1 - bad_char_index)
                text_index += shift

        return positions