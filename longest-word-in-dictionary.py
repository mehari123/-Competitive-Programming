class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        head = TrieNode()
        for word in words:
            temp = head
            for c in word:
                ind = ord(c) - ord('a')
                if not temp.children[ind]:
                    temp.children[ind] = TrieNode()
                temp = temp.children[ind]
            temp.end = True
        result = ""
        def dfs(node,word):
            nonlocal result
            if node.end and len(word) > len(result):
                result = word
            for i in range(26):
                if node.children[i] and node.children[i].end:
                    dfs(node.children[i],word + chr(i + ord('a')))
        dfs(head,"")
        return result