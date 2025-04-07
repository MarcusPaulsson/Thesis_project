import re

class AutomaticGuitarSimulator:
    """
    A class to simulate an automatic guitar player.
    """

    def __init__(self, text: str) -> None:
        """
        Initializes the AutomaticGuitarSimulator with the music score.

        Args:
            text (str): The music score to be played, e.g., "C53231323 Em43231323".
        """
        self.play_text = text

    def interpret(self, display: bool = False) -> list[dict[str, str]]:
        """
        Interprets the music score into a list of chords and tunes.

        Args:
            display (bool, optional): Whether to print the interpreted score. Defaults to False.

        Returns:
            list[dict[str, str]]: A list of dictionaries, where each dictionary contains a 'Chord' (str) and a 'Tune' (str).
                                  Returns an empty list if the input is empty or contains only whitespace.

        Examples:
            >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
            >>> play_list = context.interpret(display = False)
            >>> play_list == [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]
            True
        """
        if not self.play_text or self.play_text.isspace():
            return []

        play_list = []
        segments = self.play_text.split()

        for segment in segments:
            match = re.match(r"([A-Za-z]+)([0-9]+)", segment)  # Use regex for robust parsing
            if match:
                chord = match.group(1)
                tune = match.group(2)
                play_list.append({'Chord': chord, 'Tune': tune})

        if display:
            for item in play_list:
                print(self.display(item['Chord'], item['Tune']))  # Print instead of return

        return play_list

    def display(self, key: str, value: str) -> str:
        """
        Formats the chord and tune into a string for display.

        Args:
            key (str): The chord.
            value (str): The tune.

        Returns:
            str: A formatted string representing the chord and tune.

        Examples:
            >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
            >>> context.display("C", "53231323")
            'Normal Guitar Playing -- Chord: C, Play Tune: 53231323'
        """
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"