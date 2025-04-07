class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        """
        Initialize the score to be played
        :param text: str, score to be played
        """
        self.play_text = text.strip()

    def interpret(self, display=False):
        """
        Interpret the music score to be played
        :param display: Bool, representing whether to print the interpreted score
        :return: list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively.
        If the input is empty or contains only whitespace, an empty list is returned.
        """
        if not self.play_text:
            return []

        parts = []
        current_chord = ""
        current_tune = ""

        for char in self.play_text:
            if char.isalpha():  # If the character is a letter, it's part of the chord
                if current_chord:  # If there's a chord being formed, save it
                    parts.append({'Chord': current_chord, 'Tune': current_tune})
                current_chord = char  # Start a new chord
                current_tune = ""  # Reset tune
            else:  # Otherwise, it's part of the tune
                current_tune += char

        # Append the last chord and tune if they exist
        if current_chord and current_tune:
            parts.append({'Chord': current_chord, 'Tune': current_tune})

        if display:
            for part in parts:
                print(f"Normal Guitar Playing -- Chord: {part['Chord']}, Play Tune: {part['Tune']}")

        return parts

    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key: str, chord
        :param value: str, play tune
        :return: str
        """
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"