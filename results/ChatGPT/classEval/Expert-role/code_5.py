class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        self.play_text = text

    def interpret(self, display=False):
        if not self.play_text.strip():
            return []
        
        result = []
        parts = self.play_text.split()
        
        for part in parts:
            chord = ''.join(filter(str.isalpha, part))
            tune = ''.join(filter(str.isdigit, part))
            result.append({'Chord': chord, 'Tune': tune})
        
        if display:
            for item in result:
                print(self.display(item['Chord'], item['Tune']))
        
        return result

    def display(self, key, value):
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"