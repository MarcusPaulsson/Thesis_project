import re

class RegexUtils:
    """
    A utility class for performing various operations using regular expressions,
    including matching, finding occurrences, splitting text, and substituting text.
    It also provides predefined patterns for validating phone numbers and extracting email addresses.
    """

    @staticmethod
    def match(pattern, text):
        """Check if the text matches the regular expression."""
        return bool(re.fullmatch(pattern, text))

    @staticmethod
    def findall(pattern, text):
        """Find all matching substrings and return a list of them."""
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
        """Generate a regular expression pattern that matches email addresses."""
        return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    @staticmethod
    def generate_phone_number_pattern():
        """Generate a regular expression pattern that matches phone numbers."""
        return r'\b\d{3}-\d{3}-\d{4}\b'

    @staticmethod
    def generate_split_sentences_pattern():
        """Generate a regular expression pattern that matches sentence boundaries."""
        return r'[.!?][\s]+(?=[A-Z])'

    @staticmethod
    def split_sentences(text):
        """Split the text into a list of sentences."""
        return re.split(RegexUtils.generate_split_sentences_pattern(), text)

    @staticmethod
    def validate_phone_number(phone_number):
        """Verify if the phone number is valid."""
        return RegexUtils.match(RegexUtils.generate_phone_number_pattern(), phone_number)

    @staticmethod
    def extract_email(text):
        """Extract all email addresses from the text."""
        return RegexUtils.findall(RegexUtils.generate_email_pattern(), text)