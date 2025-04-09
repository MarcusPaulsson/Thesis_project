import re

class SplitSentence:
    """
    The class allows to split sentences, count words in a sentence, and process a text to find the maximum word count.
    """

    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and have a space after that. 
        'Mr.' also ends with . but is not treated as a sentence.
        
        :param sentences_string: str, string to split
        :return: list, list of split sentences
        """
        sentences = re.split(r'(?<!Mr)(?<![A-Z]\.)[.?\s]+', sentences_string.strip())
        return [s.strip() for s in sentences if s.strip()]

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Words are separated by spaces and punctuation marks/numbers are not counted.
        
        :param sentence: str, sentence to be counted
        :return: int, number of words in the sentence
        """
        words = re.findall(r'\b[a-zA-Z]+\b', sentence)
        return len(words)

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence.
        
        :param sentences_string: str, undivided long sentence
        :return: int, number of words in the longest sentence
        """
        sentences = self.split_sentences(sentences_string)
        return max((self.count_words(sentence) for sentence in sentences), default=0)
