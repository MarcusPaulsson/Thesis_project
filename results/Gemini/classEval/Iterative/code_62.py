class NLPDataProcessor:
    """
    The class processes NLP data by removing stop words from a list of strings using a pre-defined stop word list.
    """

    def __init__(self, stop_words=None):
        """
        Initializes the NLPDataProcessor with an optional custom stop word list.
        If no stop words are provided, the default list ['a', 'an', 'the'] is used.
        """
        if stop_words is None:
            self.stop_words = ['a', 'an', 'the']
        else:
            self.stop_words = stop_words

    def construct_stop_word_list(self):
        """
        Returns the stop word list.  This method is now largely redundant,
        but kept for backwards compatibility, returning the initialized stop words.
        :return: a list of stop words
        >>> processor = NLPDataProcessor()
        >>> processor.construct_stop_word_list()
        ['a', 'an', 'the']
        """
        return self.stop_words

    def remove_stop_words(self, string_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :return: a list of lists of words without stop words
        >>> processor = NLPDataProcessor()
        >>> processor.remove_stop_words(['This is a test.'])
        [['This', 'is', 'test.']]
        >>> processor.remove_stop_words(['This is a test a an the.'])
        [['This', 'is', 'test']]
        """
        result = []
        for string in string_list:
            words = string.split()
            filtered_words = [word for word in words if word.lower() not in self.stop_words]
            result.append(filtered_words)
        return result

    def process(self, string_list):
        """
        Removes stop words from a list of strings using the processor's stop word list.
        :param string_list: a list of strings
        :return: a list of lists of words without stop words
        >>> processor = NLPDataProcessor()
        >>> processor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        >>> processor = NLPDataProcessor(stop_words=['is', 'a'])
        >>> processor.process(['This is a test.'])
        [['This', 'test.']]
        """
        return self.remove_stop_words(string_list)


if __name__ == '__main__':
    import doctest
    doctest.testmod()