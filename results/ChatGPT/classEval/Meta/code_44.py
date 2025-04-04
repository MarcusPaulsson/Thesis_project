htmlutil = HtmlUtil()
formatted_text = htmlutil.format_line_html_text('''
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
''')
print(formatted_text)

code_snippets = htmlutil.extract_code_from_html_text('''
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
''')
print(code_snippets)