class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        root = TrieNode()
        def insert(word):
            nonlocal root
            current = root
            for w in word:

                if w not in current.child:

                    current.child[w] = TrieNode()

                current.child[w].val += 1
                current = current.child[w]
            


        def searchPre(word1):
            val = 0
            current = root
            for w in word1:

                val += current.child[w].val
                current = current.child[w]
                
            return val 

        for wor in words:

            insert(wor)

        ans = []
        for worr in words:

            ans.append(searchPre(worr))

        print(ans)
        return ans

class TrieNode():

    def __init__(self):

        self.val = 0
        self.child = defaultdict(TrieNode)