class AutomaticGuitarSimulator:
    def __init__(self, text: str) -> None:
        """
        Initialize the score to be played
        :param text: str, score to be played
        """
        self.play_text = text.strip()

    def interpret(self, display=False):
        """
        Interpret the music score to be played
        :param display: bool, representing whether to print the interpreted score
        :return: list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively.
        If the input is empty or contains only whitespace, an empty list is returned.
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display=False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]
        """
        if not self.play_text:
            return []

        chords = self.play_text.split()
        interpreted_score = []

        for chord in chords:
            if len(chord) < 2:
                continue
            interpreted_score.append({
                'Chord': chord[:-8],  # Assuming the last 8 characters are the tune
                'Tune': chord[-8:]
            })
            if display:
                self.display(interpreted_score[-1]['Chord'], interpreted_score[-1]['Tune'])

        return interpreted_score

    def display(self, key: str, value: str):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key: str, chord
        :param value: str, play tune
        :return: None
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323
        """
        print(f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}")