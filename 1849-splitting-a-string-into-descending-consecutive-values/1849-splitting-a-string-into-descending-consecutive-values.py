class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(index,substr):
            
            if len(substr) >= 2:
                
                if int(substr[-2]) - int(substr[-1]) != 1:
                    
                    return False 
                
            if len(substr) > 1  and index == len(s):
                
                if int(substr[-2]) - int(substr[-1]) == 1:
                    
                    return True
                
            for i in range(index + 1, len(s) +1):
                
                if  backtrack(i,substr +[s[index:i]]):
                    
                    return True
                
        ans = backtrack(0,[])
        return ans
                
                
            
            
            
        
        
        