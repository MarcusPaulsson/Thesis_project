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
        self.word_list = set()  # Use a set for faster lookups

    def add_word(self, word):
        """
        Add the input word to the word list.
        :param word: str, input word
        """
        if isinstance(word, str):
            self.word_list.add(word)
        else:
            raise TypeError("Word must be a string.")


    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if no matching word is found.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am A student.')
        'A'
        >>> longestWord.find_longest_word('I am a student.')
        ''
        """
        if not self.word_list:
            return ''

        # Remove punctuation and split into words
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        words = regex.sub(' ', sentence).split()

        longest_word = ''
        for word in words:
            if word in self.word_list:
                if len(word) > len(longest_word):
                    longest_word = word

        return longest_word