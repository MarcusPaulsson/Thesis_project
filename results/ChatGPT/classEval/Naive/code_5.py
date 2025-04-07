class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        self.play_text = text

    def interpret(self, display=False):
        if not self.play_text.strip():
            return []

        parts = []
        current_chord = ''
        current_tune = ''

        for char in self.play_text:
            if char.isalpha():
                if current_chord and current_tune:
                    parts.append({'Chord': current_chord, 'Tune': current_tune})
                current_chord = char
                current_tune = ''
            else:
                current_tune += char

        if current_chord and current_tune:
            parts.append({'Chord': current_chord, 'Tune': current_tune})

        if display:
            for part in parts:
                self.display(part['Chord'], part['Tune'])

        return parts

    def display(self, key, value):
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"