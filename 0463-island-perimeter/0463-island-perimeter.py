class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        
        def dfs(i,j):
            
            direction = ([i-1,j],[i+1,j],[i,j-1],[i,j+1])
            peri = 0
            for di in direction:
                
                if di[0] < 0 or di[1] < 0 or di[0] >= len(grid) or di[1] >= len(grid[0]) or grid[di[0]][di[1]] == 0:
                    
                    peri += 1
                    
                    
            return peri
        
        perimeter = 0
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    
                    perimeter += dfs(i,j)
                    
        return perimeter
                    
                    
                    
                
                    
                    
        