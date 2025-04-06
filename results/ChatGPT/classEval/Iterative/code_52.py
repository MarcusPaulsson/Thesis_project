import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string

# Download required NLTK resources
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

class Lemmatization:
    """
    A class for performing lemmatization and part-of-speech tagging on sentences, as well as removing punctuation.
    """

    def __init__(self):
        """
        Initializes the WordNetLemmatizer object.
        """
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        """
        Lemmatizes the words in the input sentence based on their part of speech.
        :param sentence: A sentence string
        :return: A list of lemmatized words.
        """
        # Remove punctuation and tokenize the sentence
        words = word_tokenize(self.remove_punctuation(sentence))
        # Get part of speech tags
        pos_tags = self.get_pos_tags(words)
        
        lemmatized_words = [
            self.lemmatizer.lemmatize(word, pos=self.get_wordnet_pos(tag))
            for word, tag in zip(words, pos_tags)
        ]
        
        return lemmatized_words

    def get_pos_tags(self, words):
        """
        Gets the part of speech tags for a list of words.
        :param words: A list of words
        :return: A list of part of speech tags.
        """
        return [tag for _, tag in pos_tag(words)]

    def get_wordnet_pos(self, tag):
        """
        Converts POS tag to a format compatible with WordNetLemmatizer.
        :param tag: A part of speech tag
        :return: A WordNet-compatible POS tag.
        """
        if tag.startswith('VB'):
            return 'v'
        elif tag.startswith('N'):
            return 'n'
        elif tag.startswith('J'):
            return 'a'
        elif tag.startswith('R'):
            return 'r'
        else:
            return 'n'  # Default to noun if no match

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: A sentence string
        :return: A string without punctuation.
        """
        return sentence.translate(str.maketrans('', '', string.punctuation))