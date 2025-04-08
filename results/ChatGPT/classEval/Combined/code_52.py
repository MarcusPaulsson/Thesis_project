import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string
import unittest

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


class TestLemmatization(unittest.TestCase):
    def setUp(self):
        self.lemmatization = Lemmatization()

    def test_lemmatize_sentence(self):
        sentences = [
            ("I am running in a race.", ['I', 'be', 'run', 'in', 'a', 'race']),
            ("Until the beating, Cantanco's eyesight had been weak, but adequate.", ['Until', 'the', 'beating', 'Cantanco', 'eyesight', 'have', 'be', 'weak', 'but', 'adequate']),
            ("The dog's barked at the mailman.", ['The', 'dog', 'bark', 'at', 'the', 'mailman']),
            ("He was running and eating at same time.", ['He', 'be', 'run', 'and', 'eat', 'at', 'same', 'time']),
            ("I was taking a ride in the car.", ['I', 'be', 'take', 'a', 'ride', 'in', 'the', 'car']),
        ]

        for sentence, expected in sentences:
            self.assertEqual(self.lemmatization.lemmatize_sentence(sentence), expected)

    def test_get_pos_tag(self):
        sentences = [
            ("I am running in a race.", ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']),
            ("Cantanco's eyesight had been weak, but adequate.", ['NNP', 'NN', 'VBD', 'VBN', 'JJ', 'CC', 'JJ']),
            ("The dog's barked at the mailman.", ['DT', 'NNS', 'VBD', 'IN', 'DT', 'NN']),
            ("He was running and eating at same time.", ['PRP', 'VBD', 'VBG', 'CC', 'VBG', 'IN', 'JJ', 'NN']),
            ("I was taking a ride in the car.", ['PRP', 'VBD', 'VBG', 'DT', 'NN', 'IN', 'DT', 'NN']),
        ]

        for sentence, expected in sentences:
            self.assertEqual(self.lemmatization.get_pos_tag(sentence), expected)

    def test_remove_punctuation(self):
        sentences = [
            ("I am running in a race.", "I am running in a race"),
            ("Until the beating, Cantanco's eyesight had been weak, but adequate.", 'Until the beating Cantanco eyesight had been weak but adequate'),
            ("The dog's barked at the mailman!!!", 'The dogs barked at the mailman'),
            ("He was running and eating at same time...", 'He was running and eating at same time '),
            ("Is this a test? I hope it is...", 'Is this a test I hope it is'),
        ]

        for sentence, expected in sentences:
            self.assertEqual(self.lemmatization.remove_punctuation(sentence), expected)


if __name__ == "__main__":
    unittest.main()