class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        alter = str(bin(n))
        
        alter = alter[2:]
        continues = 0 
        prev = 3
        
        for con in alter:
                
            if con == "0":
                
                if prev == 0:
                    
                    continues += 1
                else:
                    
                    continues = 1
                prev = 0
                    
            elif con == "1":
                
                if prev == 1:
                    
                    continues += 1
                else:
                    continues = 1
                    
                prev =1
            if continues >= 2:
                return False
                
        return True