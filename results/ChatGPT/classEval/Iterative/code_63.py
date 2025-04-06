import re
from collections import Counter

class NLPDataProcessor:
    """
    The class processes NLP data by extracting words from a list of strings, calculating the frequency of each word,
    and returning the top 5 most frequent words.
    """

    def process_data(self, string_list):
        """
        Cleans the input strings by removing non-alphabetic characters and converting to lower case.
        
        :param string_list: List of strings to process
        :return: List of lists, where each inner list contains the words from the corresponding string
        """
        words_list = []
        for string in string_list:
            cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string).lower()
            words = cleaned_string.split()
            words_list.append(words)
        return words_list

    def calculate_word_frequency(self, words_list):
        """
        Calculates the frequency of words in the provided list of lists of words.
        
        :param words_list: List of lists containing words
        :return: Dictionary of the top 5 most common words and their frequencies
        """
        word_counter = Counter()
        for words in words_list:
            word_counter.update(words)
        return dict(word_counter.most_common(5))

    def process(self, string_list):
        """
        Processes the input strings to return the top 5 most frequent words.
        
        :param string_list: List of strings to process
        :return: Dictionary of the top 5 most common words and their frequencies
        """
        words_list = self.process_data(string_list)
        return self.calculate_word_frequency(words_list)