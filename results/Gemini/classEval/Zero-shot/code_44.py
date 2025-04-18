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
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text(<html>
        >>> <body>
        >>>    <h1>Title</h1>
        >>>    <p>This is a paragraph.</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>Another paragraph.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        Title
        This is a paragraph.
        -CODE-
        Another paragraph.
        -CODE-
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        codes = soup.find_all('pre')
        for code in codes:
            code.extract()
        text = soup.get_text()
        text = '\n'.join(line.strip() for line in text.splitlines())
        text = HtmlUtil.__format_line_feed(text)
        text = text.replace('\n\n', '\n')
        code_marks = [self.CODE_MARK] * len(codes)
        result = ''
        text_parts = text.split('\n')
        code_index = 0
        text_index = 0
        while text_index < len(text_parts) or code_index < len(code_marks):
            if text_index < len(text_parts):
                result += text_parts[text_index] + '\n'
                text_index += 1
            if code_index < len(code_marks):
                result += code_marks[code_index] + '\n'
                code_index += 1
        result = result.strip()
        return result

    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.extract_code_from_html_text(<html>
        >>> <body>
        >>>    <h1>Title</h1>
        >>>    <p>This is a paragraph.</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>Another paragraph.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        ["print('Hello, world!')", 'for i in range(5):\n                print(i)']
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        code_blocks = soup.find_all('code')
        pre_blocks = soup.find_all('pre')
        codes = []
        for pre in pre_blocks:
            code_in_pre = pre.find('code')
            if code_in_pre:
                codes.append(code_in_pre.text)
            else:
                codes.append(pre.text)
        return codes