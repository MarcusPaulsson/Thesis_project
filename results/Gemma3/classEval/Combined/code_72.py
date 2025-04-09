import re

class RegexUtils:
    """
    The class provides methods to match, find all occurrences, split, and substitute text using regular expressions.
    It also includes predefined patterns for validating phone numbers and extracting email addresses.
    """

    def match(self, pattern, text):
        """
        Check if the text matches the regular expression.

        :param pattern: The regular expression pattern (string).
        :param text: The text to match (string).
        :return: True if the text matches the pattern, False otherwise (bool).
        """
        return bool(re.match(pattern, text))

    def findall(self, pattern, text):
        """
        Find all matching substrings in the text.

        :param pattern: The regular expression pattern (string).
        :param text: The text to search (string).
        :return: A list of all matching substrings (list of strings).
        """
        return re.findall(pattern, text)

    def split(self, pattern, text):
        """
        Split the text based on the regular expression pattern.

        :param pattern: The regular expression pattern (string).
        :param text: The text to split (string).
        :return: A list of substrings after splitting (list of strings).
        """
        return re.split(pattern, text)

    def sub(self, pattern, replacement, text):
        """
        Replace substrings matched by the regular expression with the specified replacement.

        :param pattern: The regular expression pattern (string).
        :param replacement: The replacement string (string).
        :param text: The text to perform the substitution on (string).
        :return: The text after the substitution (string).
        """
        return re.sub(pattern, replacement, text)

    def generate_email_pattern(self):
        """
        Generate a regular expression pattern for matching email addresses.

        :return: The email address pattern (string).
        """
        return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def generate_phone_number_pattern(self):
        """
        Generate a regular expression pattern for matching phone numbers in the format XXX-XXX-XXXX.

        :return: The phone number pattern (string).
        """
        return r'\b\d{3}-\d{3}-\d{4}\b'

    def generate_split_sentences_pattern(self):
        """
        Generate a regular expression pattern for splitting sentences.

        :return: The sentence splitting pattern (string).
        """
        return r'[.!?][\s]{1,2}(?=[A-Z])'

    def split_sentences(self, text):
        """
        Split the text into a list of sentences.

        :param text: The text to split (string).
        :return: A list of sentences (list of strings).
        """
        sentences = re.split(self.generate_split_sentences_pattern(), text)
        return [s.strip() for s in sentences]

    def validate_phone_number(self, phone_number):
        """
        Validate if the given phone number matches the expected format.

        :param phone_number: The phone number to validate (string).
        :return: True if the phone number is valid, False otherwise (bool).
        """
        pattern = self.generate_phone_number_pattern()
        return bool(re.match(pattern, phone_number))

    def extract_email(self, text):
        """
        Extract all email addresses from the text.

        :param text: The text to extract emails from (string).
        :return: A list of extracted email addresses (list of strings).
        """
        pattern = self.generate_email_pattern()
        return re.findall(pattern, text)