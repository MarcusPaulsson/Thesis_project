import re

class LongestWord:
    """
    This class allows adding words to a list and finding the longest word in a given sentence 
    by comparing the words with those in the word list.
    """

    def __init__(self):
        """
        Initialize a list of words.
        """
        self.word_list = []

    def add_word(self, word: str):
        """
        Append the input word into self.word_list.
        :param word: str, input word
        """
        if isinstance(word, str):
            self.word_list.append(word)

    def find_longest_word(self, sentence: str) -> str:
        """
        Remove punctuation marks and split a sentence into a list of words. 
        Find the longest split word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return: str, longest split word that is in the self.word_list. 
                 Returns '' if self.word_list is empty.
        """
        if not self.word_list:
            return ''

        # Remove punctuation and split the sentence into words
        words = re.findall(r'\b\w+\b', sentence)
        longest_word = max((word for word in words if word in self.word_list), 
                           key=len, default='')

        return longest_word