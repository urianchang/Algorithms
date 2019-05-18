# Python 3.7
# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attribute in attrs:
            print(f"-> {attribute[0]} > {attribute[1]}")


hp = CustomHTMLParser()
for _ in range(int(input())):
    html = input()
    hp.feed(html)
