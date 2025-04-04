import re
from bs4 import BeautifulSoup

class HtmlUtil:
    """
    A utility class for formatting and extracting code from HTML text,
    including cleaning up text and converting certain elements into specific marks.
    """

    def __init__(self):
        """
        Initialize a series of labels for different types of content.
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
    def _format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break.
        
        :param text: string with consecutive line breaks.
        :return: string with replaced line breaks.
        """
        return re.sub(r'\n+', '\n', text).strip()

    def format_line_html_text(self, html_text):
        """
        Extracts text from HTML, removing code sections and adding a marker for code.
        
        :param html_text: string containing HTML.
        :return: cleaned text with -CODE- markers for code sections.
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        
        # Extract text and code and replace code sections with -CODE- markers
        text_parts = []
        code_parts = []
        
        for element in soup.body.find_all(True):  # find all tags
            if element.name in ['pre', 'code']:
                code_parts.append(element.get_text())
            else:
                text_parts.append(element.get_text())
        
        cleaned_text = self._format_line_feed('\n'.join(text_parts))
        code_marked_text = '\n'.join([cleaned_text] + [self.CODE_MARK for _ in code_parts])
        
        return code_marked_text

    def extract_code_from_html_text(self, html_text):
        """
        Extracts code from the HTML body.
        
        :param html_text: string containing HTML.
        :return: list of code snippets found in the HTML.
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        code_snippets = []

        # Extract code from <pre> and <code> tags
        for element in soup.find_all(['pre', 'code']):
            code_snippets.append(element.get_text())

        return code_snippets

# Example usage
if __name__ == "__main__":
    html_text = """
    <html>
    <body>
        <h1>Title</h1>
        <p>This is a paragraph.</p>
        <pre>print('Hello, world!')</pre>
        <p>Another paragraph.</p>
        <pre><code>for i in range(5):
            print(i)</code></pre>
    </body>
    </html>
    """

    htmlutil = HtmlUtil()
    formatted_text = htmlutil.format_line_html_text(html_text)
    print(formatted_text)
    
    extracted_code = htmlutil.extract_code_from_html_text(html_text)
    print(extracted_code)