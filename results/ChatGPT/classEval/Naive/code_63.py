import re
from collections import Counter

class NLPDataProcessor:
    """
    The class processes NLP data by extracting words from a list of strings, calculating the frequency of each word, 
    and returning the top 5 most frequent words.
    """

    def process_data(self, string_list):
        """
        Keep only English letters and spaces in the string, convert the string to lower case,
        and split the string into a list of words.
        
        :param string_list: a list of strings
        :return: words_list: a list of words lists
        >>> NLPDataProcessor().process_data(['This is a test.'])
        [['this', 'is', 'a', 'test']]
        """
        words_list = []
        for string in string_list:
            cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string).lower()
            words_list.append(cleaned_string.split())
        return words_list

    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words lists, 
        and sort the word frequency dictionary by value in descending order.
        
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary
        >>> NLPDataProcessor().calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        flat_list = [word for sublist in words_list for word in sublist]
        word_count = Counter(flat_list)
        return dict(word_count.most_common(5))

    def process(self, string_list):
        """
        Process the input strings to calculate word frequency.
        
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary
        >>> NLPDataProcessor().process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        words_list = self.process_data(string_list)
        return self.calculate_word_frequency(words_list)