import re
import string

class LongestWord:
    """
    This is a class allows to add words to a list and find the longest word in a given sentence by comparing the words with the ones in the word list.
    """

    def __init__(self):
        """
        Initialize a list of word.
        """
        self.word_list = []

    def add_word(self, word):
        """
        Append the input word into self.word_list.

        :param word: str, input word
        """
        self.word_list.append(word)

    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of words.
        Find the longest split word that is in the self.word_list.
        Words are strictly case sensitive.

        :param sentence: a sentence str
        :return str: longest split word that is in the self.word_list.
                     Return '' if self.word_list is empty or no word in sentence is in word_list.
        """
        if not self.word_list:
            return ''

        # Remove punctuation marks from the sentence
        translator = str.maketrans('', '', string.punctuation)
        sentence = sentence.translate(translator)

        # Split the sentence into words
        words = sentence.split()

        longest_word = ''
        for word in words:
            if word in self.word_list:
                if len(word) > len(longest_word):
                    longest_word = word

        return longest_word