class AutomaticGuitarSimulator:
    def __init__(self, text):
        """
        Initializes the AutomaticGuitarSimulator with the given text.

        Args:
            text (str): The guitar score to be played.
        """
        self.play_text = text

    def interpret(self, display=False):
        """
        Interprets the guitar score and returns a list of dictionaries,
        where each dictionary contains the chord and tune.

        Args:
            display (bool, optional): A flag indicating whether to print the interpreted score. Defaults to False.

        Returns:
            list: A list of dictionaries, where each dictionary has 'Chord' and 'Tune' keys.
                 Returns an empty list if the input is empty or contains only whitespace.
        """
        if not self.play_text or self.play_text.isspace():
            return []

        score_list = self.play_text.split()
        play_list = []

        for score in score_list:
            chord = ''.join(char for char in score if char.isalpha())
            tune = ''.join(char for char in score if char.isdigit())
            play_list.append({'Chord': chord, 'Tune': tune})

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