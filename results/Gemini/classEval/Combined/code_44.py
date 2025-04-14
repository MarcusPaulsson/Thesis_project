import re
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
        text = ''
        for element in soup.recursiveChildGenerator():
            if isinstance(element, str):
                stripped_text = element.strip()
                if stripped_text:  # Avoid adding empty lines
                    text += stripped_text + '\n'
            elif element.name == 'pre':
                text += self.CODE_MARK + '\n'
            elif element.name == 'ul':
                for item in element.find_all('li'):
                    text += '[-]'+ item.text + '.' + '\n'
            elif element.name == 'div':
                stripped_text = element.text.strip()
                if stripped_text:
                    text += stripped_text + '\n'
            elif element.name == 'code':
                stripped_text = element.text.strip()
                if stripped_text:
                    text += stripped_text + '\n'

        return HtmlUtil.__format_line_feed(text).strip()

    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        code_list = []
        for pre in soup.find_all('pre'):
            code = pre.find('code')
            if code:
                code_list.append(code.text)
            else:
                code_list.append(pre.text)
        return code_list