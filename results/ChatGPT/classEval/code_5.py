class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        self.play_text = text

    def interpret(self, display=False):
        if not self.play_text.strip():
            return []
        
        chords = self.play_text.split()
        result = []
        
        for chord in chords:
            chord_name = ''.join(filter(str.isalpha, chord))
            tune = ''.join(filter(str.isdigit, chord))
            result.append({'Chord': chord_name, 'Tune': tune})
        
        if display:
            for item in result:
                self.display(item['Chord'], item['Tune'])
        
        return result

    def display(self, key, value):
        print(f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}")