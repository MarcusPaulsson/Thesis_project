import re
import unittest

class LongestWord:
    """
    A class that allows adding words to a list and finding the longest word in a given sentence
    by comparing the words with those in the word list. Words are strictly case sensitive.
    """

    def __init__(self):
        """Initialize an empty list of words."""
        self.word_list = []

    def add_word(self, word):
        """
        Append the input word into self.word_list.
        :param word: str, input word
        """
        if isinstance(word, str):
            self.word_list.append(word)

    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of words. 
        Find the longest word that is in self.word_list.
        :param sentence: a sentence str
        :return str: the longest word found in self.word_list or '' if self.word_list is empty.
        """
        if not self.word_list:
            return ''
        
        # Remove punctuation and split the sentence into words
        words = re.findall(r'\b\w+\b', sentence)
        longest = ''
        
        for word in words:
            if word in self.word_list and len(word) > len(longest):
                longest = word
        
        return longest


class LongestWordTestAddWord(unittest.TestCase):
    def test_add_word_1(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        self.assertEqual(['hello'], longestWord.word_list)

    def test_add_word_2(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        longestWord.add_word("world")
        self.assertEqual(['hello', 'world'], longestWord.word_list)

    def test_add_word_3(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        longestWord.add_word("world")
        longestWord.add_word("!")
        self.assertEqual(['hello', 'world', '!'], longestWord.word_list)

    def test_add_word_4(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        longestWord.add_word("world")
        longestWord.add_word("!")
        longestWord.add_word("!")
        self.assertEqual(['hello', 'world', '!', '!'], longestWord.word_list)

    def test_add_word_5(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        longestWord.add_word("world")
        longestWord.add_word("!")
        longestWord.add_word("!")
        longestWord.add_word("!")
        self.assertEqual(['hello', 'world', '!', '!', '!'], longestWord.word_list)


class LongestWordTestFindLongestWord(unittest.TestCase):
    def test_find_longest_word_1(self):
        longestWord = LongestWord()
        longestWord.add_word("a")
        sentence = 'I am a student.'
        self.assertEqual('a', longestWord.find_longest_word(sentence))

    def test_find_longest_word_2(self):
        longestWord = LongestWord()
        sentence = 'I am a student.'
        self.assertEqual('', longestWord.find_longest_word(sentence))

    def test_find_longest_word_3(self):
        longestWord = LongestWord()
        longestWord.add_word("student")
        sentence = 'I am a student.'
        self.assertEqual('student', longestWord.find_longest_word(sentence))

    def test_find_longest_word_4(self):
        longestWord = LongestWord()
        longestWord.add_word("apple")
        sentence = 'Apple is red.'
        self.assertEqual('apple', longestWord.find_longest_word(sentence))

    def test_find_longest_word_5(self):
        longestWord = LongestWord()
        longestWord.add_word("apple")
        longestWord.add_word("red")
        sentence = 'Apple is red.'
        self.assertEqual('apple', longestWord.find_longest_word(sentence))

if __name__ == "__main__":
    unittest.main()