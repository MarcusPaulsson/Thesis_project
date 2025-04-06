import re

class LongestWord:
    """
    A class that allows adding words to a list and finding the longest word in a given sentence 
    by comparing the words with those in the word list.
    """

    def __init__(self):
        """Initialize an empty list of words."""
        self.word_list = set()  # Use a set for faster lookups

    def add_word(self, word: str):
        """
        Append the input word into self.word_list.
        
        :param word: str, input word
        """
        if isinstance(word, str) and word:  # Ensure the word is a non-empty string
            self.word_list.add(word)

    def find_longest_word(self, sentence: str) -> str:
        """
        Remove punctuation marks and split a sentence into a list of words. 
        Find the longest word that is in the self.word_list.
        Words are strictly case sensitive.

        :param sentence: str, a sentence
        :return: str, the longest word found in self.word_list or '' if self.word_list is empty.
        """
        if not self.word_list:
            return ''
        
        # Remove punctuation and split the sentence into words
        words = re.findall(r'\b\w+\b', sentence)

        # Find the longest word that is in the word_list
        longest = max((word for word in words if word in self.word_list), key=len, default='')

        return longest