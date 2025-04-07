import re

class RegexUtils:
    """
    The class provides methods to match, find all occurrences, split, and substitute text using regular expressions.
    It also includes predefined patterns for validating phone numbers and extracting email addresses.
    """

    def match(self, pattern, text):
        """
        Check if the text matches the regular expression.
        :param pattern: string, Regular expression pattern
        :param text: string, Text to match
        :return: bool, True if the text matches the pattern, False otherwise
        """
        return re.fullmatch(pattern, text) is not None

    def findall(self, pattern, text):
        """
        Find all matching substrings and return a list of all matching substrings.
        :param pattern: string, Regular expression pattern
        :param text: string, Text to match
        :return: list of string, List of all matching substrings
        """
        return re.findall(pattern, text)

    def split(self, pattern, text):
        """
        Split text based on regular expression patterns and return a list of substrings.
        :param pattern: string, Regular expression pattern
        :param text: string, Text to be split
        :return: list of string, List of substrings after splitting
        """
        return re.split(pattern, text)

    def sub(self, pattern, replacement, text):
        """
        Replace the substring matched by a regular expression with the specified string.
        :param pattern: string, Regular expression pattern
        :param replacement: string, Text to replace with
        :param text: string, Text to be replaced
        :return: string, Text after replacement
        """
        return re.sub(pattern, replacement, text)

    def generate_email_pattern(self):
        """
        Generate regular expression patterns that match email addresses.
        :return: string, Regular expression patterns that match email addresses
        """
        return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def generate_phone_number_pattern(self):
        """
        Generate regular expression patterns that match phone numbers.
        :return: string, Regular expression patterns that match phone numbers
        """
        return r'\b\d{3}-\d{3}-\d{4}\b'

    def generate_split_sentences_pattern(self):
        """
        Generate regular expression patterns that match the middle characters of two sentences.
        :return: string, Regular expression patterns that match the middle characters of two sentences
        """
        return r'[.!?][\s]+(?=[A-Z])'

    def split_sentences(self, text):
        """
        Split the text into a list of sentences.
        :param text: Text to be split
        :return: list of string, Split Text List
        """
        return re.split(r'(?<=[.!?]) +', text)

    def validate_phone_number(self, phone_number):
        """
        Verify if the phone number is valid.
        :param phone_number: Phone number to be verified
        :return: bool, True if the phone number is valid, False otherwise
        """
        return self.match(self.generate_phone_number_pattern(), phone_number)

    def extract_email(self, text):
        """
        Extract all email addresses from the text.
        :param text: string, input text
        :return: list of string, All extracted email addresses
        """
        return self.findall(self.generate_email_pattern(), text)