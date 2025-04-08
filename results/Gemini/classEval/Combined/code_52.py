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
    A class for performing lemmatization, part-of-speech tagging, and punctuation removal on sentences using NLTK.
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
        Tokenizes the sentence, removes punctuation, and returns a list of part-of-speech tags.

        Args:
            sentence (str): The input sentence.

        Returns:
            list: A list of part-of-speech tags for each word in the sentence.
        """
        sentence = self.remove_punctuation(sentence)
        tokens = word_tokenize(sentence)
        pos_tags = pos_tag(tokens)
        return [tag for token, tag in pos_tags]

    def lemmatize_sentence(self, sentence):
        """
        Lemmatizes the input sentence based on the part-of-speech tags of the words.

        Args:
            sentence (str): The input sentence.

        Returns:
            list: A list of lemmatized words.
        """
        sentence = self.remove_punctuation(sentence)
        tokens = word_tokenize(sentence)
        pos_tags = self.get_pos_tag(sentence)
        lemmatized_words = []

        for i, token in enumerate(tokens):
            pos_tag = pos_tags[i]
            lemmatized_word = self.lemmatizer.lemmatize(token, self.get_wordnet_pos(pos_tag))
            lemmatized_words.append(lemmatized_word)

        return lemmatized_words

    def get_wordnet_pos(self, treebank_tag):
        """
        Converts a Penn Treebank part-of-speech tag to a WordNet part-of-speech tag.

        Args:
            treebank_tag (str): The Penn Treebank part-of-speech tag.

        Returns:
            str: The corresponding WordNet part-of-speech tag ('a', 'v', 'n', 'r') or None if no mapping is found.
        """
        if treebank_tag.startswith('J'):
            return 'a'  # adjective
        elif treebank_tag.startswith('V'):
            return 'v'  # verb
        elif treebank_tag.startswith('N'):
            return 'n'  # noun
        elif treebank_tag.startswith('R'):
            return 'r'  # adverb
        else:
            return 'n' # Default to noun if no match

if __name__ == '__main__':
    # Example usage
    lemmatization = Lemmatization()
    sentence = "The dogs are running quickly."
    lemmatized_sentence = lemmatization.lemmatize_sentence(sentence)
    print(f"Original sentence: {sentence}")
    print(f"Lemmatized sentence: {lemmatized_sentence}")

    pos_tags = lemmatization.get_pos_tag(sentence)
    print(f"POS tags: {pos_tags}")

    sentence_with_punct = "Hello, world!"
    no_punct = lemmatization.remove_punctuation(sentence_with_punct)
    print(f"Original with punct: {sentence_with_punct}")
    print(f"No punct: {no_punct}")