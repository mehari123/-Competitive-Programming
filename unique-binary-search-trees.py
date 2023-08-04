class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
    
        catalan = [0] * (n + 1)
        catalan[0] = catalan[1] = 1
        print(catalan)
        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]
        
        print (catalan)
        return catalan[n]