import re

class RegexUtils:
    """
    Provides utility functions for working with regular expressions, including matching,
    finding all occurrences, splitting, and substituting text.  Also includes methods for
    validating phone numbers and extracting email addresses.
    """

    def match(self, pattern, text):
        """
        Checks if the beginning of the text matches the regular expression.

        Args:
            pattern (str): The regular expression pattern.
            text (str): The text to match against.

        Returns:
            bool: True if the text matches the pattern, False otherwise.
        """
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string.")
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        return bool(re.match(pattern, text))

    def findall(self, pattern, text):
        """
        Finds all non-overlapping matches of the regular expression in the text.

        Args:
            pattern (str): The regular expression pattern.
            text (str): The text to search within.

        Returns:
            list: A list of strings containing all matching substrings.  Returns an empty list if no matches are found.
        """
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string.")
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        return re.findall(pattern, text)

    def split(self, pattern, text):
        """
        Splits the text into a list of substrings based on the occurrences of the regular expression pattern.

        Args:
            pattern (str): The regular expression pattern to split on.
            text (str): The text to split.

        Returns:
            list: A list of strings representing the substrings after splitting.
        """
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string.")
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        return re.split(pattern, text)

    def sub(self, pattern, replacement, text):
        """
        Replaces all occurrences of the regular expression pattern in the text with the given replacement string.

        Args:
            pattern (str): The regular expression pattern to replace.
            replacement (str): The string to replace the matched patterns with.
            text (str): The text to perform the substitution on.

        Returns:
            str: The text after the substitutions have been made.
        """
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string.")
        if not isinstance(replacement, str):
            raise TypeError("Replacement must be a string.")
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        return re.sub(pattern, replacement, text)

    def generate_email_pattern(self):
        """
        Generates a regular expression pattern for matching email addresses.

        Returns:
            str: A regular expression pattern that matches email addresses.
        """
        return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def generate_phone_number_pattern(self):
        """
        Generates a regular expression pattern for matching phone numbers in the format XXX-XXX-XXXX.

        Returns:
            str: A regular expression pattern that matches phone numbers.
        """
        return r'\b\d{3}-\d{3}-\d{4}\b'

    def generate_split_sentences_pattern(self):
        """
        Generates a regular expression pattern for splitting sentences based on sentence-ending punctuation.

        Returns:
            str: A regular expression pattern that matches the whitespace after sentence-ending punctuation.
        """
        return r'[.!?][\s]{1,2}(?=[A-Z])'

    def split_sentences(self, text):
        """
        Splits the text into a list of sentences.

        Args:
            text (str): The text to split into sentences.

        Returns:
            list: A list of strings, where each string is a sentence.
        """
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")

        pattern = self.generate_split_sentences_pattern()
        sentences = re.split(pattern, text)
        return [s.strip() for s in sentences if s.strip()]  # Remove leading/trailing whitespace and empty sentences

    def validate_phone_number(self, phone_number):
        """
        Validates a phone number against the predefined phone number pattern.

        Args:
            phone_number (str): The phone number to validate.

        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        if not isinstance(phone_number, str):
            raise TypeError("Phone number must be a string.")

        pattern = self.generate_phone_number_pattern()
        return bool(re.match(pattern, phone_number))

    def extract_email(self, text):
        """
        Extracts all email addresses from the given text.

        Args:
            text (str): The text to extract email addresses from.

        Returns:
            list: A list of strings, where each string is an email address found in the text.
        """
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")

        pattern = self.generate_email_pattern()
        return re.findall(pattern, text)