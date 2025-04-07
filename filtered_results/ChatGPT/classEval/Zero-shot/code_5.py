class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        self.play_text = text.strip()

    def interpret(self, display=False):
        if not self.play_text:
            return []
        
        play_list = []
        elements = self.play_text.split()
        for element in elements:
            chord = ''.join(filter(str.isalpha, element))
            tune = ''.join(filter(str.isdigit, element))
            play_list.append({'Chord': chord, 'Tune': tune})
        
        if display:
            for item in play_list:
                self.display(item['Chord'], item['Tune'])
        
        return play_list

    def display(self, key, value):
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"