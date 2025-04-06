class AutomaticGuitarSimulator:
    def __init__(self, text: str) -> None:
        """
        Initialize the score to be played
        :param text: str, score to be played
        """
        self.play_text = text.strip() if text else ""

    def interpret(self, display: bool = False) -> list:
        """
        Interpret the music score to be played
        :param display: bool, representing whether to print the interpreted score
        :return: list of dict, with fields 'Chord' and 'Tune'. If the input is empty, returns an empty list.
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display=False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]
        """
        if not self.play_text:
            return []

        chords = self.play_text.split()
        interpreted_score = []

        for chord in chords:
            if len(chord) > 1:
                # Separate chord and tune
                interpreted_score.append({'Chord': chord[:-8], 'Tune': chord[-8:]})

        if display:
            for item in interpreted_score:
                self.display(item['Chord'], item['Tune'])

        return interpreted_score

    def display(self, key: str, value: str) -> None:
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key: str, chord
        :param value: str, play tune
        """
        print(f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}")