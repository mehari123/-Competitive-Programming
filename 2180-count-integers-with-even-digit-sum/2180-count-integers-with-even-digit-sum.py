class Solution:
    def countEven(self, num: int) -> int:
        
        count = 0
        
        for i in range(1,num + 1):
            
            if sum([int(n) for n in str(i)]) % 2 == 0:
                
                count += 1
                
        return count