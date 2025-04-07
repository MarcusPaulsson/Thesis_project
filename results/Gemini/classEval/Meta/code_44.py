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
        codes = soup.find_all(['pre', 'code'])
        for code in codes:
            code.extract()

        text = soup.get_text()
        text = text.replace('\t', '')
        text = '\n'.join(line.strip() for line in text.splitlines())
        text = HtmlUtil.__format_line_feed(text)
        text = text.strip()

        code_blocks = re.findall(r'<pre.*?>(?:<code.*?>)?(.*?)(?:</code>)?</pre>', html_text, re.DOTALL)
        code_blocks += re.findall(r'<code.*?>(.*?)</code>', html_text, re.DOTALL)

        formatted_text = text
        for _ in code_blocks:
            formatted_text = formatted_text + '\n' + self.CODE_MARK

        if len(code_blocks) > 0:
            formatted_text = formatted_text.replace('\n' + self.CODE_MARK, '')
            formatted_text = formatted_text.replace(self.CODE_MARK, '')

            code_blocks_count = len(code_blocks)
            code_mark_str = ('\n' + self.CODE_MARK) * code_blocks_count
            formatted_text = formatted_text + code_mark_str
            formatted_text = formatted_text.replace(code_mark_str, '')

            text_list = formatted_text.split('\n')
            text_list_new = []
            for item in text_list:
                if len(item) > 0:
                    text_list_new.append(item)
            formatted_text = '\n'.join(text_list_new)

            for item in code_blocks:
                formatted_text = formatted_text + '\n' + self.CODE_MARK
            formatted_text = formatted_text.replace('\n' + self.CODE_MARK, '')
            formatted_text = formatted_text.replace(self.CODE_MARK, '')

            code_mark_str = (self.CODE_MARK + '\n') * code_blocks_count
            formatted_text = formatted_text.replace(code_mark_str, self.CODE_MARK)
            formatted_text = formatted_text.replace(code_mark_str, self.CODE_MARK)

            pattern = r'([^\n])(\n)'+ re.escape(self.CODE_MARK)
            formatted_text = re.sub(pattern, r'\1\n' + self.CODE_MARK, formatted_text)
            pattern2 = re.escape(self.CODE_MARK) + r'(\n)([^\n])'
            formatted_text = re.sub(pattern2, self.CODE_MARK + r'\n\2', formatted_text)

            formatted_text = formatted_text.replace(self.CODE_MARK, '\n' + self.CODE_MARK + '\n')
            formatted_text = formatted_text.replace('\n' + self.CODE_MARK + '\n' + '\n', '\n' + self.CODE_MARK + '\n')
            formatted_text = formatted_text.replace('\n' + self.CODE_MARK + '\n' + '\n', '\n' + self.CODE_MARK + '\n')
            formatted_text = formatted_text.replace('\n' + self.CODE_MARK + '\n' + '\n', '\n' + self.CODE_MARK + '\n')
            formatted_text = formatted_text.strip()

        soup = BeautifulSoup(formatted_text, 'html.parser')
        text = soup.get_text()
        text = text.replace('\t', '')
        text = '\n'.join(line.strip() for line in text.splitlines())
        text = HtmlUtil.__format_line_feed(text)
        formatted_text = text.strip()

        formatted_text = formatted_text.replace('[-] ', '[-]')
        formatted_text = formatted_text.replace('<li>', '[-] ')
        
        return formatted_text

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
        code_blocks = re.findall(r'<pre.*?>(?:<code.*?>)?(.*?)(?:</code>)?</pre>', html_text, re.DOTALL)
        code_blocks += re.findall(r'<code.*?>(.*?)</code>', html_text, re.DOTALL)
        code_blocks = [block.strip() for block in code_blocks]
        return code_blocks