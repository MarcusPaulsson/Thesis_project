class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        self.play_text = text

    def interpret(self, display=False):
        if not self.play_text.strip():
            return []
        
        notes = self.play_text.split()
        interpreted_score = []

        for note in notes:
            chord = ''.join(filter(str.isalpha, note))
            tune = ''.join(filter(str.isdigit, note))
            interpreted_score.append({'Chord': chord, 'Tune': tune})

            if display:
                print(self.display(chord, tune))

        return interpreted_score

    def display(self, key, value):
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"