class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index): #None
        root = self.root
        root.index = index
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
            root.index = index
        
    def startsWith(self, word):
        root = self.root
        for symbol in word:
            if symbol not in root.children:
                return -1
            root = root.children[symbol]
        return root.index  


class WordFilter:
    def __init__(self, words):
        self.trie = Trie()
        self.words = {}
        
        for index, word in enumerate(words):
            long = word + "#" + word
            for i in range(len(word)):
                self.trie.insert(long[i:], index)
                
    def f(self, prefix, suffix):
        return self.trie.startsWith(suffix + "#" + prefix)