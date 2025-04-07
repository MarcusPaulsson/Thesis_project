import re
from collections import Counter
from typing import List, Dict

class NLPDataProcessor2:
    """
    The class processes NLP data by extracting words from a list of strings,
    calculating the frequency of each word, and returning the top N most frequent words.
    """

    def __init__(self, top_n: int = 5):
        """
        Initializes the NLPDataProcessor2 with the desired number of top words to return.

        :param top_n: The number of top frequent words to return. Defaults to 5.
        """
        self.top_n = top_n

    def process_data(self, string_list: List[str]) -> List[List[str]]:
        """
        Cleans and tokenizes a list of strings.

        Keeps only English letters and spaces in the string, then converts the string
        to lower case, and then splits the string into a list of words.

        :param string_list: A list of strings.
        :return: A list of lists of words.
        """
        words_list = []
        for string in string_list:
            cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string)
            cleaned_string = cleaned_string.lower()
            words = cleaned_string.split()
            words_list.append(words)
        return words_list

    def calculate_word_frequency(self, words_list: List[List[str]]) -> Dict[str, int]:
        """
        Calculates the word frequency of each word in the list of word lists.

        :param words_list: A list of lists of words.
        :return: A dictionary of word frequencies, where the key is the word and the value is its frequency.
        """
        word_counts = Counter()
        for words in words_list:
            word_counts.update(words)
        return dict(word_counts)

    def get_top_n_words(self, word_frequency: Dict[str, int]) -> Dict[str, int]:
        """
        Returns the top N most frequent words from a word frequency dictionary.

        :param word_frequency: A dictionary of word frequencies.
        :return: A dictionary containing the top N most frequent words and their frequencies.
        """
        sorted_words = sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)
        return dict(sorted_words[:self.top_n])

    def process(self, string_list: List[str]) -> Dict[str, int]:
        """
        Processes a list of strings to extract, clean, and count word frequencies,
        then returns the top N most frequent words.

        :param string_list: A list of strings to process.
        :return: A dictionary containing the top N most frequent words and their frequencies.
        """
        words_list = self.process_data(string_list)
        word_frequency = self.calculate_word_frequency(words_list)
        top_words = self.get_top_n_words(word_frequency)
        return top_words