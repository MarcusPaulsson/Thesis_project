class NLPDataProcessor:
    """
    The class processes NLP data by removing stop words from a list of strings using a pre-defined stop word list.
    """

    @staticmethod
    def construct_stop_word_list():
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        """
        return ['a', 'an', 'the']

    @staticmethod
    def remove_stop_words(string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :param stop_word_list: a list of stop words
        :return: a list of words without stop words
        """
        stop_word_set = set(stop_word_list)
        return [
            [word for word in string.split() if word not in stop_word_set]
            for string in string_list
        ]

    def process(self, string_list):
        """
        Construct a stop word list and remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :return: a list of words without stop words
        """
        stop_word_list = self.construct_stop_word_list()
        return self.remove_stop_words(string_list, stop_word_list)