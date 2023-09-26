class WordDictionary:

    def __init__(self):
        
        self.root = dictionay1()

    def addWord(self, word: str) -> None:

        curr = self.root
        for c in word:

            if c not in curr.C:

                curr.C[c] = dictionay1()
            curr = curr.C[c]

        curr.isEnded = True

    def search(self, word: str,curr = None) -> bool:

        if not curr:

            curr = self.root

        for i,d in enumerate(word):

            if d == ".":

                children = curr.C
                result = False
                for ch in curr.C:

                    if result or self.search(word[i+1:],curr.C[ch]):

                        return True
                return False
            elif d in curr.C:

                curr = curr.C[d]

            else:

                return False
        
        
        return curr.isEnded
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class dictionay1:

    def __init__(self):
        
        self.C = {}
        self.isEnded = False