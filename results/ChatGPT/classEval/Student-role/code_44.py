htmlutil = HtmlUtil()
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

formatted_text = htmlutil.format_line_html_text(html_text)
print(formatted_text)

codes = htmlutil.extract_code_from_html_text(html_text)
print(codes)