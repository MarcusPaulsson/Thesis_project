import re
from bs4 import BeautifulSoup

class HtmlUtil:
    """
    This is a utility class for HTML, supporting formatting and extracting code from HTML text,
    including cleaning up the text and converting certain elements into specific markers.
    """

    def __init__(self):
        """
        Initialize a series of labels for various types of content.
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
        Replace consecutive line breaks with a single line break.
        :param text: string with consecutive line breaks
        :return: string, text with single line breaks
        """
        return re.sub(r'\n+', '\n', text).strip()

    def format_line_html_text(self, html_text):
        """
        Get the HTML text without the code, and add the code marker -CODE- where the code is.
        :param html_text: string containing HTML
        :return: string with formatted text
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        for code in soup.find_all(['pre', 'code']):
            code.insert_before(self.CODE_MARK)
            code.insert_after(self.CODE_MARK)
            code.unwrap()
        text = soup.get_text(separator='\n')
        return self.__format_line_feed(text)

    def extract_code_from_html_text(self, html_text):
        """
        Extract code from the HTML body.
        :param html_text: string containing HTML
        :return: list of extracted code snippets
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        codes = [code.get_text() for code in soup.find_all(['pre', 'code'])]
        return codes