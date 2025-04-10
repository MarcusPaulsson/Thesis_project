class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        """
        Initialize the score to be played
        :param text:str, score to be played
        """
        self.play_text = text

    def interpret(self, display=False):
        """
        Interpret the music score to be played
        :param display:Bool, representing whether to print the interpreted score
        :return: list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively. If the input is empty or contains only whitespace, an empty list is returned.
        """
        if not self.play_text.strip():
            return []

        parts = []
        current_chord = ''
        current_tune = ''

        for char in self.play_text:
            if char.isalpha():
                if current_chord and current_tune:
                    parts.append({'Chord': current_chord, 'Tune': current_tune})
                current_chord = char
                current_tune = ''
            else:
                current_tune += char

        if current_chord and current_tune:
            parts.append({'Chord': current_chord, 'Tune': current_tune})

        if display:
            for part in parts:
                self.display(part['Chord'], part['Tune'])

        return parts

    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        """
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"