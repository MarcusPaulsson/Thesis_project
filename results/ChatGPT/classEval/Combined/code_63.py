import re
from collections import Counter

class NLPDataProcessor:
    """
    The class processes NLP data by extracting words from a list of strings, 
    calculating the frequency of each word, and returning the top 5 most frequent words.
    """

    def process_data(self, string_list):
        """
        Keep only English letters and spaces in the string, convert to lower case, 
        and split into a list of words.
        :param string_list: a list of strings
        :return: A list of lists, where each inner list contains the cleaned words from the corresponding string.
        """
        words_list = []
        for string in string_list:
            cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string).lower()
            words = cleaned_string.split() if cleaned_string else []
            words_list.append(words)
        return words_list

    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words lists,
        and return the top 5 most frequent words as a dictionary.
        :param words_list: a list of lists containing words
        :return: A dictionary of the top 5 word frequencies, sorted by frequency.
        """
        word_counts = Counter()
        for words in words_list:
            word_counts.update(words)
        return dict(word_counts.most_common(5))

    def process(self, string_list):
        """
        Process the input strings to extract word frequencies.
        :param string_list: a list of strings
        :return: A dictionary of the top 5 word frequencies.
        """
        words_list = self.process_data(string_list)
        return self.calculate_word_frequency(words_list)