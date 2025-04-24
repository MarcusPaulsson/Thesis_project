import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

class Lemmatization:
    """
    This class performs lemmatization and part-of-speech tagging on sentences, as well as removing punctuation.
    """

    def __init__(self):
        """
        Initializes the WordNetLemmatizer.
        """
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        """
        Lemmatizes the words in the input sentence based on their part of speech.
        :param sentence: A sentence string.
        :return: A list of lemmatized words.
        """
        cleaned_sentence = self.remove_punctuation(sentence)
        tokens = word_tokenize(cleaned_sentence)
        pos_tags = self.get_pos_tag(tokens)

        lemmatized_words = [
            self.lemmatizer.lemmatize(token, self.get_wordnet_pos(pos)) 
            for token, pos in zip(tokens, pos_tags)
        ]

        return lemmatized_words

    def get_pos_tag(self, tokens):
        """
        Gets the part of speech tags for each word in the input tokens.
        :param tokens: A list of word tokens.
        :return: A list of part of speech tags.
        """
        return [tag for _, tag in pos_tag(tokens)]

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: A sentence string.
        :return: A string without punctuation.
        """
        return sentence.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def get_wordnet_pos(treebank_tag):
        """
        Converts treebank tags to WordNet POS tags.
        :param treebank_tag: A treebank part of speech tag.
        :return: Corresponding WordNet POS tag.
        """
        if treebank_tag.startswith('J'):
            return 'a'  # Adjective
        elif treebank_tag.startswith('V'):
            return 'v'  # Verb
        elif treebank_tag.startswith('N'):
            return 'n'  # Noun
        elif treebank_tag.startswith('R'):
            return 'r'  # Adverb
        else:
            return 'n'  # Default to noun if no match