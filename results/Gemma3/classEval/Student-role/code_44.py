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
        if not text:
            return ""
        return re.sub(r'\n+', '\n', text)

    def format_line_html_text(self, html_text):
        """
        get the html text without the code, and add the code tag -CODE- where the code is
        :param html_text:string
        :return:string
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        text = soup.get_text(separator='\n')
        text = self.__format_line_feed(text)
        
        code_blocks = soup.find_all('pre')
        
        formatted_text = ""
        last_index = 0
        
        for block in code_blocks:
            if block.find('code'):
                code_content = block.find('code').get_text()
                formatted_text += text[last_index:text.find(code_content)] + self.CODE_MARK + '\n'
                last_index = text.find(code_content) + len(code_content)
        
        formatted_text += text[last_index:]
        
        return formatted_text.strip()

    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        code_blocks = soup.find_all('pre')
        codes = []
        for block in code_blocks:
            if block.find('code'):
                codes.append(block.find('code').get_text())
            else:
                codes.append(block.get_text())
        return codes