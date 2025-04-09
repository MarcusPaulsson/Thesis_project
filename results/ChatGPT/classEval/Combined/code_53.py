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

    def add_word(self, word: str) -> None:
        """
        Append the input word into self.word_list.
        :param word: str, input word
        """
        self.word_list.append(word)

    def find_longest_word(self, sentence: str) -> str:
        """
        Remove punctuation marks and split a sentence into a list of words.
        Find the longest split word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return: longest split word that is in the self.word_list. 
                 Return '' if self.word_list is empty.
        """
        if not self.word_list:
            return ''
        
        # Remove punctuation and split the sentence into words
        words = re.findall(r'\b\w+\b', sentence)
        
        # Filter words that are in the word list
        valid_words = [word for word in words if word in self.word_list]
        
        # Find the longest word
        longest_word = max(valid_words, key=len, default='')
        
        return longest_word

