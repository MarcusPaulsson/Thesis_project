import re

class SplitSentence:
    """
    The class allows to split sentences, count words in a sentence, and process a text to find the maximum word count.
    """

    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and are followed by a space. 
        Note that abbreviations like Mr. do not count as sentence endings.
        
        :param sentences_string: str, string to split
        :return: list, split sentence list
        """
        pattern = r'(?<!\bMr\.)(?<!\b[A-Z]\.)(?<!\b[A-Z]\.[A-Z]\.)[.?\n]+(?=\s|$)'
        return [sentence.strip() for sentence in re.split(pattern, sentences_string) if sentence.strip()]

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Words are separated by spaces, 
        and punctuation marks and numbers are not counted as words.
        
        :param sentence: str, sentence to be counted
        :return: int, number of words in the sentence
        """
        words = re.findall(r'\b[a-zA-Z]+\b', sentence)
        return len(words)

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence.
        
        :param sentences_string: str, undivided long sentence
        :return: int, the number of words in the longest sentence
        """
        sentences = self.split_sentences(sentences_string)
        return max((self.count_words(sentence) for sentence in sentences), default=0)