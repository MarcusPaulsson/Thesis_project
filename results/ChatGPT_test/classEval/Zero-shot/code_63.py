import re
from collections import Counter

class NLPDataProcessor2:
    """
    The class processes NLP data by extracting words from a list of strings, calculating the frequency of each word, and returning the top 5 most frequent words.
    """

    def process_data(self, string_list):
        words_list = []
        for string in string_list:
            # Keep only English letters and spaces, convert to lower case, and split into words
            cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string).lower()
            words = cleaned_string.split()
            words_list.append(words)
        return words_list

    def calculate_word_frequency(self, words_list):
        word_count = Counter()
        for words in words_list:
            word_count.update(words)
        # Sort the dictionary by value in descending order and get the top 5
        return dict(word_count.most_common(5))

    def process(self, string_list):
        words_list = self.process_data(string_list)
        return self.calculate_word_frequency(words_list)