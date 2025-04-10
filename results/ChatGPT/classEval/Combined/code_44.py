import re
from bs4 import BeautifulSoup


class HtmlUtil:
    """
    A utility class for processing HTML, providing methods for formatting text and extracting code snippets.
    """

    def __init__(self):
        """
        Initialize a series of markers for various types of content.
        """
        self.CODE_MARK = '-CODE-'

    @staticmethod
    def _format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break.

        :param text: String potentially containing consecutive line breaks.
        :return: String with consecutive line breaks replaced by a single line break.
        """
        return re.sub(r'\n+', '\n', text).strip()

    def format_line_html_text(self, html_text):
        """
        Extracts formatted text from HTML, replacing code blocks with a specific marker.

        :param html_text: String containing HTML content.
        :return: String formatted with extracted text and code markers.
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        text_parts = []

        # Extract text from relevant HTML tags
        for element in soup.find_all(['h1', 'p', 'div']):
            text = self._format_line_feed(element.get_text(strip=True))
            if text:
                text_parts.append(text)

        # Add CODE_MARK for each <pre> or <code> block
        for code_element in soup.find_all(['pre', 'code']):
            text_parts.append(self.CODE_MARK)

        return '\n'.join(text_parts)

    def extract_code_from_html_text(self, html_text):
        """
        Extracts code snippets from HTML content.

        :param html_text: String containing HTML content.
        :return: List of extracted code snippets.
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        return [code_element.get_text(strip=True) for code_element in soup.find_all(['pre', 'code'])]


# Unit tests will be defined outside this class.