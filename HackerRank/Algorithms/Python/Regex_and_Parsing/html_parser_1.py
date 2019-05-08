# Python 3.7
# https://www.hackerrank.com/challenges/html-parser-part-1/problem
"""
HTML
Hypertext Markup Language is a standard markup language used for creating
World Wide Web pages.

Parsing
Parsing is the process of syntactic analysis of a string of symbols. It
involves resolving a string into its component parts and describing their
syntactic roles.

HTMLParser
An HTMLParser instance is fed HTML data and calls handler methods when start
tags, end tags, text, comments, and other markup elements are encountered.
"""
from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])


hp = CustomHTMLParser()
for _ in range(int(input())):
    code = input()
    hp.feed(code)
