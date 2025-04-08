class AutomaticGuitarSimulator:
    def __init__(self, text: str) -> None:
        """
        Initialize the score to be played.
        :param text: str, score to be played
        """
        self.play_text = text

    def interpret(self, display: bool = False) -> list[dict]:
        """
        Interpret the music score to be played.
        :param display: bool, representing whether to print the interpreted score
        :return: list of dict, each dict contains 'Chord' and 'Tune'. 
                 If the input is empty or contains only whitespace, an empty list is returned.
        """
        if not self.play_text.strip():
            return []

        play_list = []
        for part in self.play_text.split():
            chord, tune = self._separate_chord_and_tune(part)
            play_list.append({'Chord': chord, 'Tune': tune})

            if display:
                print(self.display(chord, tune))

        return play_list

    def _separate_chord_and_tune(self, part: str) -> tuple[str, str]:
        """
        Separate the chord (letters) from the tune (numbers).
        :param part: str, the part of the score to be separated
        :return: tuple of (chord, tune)
        """
        chord = ''.join(filter(str.isalpha, part))
        tune = ''.join(filter(str.isdigit, part))
        return chord, tune

    def display(self, chord: str, tune: str) -> str:
        """
        Format and return the display string for the chord and tune.
        :param chord: str, the chord
        :param tune: str, the tune to be played
        :return: str
        """
        return f"Normal Guitar Playing -- Chord: {chord}, Play Tune: {tune}"