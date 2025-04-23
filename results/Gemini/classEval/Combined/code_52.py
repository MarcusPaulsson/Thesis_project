import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string


nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

class Lemmatization:
    """
    This is a class about Lemmatization, which utilizes the nltk library to perform lemmatization and part-of-speech tagging on sentences, as well as remove punctuation.
    """

    def __init__(self):
        """
        creates a WordNetLemmatizer object and stores it in the self.lemmatizer member variable.
        """
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
        :param sentence: a sentence str
        :return: a list of words which have been lemmatized.
        """
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        pos_tags = self.get_pos_tag(sentence)
        lemmatized_words = []
        for word, pos_tag in zip(words, pos_tags):
            lemma = self.lemmatize_word(word, pos_tag)
            lemmatized_words.append(lemma)
        return lemmatized_words

    def lemmatize_word(self, word, pos_tag):
        """
        Lemmatizes a single word based on its part-of-speech tag.
        :param word: The word to lemmatize.
        :param pos_tag: The part-of-speech tag of the word.
        :return: The lemmatized word.
        """
        if pos_tag.startswith('N'):
            return self.lemmatizer.lemmatize(word, pos='n')
        elif pos_tag.startswith('V'):
            return self.lemmatizer.lemmatize(word, pos='v')
        elif pos_tag.startswith('J'):
            return self.lemmatizer.lemmatize(word, pos='a')
        elif pos_tag.startswith('R'):
            return self.lemmatizer.lemmatize(word, pos='r')
        else:
            return self.lemmatizer.lemmatize(word)

    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        """
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        pos_tags = pos_tag(words)
        return [tag for word, tag in pos_tags]

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        """
        return sentence.translate(str.maketrans('', '', string.punctuation))