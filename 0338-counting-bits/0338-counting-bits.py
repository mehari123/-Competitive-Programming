class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = []
        for i in range(n + 1):
            sums = [0]
            count = 0
            j = i 
            
            while count < j:
                
                mod = j % 2
                j = j // 2
                sums.append(mod)
                
            ans.append(sum(sums))
            
        return ans
            
           