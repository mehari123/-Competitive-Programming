class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            if k == 1:
                return 0
            
            else:
                return 1
            
        val = 2 ** (n - 1)
        
        if k <= val:
            return self.kthGrammar(n - 1, k)
        
        else:
            res = self.kthGrammar(n - 1 , k - val)
        
            if res == 0:
                return 1
            
            else:
                return 0 
                        
                    
                
                
        