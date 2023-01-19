class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        new_grid=[]
        
        for index1 in range(len(grid)):
            
            if index1+2<len(grid):
                new_grid.append([])
            
            else:
                break
            for index2 in range(len(grid[0])):
                
                    if index1+2<len(grid) and index2+2<len(grid[0]):
                    
                        row=index1+3
                        col=index2+3
            
                        max_num=0
                    
                        for i in range(index1,row):
                        
                            for j in range(index2,col):
                            
                                if max_num<grid[i][j]:
                                
                                    max_num=grid[i][j]
                       
                        new_grid[index1].append(max_num)
                    else:
                        break
                    
        return new_grid
        