class NLPDataProcessor:
    """
    The class processes NLP data by removing stop words from a list of strings using a pre-defined stop word list.
    """

    @staticmethod
    def construct_stop_word_list():
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        >>> NLPDataProcessor.construct_stop_word_list()
        ['a', 'an', 'the']
        """
        return ['a', 'an', 'the']

    @staticmethod
    def remove_stop_words(string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :param stop_word_list: a list of stop words
        :return: a list of words without stop words
        >>> NLPDataProcessor.remove_stop_words(['This is a test.'], NLPDataProcessor.construct_stop_word_list())
        [['This', 'is', 'test.']]
        """
        return [[word for word in string.split() if word.lower() not in stop_word_list] for string in string_list]

    @staticmethod
    def process(string_list):
        """
        Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :return: a list of words without stop words
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        stop_words = NLPDataProcessor.construct_stop_word_list()
        return NLPDataProcessor.remove_stop_words(string_list, stop_words)