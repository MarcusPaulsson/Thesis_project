import re
from collections import Counter

class NLPDataProcessor2:
    """
    The class processes NLP data by extracting words from a list of strings, calculating the frequency of each word, and returning the top 5 most frequent words.
    """

    def process_data(self, string_list):
        words_list = []
        for s in string_list:
            # Keep only English letters and spaces, convert to lower case, and split into words
            cleaned_string = re.sub(r'[^a-zA-Z\s]', '', s).lower()
            words_list.append(cleaned_string.split())
        return words_list

    def calculate_word_frequency(self, words_list):
        # Flatten the list of words lists
        flat_list = [word for sublist in words_list for word in sublist]
        # Calculate frequency of each word
        word_freq = Counter(flat_list)
        # Sort by frequency and get the top 5
        return dict(word_freq.most_common(5))

    def process(self, string_list):
        words_list = self.process_data(string_list)
        return self.calculate_word_frequency(words_list)

# Example usage
nlp_processor = NLPDataProcessor2()
print(nlp_processor.process(['This is a test.', 'This is another test.']))