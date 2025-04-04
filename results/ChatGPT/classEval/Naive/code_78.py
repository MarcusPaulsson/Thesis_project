import re

class SplitSentence:
    """
    The class allows to split sentences, count words in a sentence, and process a text file to find the maximum word count.
    """

    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and have a space after that. 
        Note that Mr. also ends with . but is not considered a sentence.
        :param sentences_string: string, string to split
        :return: list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
        # Using regex to split on '. ' or '? '
        return re.split(r'(?<!\bMr)\. |(?<!\bMr)\? ', sentences_string)

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. 
        Words are separated by spaces, punctuation marks and numbers are not counted as words.
        :param sentence: string, sentence to be counted, where words are separated by spaces
        :return: int, number of words in the sentence
        >>> ss = SplitSentence()
        >>> ss.count_words("abc def")
        2
        """
        # Using regex to find words (excluding numbers and punctuation)
        words = re.findall(r'\b[a-zA-Z]+\b', sentence)
        return len(words)

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return: int, the number of words in the longest sentence
        >>> ss = SplitSentence()
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
        sentences = self.split_sentences(sentences_string)
        max_word_count = max(self.count_words(sentence) for sentence in sentences)
        return max_word_count