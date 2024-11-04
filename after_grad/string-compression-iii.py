class Solution:
    def compressedString(self, word: str) -> str:
        
        p1 = 0
        p2 = 1
        ans = ''

        while p2 < len(word):

            if word[p1] == word[p2]:

                p2 += 1

            else:
                com = p2 - p1
                while com > 9:
                    
                    ans+= str(9) + word[p1]
                    com -= 9

                if p2 > p1:

                    ans+= str(com) + word[p1]

                p1 = p2
                p2 += 1
                
        if p2 > p1:
            com = p2 - p1
            while com > 9:
                
                ans+= str(9) + word[p1]
                com -= 9

            if p2 > p1:

                ans+= str(com) + word[p1]

        return ans