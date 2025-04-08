import re

class SplitSentence:
    """
    The class allows to split sentences, count words in a sentence, and process a text to find the maximum word count.
    """

    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and have a space after that. 
        'Mr.' also ends with . but is not treated as a sentence.
        
        :param sentences_string: str, string to split
        :return: list, list of split sentences
        """
        sentences = re.split(r'(?<!Mr)(?<![A-Z]\.)[.?\s]+', sentences_string.strip())
        return [s.strip() for s in sentences if s.strip()]

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Words are separated by spaces and punctuation marks/numbers are not counted.
        
        :param sentence: str, sentence to be counted
        :return: int, number of words in the sentence
        """
        words = re.findall(r'\b[a-zA-Z]+\b', sentence)
        return len(words)

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence.
        
        :param sentences_string: str, undivided long sentence
        :return: int, number of words in the longest sentence
        """
        sentences = self.split_sentences(sentences_string)
        return max((self.count_words(sentence) for sentence in sentences), default=0)

# Unit tests
import unittest

class SplitSentenceTestSplitSentences(unittest.TestCase):
    def test_split_sentences(self):
        ss = SplitSentence()
        cases = [
            ("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?", ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']),
            ("Who is Mr. Smith? He is a teacher.", ['Who is Mr. Smith?', 'He is a teacher.']),
            ("Who is A.B.C.? He is a teacher.", ['Who is A.B.C.?', 'He is a teacher.']),
            ("aaa aaaa. bb bbbb bbb? cccc cccc.", ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.']),
            ("aaa aaaa. bb bbbb bbb?", ['aaa aaaa.', 'bb bbbb bbb?'])
        ]
        for input_text, expected in cases:
            self.assertEqual(ss.split_sentences(input_text), expected)

class SplitSentenceTestCountWords(unittest.TestCase):
    def test_count_words(self):
        ss = SplitSentence()
        cases = [
            ("abc def", 2),
            ("abc def 1", 2),
            ("abc 1", 1),
            ("abc def bbb1", 3),
            ("abc def 111", 2)
        ]
        for input_text, expected in cases:
            self.assertEqual(ss.count_words(input_text), expected)

class SplitSentenceTestProcessTextFile(unittest.TestCase):
    def test_process_text_file(self):
        ss = SplitSentence()
        cases = [
            ("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?", 4),
            ("Mr. Smith is a teacher. Yes.", 5),
            ("Mr. Smith is a teacher. Yes 1 2 3 4 5 6.", 5),
            ("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc.", 4),
            ("aaa aaaa. bb bbbb bbb?", 3)
        ]
        for input_text, expected in cases:
            self.assertEqual(ss.process_text_file(input_text), expected)

class SplitSentenceTest(unittest.TestCase):
    def test_complete_functionality(self):
        ss = SplitSentence()
        self.assertEqual(ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?"),
                         ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?'])
        self.assertEqual(ss.count_words("abc def"), 2)
        self.assertEqual(ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?"), 4)

if __name__ == "__main__":
    unittest.main()