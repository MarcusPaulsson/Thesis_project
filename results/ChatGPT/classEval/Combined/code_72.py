import re

class RegexUtils:
    """
    The class provides methods to match, find all occurrences, split, and substitute text using regular expressions.
    It includes predefined patterns for validating phone numbers and extracting email addresses.
    """

    @staticmethod
    def match(pattern, text):
        """Check if the entire text matches the regular expression."""
        return bool(re.fullmatch(pattern, text))

    @staticmethod
    def findall(pattern, text):
        """Find all matching substrings and return a list of all matches."""
        return re.findall(pattern, text)

    @staticmethod
    def split(pattern, text):
        """Split text based on regular expression patterns and return a list of substrings."""
        return re.split(pattern, text)

    @staticmethod
    def sub(pattern, replacement, text):
        """Replace the substring matched by a regular expression with the specified string."""
        return re.sub(pattern, replacement, text)

    @staticmethod
    def generate_email_pattern():
        """Generate a regex pattern that matches email addresses."""
        return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    @staticmethod
    def generate_phone_number_pattern():
        """Generate a regex pattern that matches phone numbers."""
        return r'\b\d{3}-\d{3}-\d{4}\b'

    @staticmethod
    def generate_split_sentences_pattern():
        """Generate a regex pattern that matches sentence delimiters."""
        return r'[.!?][\s]+(?=[A-Z])'

    def split_sentences(self, text):
        """Split the text into a list of sentences without punctuation except for the last sentence."""
        sentences = re.split(self.generate_split_sentences_pattern(), text)
        return [sentence.strip() for sentence in sentences if sentence]

    def validate_phone_number(self, phone_number):
        """Verify if the phone number is valid."""
        return self.match(self.generate_phone_number_pattern(), phone_number)

    def extract_email(self, text):
        """Extract all email addresses from the text."""
        return self.findall(self.generate_email_pattern(), text)