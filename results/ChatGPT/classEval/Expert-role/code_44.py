import re
import string
from bs4 import BeautifulSoup

class HtmlUtil:
    """
    This is a class as util for html, supporting for formatting and extracting code from HTML text,
    including cleaning up the text and converting certain elements into specific marks.
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
        :return: string, replaced text with single line break
        """
        return re.sub(r'\n+', '\n', text).strip()

    def format_line_html_text(self, html_text):
        """
        Get the HTML text without the code, and add the code tag -CODE- where the code is
        :param html_text: string
        :return: string
        >>> htmlutil = HtmlUtil()
        >>> result = htmlutil.format_line_html_text('<html><body><h1>Title</h1><p>This is a paragraph.</p><pre>print(\'Hello, world!\')</pre><p>Another paragraph.</p><pre><code>for i in range(5):\n    print(i)</code></pre></body></html>')
        >>> print(result)
        Title
        This is a paragraph.
        -CODE-
        Another paragraph.
        -CODE-
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        # Extract text and replace code blocks with the CODE_MARK
        for code_block in soup.find_all(['pre', 'code']):
            code_block.insert_before(self.CODE_MARK)
            code_block.decompose()
        
        # Get the text and format line feeds
        formatted_text = self.__format_line_feed(soup.get_text())
        return formatted_text

    def extract_code_from_html_text(self, html_text):
        """
        Extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        >>> htmlutil = HtmlUtil()
        >>> codes = htmlutil.extract_code_from_html_text('<html><body><h1>Title</h1><p>This is a paragraph.</p><pre>print(\'Hello, world!\')</pre><p>Another paragraph.</p><pre><code>for i in range(5):\n    print(i)</code></pre></body></html>')
        >>> print(codes)
        ["print('Hello, world!')", 'for i in range(5):\n    print(i)']
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        # Extract codes from pre and code tags
        codes = []
        for code_block in soup.find_all(['pre', 'code']):
            codes.append(code_block.get_text())
        
        return codes

# Example Usage
if __name__ == "__main__":
    html_util = HtmlUtil()
    html_text = '<html><body><h1>Title</h1><p>This is a paragraph.</p><pre>print(\'Hello, world!\')</pre><p>Another paragraph.</p><pre><code>for i in range(5):\n    print(i)</code></pre></body></html>'
    
    formatted_text = html_util.format_line_html_text(html_text)
    print(formatted_text)
    
    codes = html_util.extract_code_from_html_text(html_text)
    print(codes)