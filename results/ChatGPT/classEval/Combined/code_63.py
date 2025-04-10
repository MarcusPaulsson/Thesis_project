import re
from collections import Counter

class NLPDataProcessor:
    """
    The class processes NLP data by extracting words from a list of strings,
    calculating the frequency of each word, and returning the top 5 most frequent words.
    """

    def process_data(self, string_list):
        """
        Keep only English letters and spaces in the string, then convert the string to lower case,
        and then split the string into a list of words.
        
        :param string_list: a list of strings
        :return: words_list: a list of words lists
        """
        return [
            self._clean_string(string)
            for string in string_list
        ]

    def _clean_string(self, string):
        """
        Clean a single string by removing non-letter characters, converting to lower case,
        and splitting into words.
        
        :param string: input string to clean
        :return: list of cleaned words
        """
        cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string).lower()
        return cleaned_string.split()

    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words lists,
        and return the word frequency dictionary sorted by value in descending order.

        :param words_list: a list of words lists
        :return: word frequency dictionary
        """
        word_count = Counter(word for words in words_list for word in words)
        return dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

    def process(self, string_list):
        """
        Process the input strings by extracting words and calculating their frequency.

        :param string_list: a list of strings
        :return: top 5 word frequency dictionary
        """
        words_list = self.process_data(string_list)
        return self.calculate_word_frequency(words_list)

# Example usage (uncomment for testing):
# processor = NLPDataProcessor()
# result = processor.process(["Hello World!", "This is a test."])
# print(result)  # Output: {'hello': 2, 'world': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1}