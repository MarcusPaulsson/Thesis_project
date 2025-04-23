class AutomaticGuitarSimulator:
    def __init__(self, text: str) -> None:
        """
        Initialize the score to be played.
        
        :param text: str, score to be played
        """
        self.play_text = text.strip()

    def interpret(self, display: bool = False) -> list:
        """
        Interpret the music score to be played.
        
        :param display: bool, representing whether to print the interpreted score
        :return: list of dict, each dict includes 'Chord' and 'Tune'.
        If the input is empty or contains only whitespace, an empty list is returned.
        """
        if not self.play_text:
            return []

        chords = self.play_text.split()
        play_list = []

        for chord in chords:
            if chord:  # Ensure the chord is not empty
                chord_name = ''.join(filter(str.isalpha, chord))
                tune = ''.join(filter(str.isdigit, chord))
                play_list.append({'Chord': chord_name, 'Tune': tune})

                if display:
                    print(self.display(chord_name, tune))

        return play_list

    def display(self, chord: str, tune: str) -> str:
        """
        Format and return the chord and play tune.
        
        :param chord: str, chord name
        :param tune: str, play tune
        :return: str formatted message
        """
        return f"Normal Guitar Playing -- Chord: {chord}, Play Tune: {tune}"