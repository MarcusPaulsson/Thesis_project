import re
import unittest

class AutomaticGuitarSimulator:
    def __init__(self, text: str) -> None:
        """
        Initialize the score to be played
        :param text: str, score to be played
        """
        self.play_text = text

    def interpret(self, display=False) -> list:
        """
        Interpret the music score to be played
        :param display: bool, representing whether to print the interpreted score
        :return: list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively.
                If the input is empty or contains only whitespace, an empty list is returned.
        """
        if not self.play_text.strip():
            return []

        # Split the input text into chords and tunes
        play_list = []
        matches = re.findall(r'([A-Za-z]+)(\d+)', self.play_text)
        for chord, tune in matches:
            play_list.append({'Chord': chord, 'Tune': tune})

        if display:
            for item in play_list:
                print(self.display(item['Chord'], item['Tune']))

        return play_list

    def display(self, key: str, value: str) -> str:
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key: str, chord
        :param value: str, play tune
        :return: str
        """
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"


class AutomaticGuitarSimulatorTestInterpret(unittest.TestCase):
    def test_interpret_1(self):
        context = AutomaticGuitarSimulator("C53231323")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'C', 'Tune': '53231323'}])

    def test_interpret_2(self):
        context = AutomaticGuitarSimulator("F43231323")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'F', 'Tune': '43231323'}])

    def test_interpret_3(self):
        context = AutomaticGuitarSimulator("Em43231323")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'Em', 'Tune': '43231323'}])

    def test_interpret_4(self):
        context = AutomaticGuitarSimulator("G63231323")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'G', 'Tune': '63231323'}])

    def test_interpret_5(self):
        context = AutomaticGuitarSimulator("F43231323 G63231323")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}])

    def test_interpret_6(self):
        context = AutomaticGuitarSimulator(" ")
        play_list = context.interpret()
        self.assertEqual(play_list, [])

    def test_interpret_7(self):
        context = AutomaticGuitarSimulator("ABC43231323 DEF63231323")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'ABC', 'Tune': '43231323'}, {'Chord': 'DEF', 'Tune': '63231323'}])

    def test_interpret_8(self):
        context = AutomaticGuitarSimulator("C53231323")
        play_list = context.interpret(display=True)
        self.assertEqual(play_list, [{'Chord': 'C', 'Tune': '53231323'}])

    def test_interpret_9(self):
        context = AutomaticGuitarSimulator("")
        play_list = context.interpret()
        self.assertEqual(play_list, [])


class AutomaticGuitarSimulatorTestDisplay(unittest.TestCase):
    def test_display_1(self):
        context = AutomaticGuitarSimulator("C53231323 Em43231323")
        play_list = context.interpret()
        result = context.display(play_list[0]['Chord'], play_list[0]['Tune'])
        self.assertEqual(result, "Normal Guitar Playing -- Chord: C, Play Tune: 53231323")

    def test_display_2(self):
        context = AutomaticGuitarSimulator("C53231323 Em43231323")
        play_list = context.interpret()
        result = context.display(play_list[1]['Chord'], play_list[1]['Tune'])
        self.assertEqual(result, "Normal Guitar Playing -- Chord: Em, Play Tune: 43231323")

    def test_display_3(self):
        context = AutomaticGuitarSimulator("F43231323 G63231323")
        play_list = context.interpret()
        result = context.display(play_list[0]['Chord'], play_list[0]['Tune'])
        self.assertEqual(result, "Normal Guitar Playing -- Chord: F, Play Tune: 43231323")

    def test_display_4(self):
        context = AutomaticGuitarSimulator("F43231323 G63231323")
        play_list = context.interpret()
        result = context.display(play_list[1]['Chord'], play_list[1]['Tune'])
        self.assertEqual(result, "Normal Guitar Playing -- Chord: G, Play Tune: 63231323")

    def test_display_5(self):
        context = AutomaticGuitarSimulator("")
        result = context.display('', '')
        self.assertEqual(result, "Normal Guitar Playing -- Chord: , Play Tune: ")


class AutomaticGuitarSimulatorTest(unittest.TestCase):
    def test_AutomaticGuitarSimulator(self):
        context = AutomaticGuitarSimulator("C53231323")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'C', 'Tune': '53231323'}])

        context = AutomaticGuitarSimulator("C53231323 Em43231323")
        play_list = context.interpret()
        result = context.display(play_list[0]['Chord'], play_list[0]['Tune'])
        self.assertEqual(result, "Normal Guitar Playing -- Chord: C, Play Tune: 53231323")

if __name__ == '__main__':
    unittest.main()