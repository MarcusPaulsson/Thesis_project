import re

class RegexUtils:
    """
    A utility class for performing various operations using regular expressions, including matching, finding,
    splitting, and substituting text. It includes predefined patterns for validating phone numbers and extracting
    email addresses.
    """

    @staticmethod
    def match(pattern, text):
        """
        Check if the text fully matches the regular expression pattern.
        
        :param pattern: str, Regular expression pattern
        :param text: str, Text to match
        :return: bool, True if the text fully matches the pattern, otherwise False
        """
        return bool(re.fullmatch(pattern, text))

    @staticmethod
    def findall(pattern, text):
        """
        Find all occurrences of the pattern in the text and return them as a list.
        
        :param pattern: str, Regular expression pattern
        :param text: str, Text to search
        :return: list of str, List of all matching substrings
        """
        return re.findall(pattern, text)

    @staticmethod
    def split(pattern, text):
        """
        Split the text by the occurrences of the pattern.
        
        :param pattern: str, Regular expression pattern
        :param text: str, Text to split
        :return: list of str, List of substrings after splitting
        """
        return re.split(pattern, text)

    @staticmethod
    def sub(pattern, replacement, text):
        """
        Replace occurrences of the pattern in the text with the specified replacement.
        
        :param pattern: str, Regular expression pattern
        :param replacement: str, Text to replace with
        :param text: str, Text to be modified
        :return: str, Text after replacement
        """
        return re.sub(pattern, replacement, text)

    @staticmethod
    def generate_email_pattern():
        """
        Generate a regex pattern for matching email addresses.
        
        :return: str, Regex pattern for email addresses
        """
        return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    @staticmethod
    def generate_phone_number_pattern():
        """
        Generate a regex pattern for matching phone numbers in the format xxx-xxx-xxxx.
        
        :return: str, Regex pattern for phone numbers
        """
        return r'\b\d{3}-\d{3}-\d{4}\b'

    @staticmethod
    def generate_split_sentences_pattern():
        """
        Generate a regex pattern for splitting sentences based on punctuation.
        
        :return: str, Regex pattern for splitting sentences
        """
        return r'[.!?][\s]+(?=[A-Z])'

    @staticmethod
    def split_sentences(text):
        """
        Split the text into a list of sentences.
        
        :param text: str, Text to be split into sentences
        :return: List of str, Sentences from the text
        """
        sentences = re.split(RegexUtils.generate_split_sentences_pattern(), text)
        return [s.strip() for s in sentences if s.strip()]

    @staticmethod
    def validate_phone_number(phone_number):
        """
        Validate if the provided phone number matches the expected format.
        
        :param phone_number: str, Phone number to validate
        :return: bool, True if the phone number is valid, otherwise False
        """
        pattern = RegexUtils.generate_phone_number_pattern()
        return RegexUtils.match(pattern, phone_number)

    @staticmethod
    def extract_email(text):
        """
        Extract all email addresses from the provided text.
        
        :param text: str, Input text to extract emails from
        :return: list of str, List of extracted email addresses
        """
        pattern = RegexUtils.generate_email_pattern()
        return RegexUtils.findall(pattern, text)