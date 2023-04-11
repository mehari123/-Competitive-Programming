class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        self.totalP =  0 
        visited = set()
        
        def province(city,index):
            
            visited.add(index)
            
            for i,c  in enumerate(city):
                
         
                if c == 1 and (i not in visited):
                    
                 
                    province(isConnected[i],i)
                    
            return 1
            
        for i in range(len(isConnected)):
            
            if i not in visited:
                province(isConnected[i],i)
                self.totalP +=1
                
            
        return self.totalP
        