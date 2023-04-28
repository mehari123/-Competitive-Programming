class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        
        ilands = set()
        visited = set()
        
        def collect_iland(i,j):

            if grid2[i][j] == 0:

                return 

            visited.add(tuple([i,j]))
            one_iland.add(tuple([i,j]))
            directions = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]

            for di in directions:
                
                if tuple(di) not in visited and 0 <= di[0] < len(grid2) and 0 <= di[1] < len(grid2[0]) and grid2[di[0]][di[1]] != 0:
                        
                        collect_iland(di[0],di[1])
                        
                visited.add(tuple([di[0],di[1]]))
                
                
        
        for i in range(len(grid2)):
            
            for j in range(len(grid2[0])):
                
                if tuple([i,j]) not in visited and grid2[i][j] != 0:
                    
                    one_iland = set()
                    collect_iland(i,j)
                    ilands.add(tuple(one_iland))
                    
                visited.add(tuple([i,j]))
        
        sub_iland = True
        count1 = 0
        
        for iland in ilands:
            
            for i in iland:
                
                if grid1[i[0]][i[1]] == 0 :
                    
                    sub_iland = False
                    break
                    
            if sub_iland:
                
                count1 += 1
                
            sub_iland = True
         
        return count1
                
            
                    
      
                
               
                    
                    
                    
                    
                    
                    
        