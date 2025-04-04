import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

class Lemmatization:
    """
    This class performs lemmatization and part-of-speech tagging on sentences, as well as removes punctuation.
    """

    def __init__(self):
        """
        Initializes the WordNetLemmatizer object.
        """
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        """
        Removes punctuation from the sentence, tokenizes it, tags parts of speech, 
        and lemmatizes the words based on their parts of speech.

        :param sentence: A sentence as a string.
        :return: A list of lemmatized words.
        
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_sentence("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']
        """
        sentence = self.remove_punctuation(sentence)
        tokens = word_tokenize(sentence)
        pos_tags = self.get_pos_tag(tokens)
        
        lemmatized_words = []
        for word, tag in zip(tokens, pos_tags):
            lemmatized_word = self.lemmatizer.lemmatize(word, pos=self.get_wordnet_pos(tag))
            lemmatized_words.append(lemmatized_word)
        
        return lemmatized_words

    def get_pos_tag(self, tokens):
        """
        Tags parts of speech for each word in the tokenized sentence.

        :param tokens: A list of tokens.
        :return: A list of part-of-speech tags for each token.
        
        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag(["I", "am", "running", "in", "a", "race"])
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']
        """
        return [tag for _, tag in pos_tag(tokens)]

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.

        :param sentence: A sentence as a string.
        :return: A string without punctuation.
        
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'
        """
        return sentence.translate(str.maketrans('', '', string.punctuation))

    def get_wordnet_pos(self, tag):
        """
        Converts the part-of-speech tag to a format understood by WordNetLemmatizer.

        :param tag: A part-of-speech tag.
        :return: A corresponding WordNet part-of-speech constant.
        """
        if tag.startswith('J'):
            return 'a'  # Adjective
        elif tag.startswith('V'):
            return 'v'  # Verb
        elif tag.startswith('N'):
            return 'n'  # Noun
        elif tag.startswith('R'):
            return 'r'  # Adverb
        else:
            return 'n'  # Default to noun