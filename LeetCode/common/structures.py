class TrieNode:
    def __init__(self, char = ""):
        self.char = char
        self.children = {}
        self.is_end = False 
        self.counter = 0


class Trie:
    def __init__(self):
       self.root = TrieNode() 

    def insert(self, word: str) -> None:
        # Inserts a word into the trie
        node = self.root 
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        node.counter += 1

    def search(self, word: str) -> bool:
        # Searches if the word is in the trie
        node = self.root 
        for char in word:
            if char not in node.children:
                return False 
            node = node.children[char]
        
        # Reached end of word. Is the word present?
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        # Checks if there is a word in the trie with the prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False 
            node = node.children[char]
        return True        

