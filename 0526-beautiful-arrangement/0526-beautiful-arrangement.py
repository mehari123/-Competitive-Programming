class Solution:
    def countArrangement(self, n: int) -> int:
       
        def backtrack(pickindex=1,visited = 0):
            
            if visited == 2 ** n - 1:
                
                return 1
            num_beauty = 0
            for i in range(1,n+1):
                
                if (1 << (i-1)) & visited:
                    continue
                
                if any([pickindex % i == 0,i % pickindex == 0]):
                    
                    num_beauty += backtrack(pickindex + 1, visited | 1 << (i-1))
            
            return num_beauty
        
        return backtrack()
                        
                        
                    
                        
                    
                    
            
                        
                    
                    
                    
            
            
        