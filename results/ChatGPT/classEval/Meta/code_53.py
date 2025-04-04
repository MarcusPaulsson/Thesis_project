import re

class LongestWord:
    """
    This is a class that allows adding words to a list and finding the longest word in a given sentence 
    by comparing the words with the ones in the word list.
    """

    def __init__(self):
        """
        Initialize a list of words.
        """
        self.word_list = []

    def add_word(self, word):
        """
        Append the input word into self.word_list
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
                     Return '' if self.word_list is empty.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.')
        'a'
        """
        if not self.word_list:
            return ''

        # Remove punctuation and split the sentence into words
        words = re.findall(r'\b\w+\b', sentence)
        
        # Find the longest word in the word_list that is in the sentence
        longest = ''
        for word in words:
            if word in self.word_list and len(word) > len(longest):
                longest = word
                
        return longest