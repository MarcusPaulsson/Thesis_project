import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string


# Download necessary NLTK data files
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')


class Lemmatization:
    """
    A class for performing lemmatization and part-of-speech tagging on sentences,
    utilizing the NLTK library.
    """

    def __init__(self):
        """Initializes the WordNetLemmatizer."""
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        """
        Lemmatizes the words in a sentence based on their part of speech after removing punctuation.
        
        :param sentence: A sentence as a string.
        :return: A list of lemmatized words.
        """
        cleaned_sentence = self.remove_punctuation(sentence)
        tokens = word_tokenize(cleaned_sentence)
        pos_tags = self.get_pos_tag(cleaned_sentence)

        lemmatized_words = [
            self.lemmatizer.lemmatize(token, self.map_pos_to_wordnet(pos)) 
            for token, pos in zip(tokens, pos_tags)
        ]
        return lemmatized_words

    def get_pos_tag(self, sentence):
        """
        Gets the part of speech tags for each word in a sentence after removing punctuation.
        
        :param sentence: A sentence as a string.
        :return: A list of part of speech tags.
        """
        cleaned_sentence = self.remove_punctuation(sentence)
        tokens = word_tokenize(cleaned_sentence)
        pos_tags = pos_tag(tokens)
        return [tag for _, tag in pos_tags]

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input sentence.
        
        :param sentence: A sentence as a string.
        :return: A string without punctuation.
        """
        return sentence.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def map_pos_to_wordnet(pos):
        """
        Maps NLTK POS tags to WordNet POS tags.

        :param pos: A part of speech tag as a string.
        :return: Corresponding WordNet POS tag.
        """
        if pos.startswith('V'):
            return 'v'
        elif pos.startswith('N'):
            return 'n'
        elif pos.startswith('J'):
            return 'a'
        else:
            return 'n'  # Default to noun if not found

