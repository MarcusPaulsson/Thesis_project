class AutomaticGuitarSimulator:
    def __init__(self, text: str) -> None:
        """
        Initialize the score to be played.
        :param text: str, score to be played.
        """
        self.play_text = text.strip()

    def interpret(self, display: bool = False) -> list:
        """
        Interpret the music score to be played.
        :param display: bool, representing whether to print the interpreted score.
        :return: list of dict, each dict includes 'Chord' (str) and 'Tune' (str).
        If the input is empty or contains only whitespace, an empty list is returned.

        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display=False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, 
        {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]
        """
        if not self.play_text:
            return []

        parts = self.play_text.split()
        result = []

        for part in parts:
            chord = ''.join(filter(str.isalpha, part))
            tune = ''.join(filter(str.isdigit, part))
            result.append({'Chord': chord, 'Tune': tune})

            if display:
                print(self.display(chord, tune))

        return result

    def display(self, chord: str, tune: str) -> str:
        """
        Print out chord and play tune with the following format:
        Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param chord: str, chord.
        :param tune: str, play tune.
        :return: str formatted message.

        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323")
        >>> context.display("C", "53231323")
        'Normal Guitar Playing -- Chord: C, Play Tune: 53231323'
        """
        return f"Normal Guitar Playing -- Chord: {chord}, Play Tune: {tune}"