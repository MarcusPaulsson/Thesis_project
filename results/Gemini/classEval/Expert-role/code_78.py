import re

class SplitSentence:
    """
    The class allows to split sentences, count words in a sentence, and process a text file to find the maximum word count.
    """


    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. Please note that Mr. also end with . but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
        sentences = re.split(r'(?<!Mr)(?<!Mrs)(?<!Ms)\.|\?', sentences_string)
        sentences = [s.strip() + ('.' if sentences_string.count(s.strip() + '.') > sentences_string.count(s.strip() + '.') else '?' if sentences_string.count(s.strip() + '?') > sentences_string.count(s.strip() + '.') else '') for s in sentences if s.strip()]
        
        return sentences

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        >>> ss.count_words("abc def")
        2
        """
        words = re.findall(r'[a-zA-Z]+', sentence)
        return len(words)

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
        sentences = self.split_sentences(sentences_string)
        max_words = 0
        for sentence in sentences:
            word_count = self.count_words(sentence)
            if word_count > max_words:
                max_words = word_count
        return max_words