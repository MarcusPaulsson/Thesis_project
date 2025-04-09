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

        for word, tag in zip(words, pos_tags):
            if tag.startswith('VB'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='v'))
            elif tag.startswith('NN'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='n'))
            elif tag.startswith('JJ'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='a'))
            else:
                lemmatized_words.append(word)
        
        return lemmatized_words

    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        """
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        return [tag for word, tag in pos_tag(words)]

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        """
        return sentence.translate(str.maketrans('', '', string.punctuation))

