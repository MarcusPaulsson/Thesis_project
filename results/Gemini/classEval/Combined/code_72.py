import re

class RegexUtils:
    """
    The class provides methods to match, find all occurrences, split, and substitute text using regular expressions.
    It also includes predefined patterns for validating phone numbers and extracting email addresses.
    """

    def match(self, pattern, text):
        """
        Check if the text matches the regular expression.

        :param pattern: str, Regular expression pattern.
        :param text: str, Text to match.
        :return: bool, True if the text matches the regular expression, False otherwise.
        """
        try:
            return bool(re.match(pattern, text))
        except re.error as e:
            print(f"Regex error: {e}")
            return False

    def findall(self, pattern, text):
        """
        Find all matching substrings and return a list of all matching substrings.

        :param pattern: str, Regular expression pattern.
        :param text: str, Text to match.
        :return: list of str, List of all matching substrings.
        """
        try:
            return re.findall(pattern, text)
        except re.error as e:
            print(f"Regex error: {e}")
            return []

    def split(self, pattern, text):
        """
        Split text based on regular expression patterns and return a list of substrings.

        :param pattern: str, Regular expression pattern.
        :param text: str, Text to be split.
        :return: list of str, List of substrings after splitting.
        """
        try:
            return re.split(pattern, text)
        except re.error as e:
            print(f"Regex error: {e}")
            return [text]

    def sub(self, pattern, replacement, text):
        """
        Replace the substring matched by a regular expression with the specified string.

        :param pattern: str, Regular expression pattern.
        :param replacement: str, Text to replace with.
        :param text: str, Text to be replaced.
        :return: str, Text after replacement.
        """
        try:
            return re.sub(pattern, replacement, text)
        except re.error as e:
            print(f"Regex error: {e}")
            return text

    def generate_email_pattern(self):
        """
        Generate regular expression patterns that match email addresses.

        :return: str, Regular expression patterns that match email addresses.
        """
        return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def generate_phone_number_pattern(self):
        """
        Generate regular expression patterns that match phone numbers in the format XXX-XXX-XXXX.

        :return: str, Regular expression patterns that match phone numbers.
        """
        return r'\b\d{3}-\d{3}-\d{4}\b'

    def generate_split_sentences_pattern(self):
        """
        Generate regular expression patterns that match the end of sentences, followed by whitespace and a capital letter.

        :return: str, Regular expression patterns that match the middle characters of two sentences.
        """
        return r'[.!?][\s]{1,2}(?=[A-Z])'

    def split_sentences(self, text):
        """
        Split the text into a list of sentences.

        :param text: str, Text to be split.
        :return: list of str, Split text list.
        """
        pattern = self.generate_split_sentences_pattern()
        try:
            return re.split(pattern, text)
        except re.error as e:
            print(f"Regex error: {e}")
            return [text]

    def validate_phone_number(self, phone_number):
        """
        Verify if the phone number is valid based on XXX-XXX-XXXX format.

        :param phone_number: str, Phone number to be verified.
        :return: bool, True if the phone number is valid, False otherwise.
        """
        pattern = self.generate_phone_number_pattern()
        return self.match(pattern, phone_number)

    def extract_email(self, text):
        """
        Extract all email addresses from the text.

        :param text: str, Input text.
        :return: list of str, All extracted email addresses.
        """
        pattern = self.generate_email_pattern()
        return self.findall(pattern, text)