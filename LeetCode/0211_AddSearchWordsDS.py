# https://leetcode.com/problems/design-add-and-search-words-data-structure/
class CharacterNode:
    def __init__(self, char = ""):
        self.char = char 
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = CharacterNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                new = CharacterNode(ch)
                node.children[ch] = new
                node = new
        node.is_end = True

    def search(self, word: str) -> bool:
        stack = [(self.root, word)]

        while stack:
            node, w = stack.pop()
            if not w:
                if node.is_end:
                    return True             
            elif w[0] == ".":
                for n in node.children.values():
                    stack.append((n, w[1:])) 
            else:
                if w[0] in node.children:
                    n = node.children[w[0]] 
                    stack.append((n, w[1:]))    
        
        return False


wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")

print(wd.search("pad")) # False
print(wd.search("bad")) # True
print(wd.search(".ad")) # True
print(wd.search("b..")) # True
