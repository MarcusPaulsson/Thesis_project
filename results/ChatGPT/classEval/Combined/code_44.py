import re
from bs4 import BeautifulSoup

class HtmlUtil:
    """
    A utility class for formatting and extracting code from HTML text,
    including cleaning up the text and converting certain elements into specific markers.
    """

    def __init__(self):
        """
        Initialize a series of labels.
        """
        self.CODE_MARK = '-CODE-'

    @staticmethod
    def _format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break.
        :param text: string with consecutive line breaks
        :return: string, replaced text with single line break
        """
        return re.sub(r'\n+', '\n', text).strip()

    def format_line_html_text(self, html_text):
        """
        Get the HTML text without the code, and add the code tag -CODE- where the code is.
        :param html_text: string
        :return: string
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        text_parts = []

        for element in soup.body.find_all(['h1', 'p', 'pre']):
            if element.name in ['h1', 'p']:
                text_parts.append(element.get_text(strip=True))
            elif element.name == 'pre':
                text_parts.append(self.CODE_MARK)

        return self._format_line_feed('\n'.join(text_parts))

    def extract_code_from_html_text(self, html_text):
        """
        Extract codes from the HTML body.
        :param html_text: string, HTML text
        :return: list of code
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        code_snippets = []

        for code in soup.find_all(['pre', 'code']):
            code_snippets.append(code.get_text(strip=True))

        return code_snippets