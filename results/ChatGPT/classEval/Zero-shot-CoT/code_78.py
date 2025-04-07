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
        """
        # Using regex to split sentences while ignoring abbreviations like Mr.
        pattern = r'(?<!\bMr\.)(?<!\b[A-Z]\.)(?<!\b[A-Z]\.\s)([.?\!])\s'
        return [s.strip() + ('' if s.endswith(('.', '?', '!')) else '.') for s in re.split(pattern, sentences_string) if s]

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        """
        # Count words by splitting and filtering out non-alphabetic words
        return len([word for word in sentence.split() if word.isalpha()])

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        """
        sentences = self.split_sentences(sentences_string)
        return max((self.count_words(sentence) for sentence in sentences), default=0)