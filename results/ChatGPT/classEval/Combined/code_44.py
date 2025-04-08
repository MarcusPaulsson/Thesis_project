import re
from bs4 import BeautifulSoup

class HtmlUtil:
    """
    A utility class for processing HTML, providing methods for formatting and extracting code 
    from HTML text, including text cleanup and conversion of certain elements into specific markers.
    """

    def __init__(self):
        """
        Initialize a series of labels to be used as markers.
        """
        self.SPACE_MARK = '-SPACE-'
        self.JSON_MARK = '-JSON-'
        self.MARKUP_LANGUAGE_MARK = '-MARKUP_LANGUAGE-'
        self.URL_MARK = '-URL-'
        self.NUMBER_MARK = '-NUMBER-'
        self.TRACE_MARK = '-TRACE-'
        self.COMMAND_MARK = '-COMMAND-'
        self.COMMENT_MARK = '-COMMENT-'
        self.CODE_MARK = '-CODE-'

    @staticmethod
    def __format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break and trim the text.
        :param text: string with consecutive line breaks
        :return: string with consecutive line breaks replaced by a single line break
        """
        return re.sub(r'\n+', '\n', text).strip()

    def format_line_html_text(self, html_text):
        """
        Format HTML text by extracting text content and adding code markers.
        :param html_text: string containing HTML
        :return: formatted string with text and code markers
        """
        soup = BeautifulSoup(html_text, "html.parser")

        # Extract text and code markers
        text_parts = []
        code_parts = []

        for elem in soup.find_all(['h1', 'p', 'div']):
            text = elem.get_text(strip=True)
            if text:
                text_parts.append(text)

        for code_elem in soup.find_all(['pre', 'code']):
            code = code_elem.get_text(strip=True)
            if code:
                code_parts.append(self.CODE_MARK)

        # Join text parts and code markers
        formatted_text = '\n'.join(text_parts)
        if code_parts:
            formatted_text += '\n' + '\n'.join(code_parts)

        return self.__format_line_feed(formatted_text)

    def extract_code_from_html_text(self, html_text):
        """
        Extract code snippets from HTML content.
        :param html_text: string containing HTML
        :return: list of extracted code snippets
        """
        soup = BeautifulSoup(html_text, "html.parser")
        code_parts = []

        for code_elem in soup.find_all(['pre', 'code']):
            code = code_elem.get_text(strip=True)
            if code:
                code_parts.append(code)

        return code_parts