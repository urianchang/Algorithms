# Python 3.7
# https://www.hackerrank.com/challenges/html-parser-part-2/problem
"""
.handle_comment(data)
Method called when a comment is encountered.

.handle_data(data)
Method called to process arbitrary data (e.g. text nodes).
"""
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

    def handle_comment(self, data):
        line_count = len(data.split('\n'))
        if line_count > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        if data.strip():
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += "\n"

parser = MyHTMLParser()
parser.feed(html)
parser.close()
