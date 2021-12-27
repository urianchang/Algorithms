# To run: python -m unittest structures_test.py
from unittest import TestCase

from structures import Trie


class TrieTest(TestCase):
    def test_search(self):
        T = Trie()
        T.insert("hello")

        assert T.search("hell") == False
        assert T.search("world") == False 
        assert T.search("hello") == True         

    def test_startsWith(self):
        T = Trie()
        T.insert("hello")

        assert T.startsWith("hell") == True
        assert T.startsWith("boo") == False
        assert T.startsWith("hello") == True
