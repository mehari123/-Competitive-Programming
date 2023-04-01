class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        
        diff = x ^ y 
        count = 0
        
        while diff > 0 :
            
            mod = diff % 2
            diff = diff // 2
            
            if mod == 1 :
                
                count +=1
                  
        return count
    
        