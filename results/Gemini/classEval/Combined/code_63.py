import re
from collections import Counter

class NLPDataProcessor2:
    """
    The class processes NLP data by extracting words from a list of strings, calculating the frequency of each word, and returning the top 5 most frequent words.
    """

    def process_data(self, string_list):
        """
        Keeps only English letters and spaces in the string, then converts the string to lower case,
        and then splits the string into a list of words.
        :param string_list: a list of strings
        :return: words_list: a list of words lists
        """
        words_list = []
        for string in string_list:
            # Remove non-alphabetic characters and spaces
            cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string)
            # Convert to lowercase and split into words
            words = cleaned_string.lower().split()
            words_list.append(words)
        return words_list

    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words list,
        and sort the word frequency dictionary by value in descending order.
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        """
        word_counts = Counter()
        for words in words_list:
            word_counts.update(words)

        # Sort the word frequency dictionary by value in descending order and return Top 5
        sorted_word_counts = dict(word_counts.most_common(5))
        return sorted_word_counts

    def process(self, string_list):
        """
        Keeps only English letters and spaces in the string, then converts the string to lower case,
        and then splits the string into a list of words.
        Calculates the word frequency of each word in the list of words list,
        and returns the top 5 most frequent words.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        """
        words_list = self.process_data(string_list)
        word_frequency = self.calculate_word_frequency(words_list)
        return word_frequency