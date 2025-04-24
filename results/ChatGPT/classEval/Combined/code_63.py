import re
from collections import Counter

class NLPDataProcessor:
    """
    The class processes NLP data by extracting words from a list of strings, calculating the frequency of each word, 
    and returning the top 5 most frequent words.
    """

    def process_data(self, string_list):
        """
        Keep only English letters and spaces in the string, convert to lower case, and split into a list of words.
        :param string_list: a list of strings
        :return: words_list: a list of words lists
        """
        words_list = [
            re.sub(r'[^a-zA-Z\s]', '', string).lower().split()
            for string in string_list
        ]
        return words_list

    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words lists, and return the top 5 most common words.
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        """
        word_counter = Counter(word for words in words_list for word in words)
        return dict(word_counter.most_common(5))

    def process(self, string_list):
        """
        Process the input strings to extract words and calculate their frequencies.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary
        """
        words_list = self.process_data(string_list)
        return self.calculate_word_frequency(words_list)