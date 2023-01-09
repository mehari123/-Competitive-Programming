class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_=len(grid)
        col_=len(grid[0])
        cols={}
        rows={}
        
        for index in range(row_): 
            row_0=0
            row_1=0
    
            for index2 in range(col_):
                
                if grid[index][index2]==0:   
                    row_0+=1
                
                else:
                    row_1+=1         
            rows[index]=[row_0,row_1]
        
        for index in range(col_):
            col_0=0
            col_1=0
            
            for index2 in range(row_):

                if grid[index2][index]==0: 
                    col_0+=1  

                else:
                    col_1+=1      
            cols[index]=[col_0,col_1]
        

        diff=[]
        
        for row in range(row_):
            
            row1=rows[row]
            diff.append([])
            
            for col in range(col_):
                
                col1=cols[col]
                
                diff[row].append(row1[1]+col1[1]-row1[0]-col1[0])
                
        return diff
                
            
                    
                    
        
        