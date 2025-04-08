import re
import string

class LongestWord:
    """
    This is a class allows to add words to a list and find the longest word in a given sentence by comparing the words with the ones in the word list.
    """

    def __init__(self):
        """
        Initialize a list of words.
        """
        self.word_list = []

    def add_word(self, word):
        """
        Appends the input word into self.word_list.
        :param word: str, input word
        """
        if isinstance(word, str):
            self.word_list.append(word)
        else:
            raise TypeError("Word must be a string.")

    def find_longest_word(self, sentence):
        """
        Removes punctuation marks and splits a sentence into a list of words.
        Finds the longest split word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest split word that is in the self.word_list. Returns '' if self.word_list is empty or no word from sentence found in word_list.
        """
        if not self.word_list:
            return ''

        # Remove punctuation marks from the sentence
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))

        # Split the sentence into a list of words
        words = sentence.split()

        # Find the longest word that is in the word_list
        longest_word = ''
        for word in words:
            if word in self.word_list:
                if len(word) > len(longest_word):
                    longest_word = word

        return longest_word