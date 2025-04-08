class AutomaticGuitarSimulator:
    def __init__(self, text):
        """
        Initializes the AutomaticGuitarSimulator with the given text.

        Args:
            text (str): The text representing the guitar score to be played.
        """
        self.play_text = text

    def interpret(self, display=False):
        """
        Interprets the guitar score and returns a list of dictionaries,
        where each dictionary contains the 'Chord' and 'Tune'.

        Args:
            display (bool, optional): If True, prints the interpreted score. Defaults to False.

        Returns:
            list: A list of dictionaries, where each dictionary represents a chord and tune.
                   Returns an empty list if the input text is empty or contains only whitespace.
        """
        if not self.play_text or self.play_text.isspace():
            return []

        score_list = self.play_text.split()
        result = []
        for score in score_list:
            chord = ''.join(char for char in score if char.isalpha())
            tune = ''.join(char for char in score if char.isdigit())
            result.append({'Chord': chord, 'Tune': tune})

        if display:
            for item in result:
                print(self.display(item['Chord'], item['Tune']))

        return result

    def display(self, key, value):
        """
        Formats and returns a string representing the chord and tune.

        Args:
            key (str): The chord.
            value (str): The tune.

        Returns:
            str: A formatted string representing the chord and tune.
        """
        return "Normal Guitar Playing -- Chord: %s, Play Tune: %s" % (key, value)