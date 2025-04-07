import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string

# Download necessary NLTK data
try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')


class Lemmatization:
    """
    A class for performing lemmatization on sentences using NLTK.
    It includes functionality for removing punctuation, tokenizing,
    part-of-speech tagging, and lemmatizing words based on their POS tags.
    """

    def __init__(self):
        """
        Initializes the Lemmatization class with a WordNetLemmatizer.
        """
        self.lemmatizer = WordNetLemmatizer()

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input sentence.

        Args:
            sentence (str): The input sentence.

        Returns:
            str: The sentence with punctuation removed.
        """
        translator = str.maketrans('', '', string.punctuation)
        return sentence.translate(translator)

    def get_pos_tag(self, sentence):
        """
        Tokenizes the input sentence and tags each word with its part of speech.

        Args:
            sentence (str): The input sentence.

        Returns:
            list: A list of POS tags corresponding to each word in the sentence.
        """
        words = word_tokenize(self.remove_punctuation(sentence))
        pos_tags = pos_tag(words)
        return [tag for word, tag in pos_tags]

    def lemmatize_sentence(self, sentence):
        """
        Lemmatizes the words in the input sentence based on their POS tags.

        Args:
            sentence (str): The input sentence.

        Returns:
            list: A list of lemmatized words.
        """
        words = word_tokenize(self.remove_punctuation(sentence))
        pos_tags = self.get_pos_tag(sentence)
        lemmatized_words = []
        for word, tag in zip(words, pos_tags):
            if tag.startswith('V'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='v'))
            elif tag.startswith('N'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='n'))
            elif tag.startswith('J'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='a'))
            elif tag.startswith('R'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='r'))
            else:
                lemmatized_words.append(self.lemmatizer.lemmatize(word))
        return lemmatized_words