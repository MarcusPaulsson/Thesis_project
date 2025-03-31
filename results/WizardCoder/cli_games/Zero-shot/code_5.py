class AutomaticGuitarSimulator:
    def __init__(self, text):
        self.play_text = text

    @staticmethod
    def interpret(text):
        if not text or text.isspace():
            return []

        chord_list = []
        for line in text.split('\n'):
            chord, tune = line.strip().split()
            chord_dict = {'Chord': chord, 'Tune': tune}
            chord_list.append(chord_dict)
        return chord_list

    def display(self, key, value):
        print("Normal Guitar Playing -- Chord: {}, Play Tune: {}".format(key, value))