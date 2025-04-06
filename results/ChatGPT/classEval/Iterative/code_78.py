import re

class SplitSentence:
    """
    The class allows to split sentences, count words in a sentence, and process a text to find the maximum word count of sentences.
    """

    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. 
        Note that Mr. also ends with . but is not treated as a sentence end.
        
        :param sentences_string: str, string to split
        :return: list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
        return re.split(r'(?<!Mr)\. |\? ', sentences_string.strip())

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Words are defined as sequences of alphabetic characters.
        
        :param sentence: str, sentence to be counted
        :return: int, number of words in the sentence
        >>> ss = SplitSentence()
        >>> ss.count_words("abc def")
        2
        """
        words = re.findall(r'\b[a-zA-Z]+\b', sentence)
        return len(words)

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence.
        
        :param sentences_string: str, undivided long sentence
        :return: int, the number of words in the longest sentence
        >>> ss = SplitSentence()
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
        sentences = self.split_sentences(sentences_string)
        # Use max with a default value of 0 to handle empty input
        max_words = max((self.count_words(sentence) for sentence in sentences), default=0)
        return max_words