import re

class SplitSentence:
    """
    The class allows to split sentences, count words in a sentence, and process a text to find the maximum word count.
    """

    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and are not preceded by abbreviations like 'Mr.'.
        :param sentences_string: string, string to split
        :return: list, split sentence list
        """
        sentence_pattern = r'(?<!\bMr\.)(?<!\b[A-Z]\.[A-Z]\.)[^?.!]+[?.!](?=\s|$)'
        return [sentence.strip() for sentence in re.findall(sentence_pattern, sentences_string)]

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Words are separated by spaces; punctuation marks and numbers are not counted.
        :param sentence: string, sentence to be counted
        :return: int, number of words in the sentence
        """
        words = [word for word in sentence.split() if word.isalpha()]
        return len(words)

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence.
        :param sentences_string: string, undivided long sentence
        :return: int, the number of words in the longest sentence
        """
        sentences = self.split_sentences(sentences_string)
        return max((self.count_words(sentence) for sentence in sentences), default=0)