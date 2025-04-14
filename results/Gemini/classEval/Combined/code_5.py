class AutomaticGuitarSimulator:
    def __init__(self, text):
        """
        Initializes the AutomaticGuitarSimulator with the given text.

        Args:
            text (str): The text representing the guitar score.
        """
        self.play_text = text

    def interpret(self, display=False):
        """
        Interprets the guitar score and returns a list of dictionaries,
        where each dictionary contains the chord and tune.

        Args:
            display (bool, optional): Whether to display the interpreted score. Defaults to False.

        Returns:
            list: A list of dictionaries, where each dictionary has 'Chord' and 'Tune' keys.
                   Returns an empty list if the input text is empty or contains only whitespace.
        """
        if not self.play_text or self.play_text.isspace():
            return []

        play_list = []
        parts = self.play_text.split()

        for part in parts:
            chord = ''.join(filter(str.isalpha, part))
            tune = ''.join(filter(str.isdigit, part))
            play_list.append({'Chord': chord, 'Tune': tune})

        if display:
            for item in play_list:
                print(self.display(item['Chord'], item['Tune']))

        return play_list

    def display(self, key, value):
        """
        Formats and returns a string representing the chord and tune.

        Args:
            key (str): The chord.
            value (str): The tune.

        Returns:
            str: A formatted string representing the chord and tune.
        """
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"