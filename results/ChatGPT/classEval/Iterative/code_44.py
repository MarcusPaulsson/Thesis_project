import re
from bs4 import BeautifulSoup

class HtmlUtil:
    """
    A utility class for formatting and extracting code from HTML text.
    It includes methods for cleaning up the text and converting certain elements into specific markers.
    """

    def __init__(self):
        """
        Initialize a series of markers.
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
        Replace consecutive line breaks with a single line break and strip leading/trailing whitespace.
        
        :param text: string with consecutive line breaks
        :return: string, replaced text with single line break
        """
        return re.sub(r'\n+', '\n', text).strip()

    def format_line_html_text(self, html_text):
        """
        Get the HTML text without the code, adding the CODE_MARK where the code is.
        
        :param html_text: string
        :return: formatted string with -CODE- markers
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        
        for code in soup.find_all(['pre', 'code']):
            code.insert_before(self.CODE_MARK)
            code.insert_after(self.CODE_MARK)
            code.unwrap()
        
        formatted_text = soup.get_text(separator='\n')
        return self.__format_line_feed(formatted_text)

    def extract_code_from_html_text(self, html_text):
        """
        Extract codes from the HTML body.
        
        :param html_text: string, HTML text
        :return: list of extracted code snippets
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        codes = [code.get_text(strip=True) for code in soup.find_all(['pre', 'code'])]
        return codes