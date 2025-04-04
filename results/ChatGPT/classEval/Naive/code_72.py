import re

class RegexUtils:
    """
    The class provides methods to match, find all occurrences, split, and substitute text using regular expressions.
    It also includes predefined patterns for validating phone numbers and extracting email addresses.
    """

    def match(self, pattern, text):
        """Check if the text matches the regular expression."""
        return bool(re.match(pattern, text))

    def findall(self, pattern, text):
        """Find all matching substrings and return a list of all matching substrings."""
        return re.findall(pattern, text)

    def split(self, pattern, text):
        """Split text based on regular expression patterns and return a list of substrings."""
        return re.split(pattern, text)

    def sub(self, pattern, replacement, text):
        """Replace the substring matched by a regular expression with the specified string."""
        return re.sub(pattern, replacement, text)

    def generate_email_pattern(self):
        """Generate regular expression patterns that match email addresses."""
        return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def generate_phone_number_pattern(self):
        """Generate regular expression patterns that match phone numbers."""
        return r'\b\d{3}-\d{3}-\d{4}\b'

    def generate_split_sentences_pattern(self):
        """Generate regular expression patterns that match the middle characters of two sentences."""
        return r'[.!?][\s]{1,2}(?=[A-Z])'

    def split_sentences(self, text):
        """Split the text into a list of sentences without punctuation except the last sentence."""
        sentences = re.split(self.generate_split_sentences_pattern(), text)
        return [sentence.strip(' ') for sentence in sentences if sentence]

    def validate_phone_number(self, phone_number):
        """Verify if the phone number is valid."""
        pattern = self.generate_phone_number_pattern()
        return bool(re.match(pattern, phone_number))

    def extract_email(self, text):
        """Extract all email addresses from the text."""
        pattern = self.generate_email_pattern()
        return self.findall(pattern, text)