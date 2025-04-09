import re


class AutomaticGuitarSimulator:
    def __init__(self, text: str) -> None:
        """
        Initialize the score to be played
        :param text: str, score to be played
        """
        self.play_text = text

    def interpret(self, display=False) -> list:
        """
        Interpret the music score to be played
        :param display: bool, representing whether to print the interpreted score
        :return: list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively.
                If the input is empty or contains only whitespace, an empty list is returned.
        """
        if not self.play_text.strip():
            return []

        # Split the input text into chords and tunes
        play_list = []
        matches = re.findall(r'([A-Za-z]+)(\d+)', self.play_text)
        for chord, tune in matches:
            play_list.append({'Chord': chord, 'Tune': tune})

        if display:
            for item in play_list:
                print(self.display(item['Chord'], item['Tune']))

        return play_list

    def display(self, key: str, value: str) -> str:
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key: str, chord
        :param value: str, play tune
        :return: str
        """
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"

