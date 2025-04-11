import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string


nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

class Lemmatization:
    """
    A class for performing lemmatization and part-of-speech tagging on sentences, including punctuation removal.
    """

    def __init__(self):
        """Initializes the WordNetLemmatizer."""
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        """
        Lemmatizes the words in the input sentence based on their part of speech.
        
        :param sentence: A sentence string.
        :return: A list of lemmatized words.
        """
        cleaned_sentence = self.remove_punctuation(sentence)
        tokens = word_tokenize(cleaned_sentence)
        pos_tags = self.get_pos_tag(cleaned_sentence)
        
        return [
            self.lemmatizer.lemmatize(token, pos=self.get_wordnet_pos(tag))
            if tag in {'V', 'N', 'J'} else token 
            for token, tag in zip(tokens, pos_tags)
        ]

    def get_pos_tag(self, sentence):
        """
        Retrieves the part of speech tags for the words in the input sentence.
        
        :param sentence: A sentence string.
        :return: A list of part of speech tags.
        """
        cleaned_sentence = self.remove_punctuation(sentence)
        tokens = word_tokenize(cleaned_sentence)
        return [tag for _, tag in pos_tag(tokens)]

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        
        :param sentence: A sentence string.
        :return: A string without any punctuation.
        """
        return sentence.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def get_wordnet_pos(tag):
        """
        Converts the part-of-speech naming convention used by nltk to the one used by WordNet.
        
        :param tag: NLTK pos tag.
        :return: WordNet POS tag.
        """
        if tag.startswith('V'):
            return 'v'  # Verb
        elif tag.startswith('N'):
            return 'n'  # Noun
        elif tag.startswith('J'):
            return 'a'  # Adjective
        else:
            return 'n'  # Default to noun for other tags

