import re
import string
import gensim
from bs4 import BeautifulSoup

class HtmlUtil:
    """
    This is a class as util for html, supporting for formatting and extracting code from HTML text, including cleaning up the text and converting certain elements into specific marks.
    """

    def __init__(self):
        """
        Initialize a series of labels
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
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return:string, replaced text with single line break
        """
        return re.sub(r'\n+', '\n', text)

    def format_line_html_text(self, html_text):
        """
        get the html text without the code, and add the code tag -CODE- where the code is
        :param html_text:string
        :return:string
        """
        soup = BeautifulSoup(html_text, 'html.parser')

        # Replace code blocks with the CODE_MARK
        code_blocks = soup.find_all(['pre', 'code'])
        for code_block in code_blocks:
            code_block.replace_with(self.CODE_MARK)

        # Handle list items
        list_items = soup.find_all('li')
        for list_item in list_items:
            list_item.replace_with('[-]'+list_item.get_text()+'.')

        # Extract text and clean it up
        text = soup.get_text()
        text = text.replace('\r', '').strip()
        text = '\n'.join(line.strip() for line in text.splitlines())
        text = HtmlUtil.__format_line_feed(text)

        return text

    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        code_blocks = soup.find_all(['pre', 'code'])
        codes = [code_block.get_text() for code_block in code_blocks]
        return codes