import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string
import unittest

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


class TestLemmatization(unittest.TestCase):
    def setUp(self):
        self.lemmatization = Lemmatization()

    def test_lemmatize_sentence(self):
        test_cases = [
            ("I am running in a race.", ['I', 'be', 'run', 'in', 'a', 'race']),
            ("Until the beating, Cantanco's eyesight had been weak, but adequate.", 
             ['Until', 'the', 'beating', 'Cantancos', 'eyesight', 'have', 'be', 'weak', 'but', 'adequate']),
            ("The dog's barked at the mailman.", ['The', 'dog', 'bark', 'at', 'the', 'mailman']),
            ("He was running and eating at same time.", ['He', 'be', 'run', 'and', 'eat', 'at', 'same', 'time']),
            ("I was taking a ride in the car.", ['I', 'be', 'take', 'a', 'ride', 'in', 'the', 'car'])
        ]
        
        for sentence, expected in test_cases:
            with self.subTest(sentence=sentence):
                self.assertEqual(self.lemmatization.lemmatize_sentence(sentence), expected)

    def test_get_pos_tag(self):
        test_cases = [
            ("I am running in a race.", ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']),
            ("Cantanco's eyesight had been weak, but adequate.", ['NNP', 'NN', 'VBD', 'VBN', 'JJ', 'CC', 'JJ']),
            ("The dog's barked at the mailman.", ['DT', 'NNS', 'VBD', 'IN', 'DT', 'NN']),
            ("He was running and eating at same time.", ['PRP', 'VBD', 'VBG', 'CC', 'VBG', 'IN', 'JJ', 'NN']),
            ("I was taking a ride in the car.", ['PRP', 'VBD', 'VBG', 'DT', 'NN', 'IN', 'DT', 'NN'])
        ]
        
        for sentence, expected in test_cases:
            with self.subTest(sentence=sentence):
                self.assertEqual(self.lemmatization.get_pos_tag(sentence), expected)

    def test_remove_punctuation(self):
        test_cases = [
            ("I am running in a race.", "I am running in a race"),
            ("Until the beating, Cantanco's eyesight had been weak, but adequate.", 
             'Until the beating Cantancos eyesight had been weak but adequate'),
            ("The dog's barked at the mailman!!!", 'The dogs barked at the mailman'),
            ("He was running and eating at same time...", 'He was running and eating at same time '),
            ("Is this a test? I hope it is...", 'Is this a test I hope it is')
        ]
        
        for sentence, expected in test_cases:
            with self.subTest(sentence=sentence):
                self.assertEqual(self.lemmatization.remove_punctuation(sentence), expected)

if __name__ == "__main__":
    unittest.main()