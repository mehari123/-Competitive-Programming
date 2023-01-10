class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        row_len=len(grid)
        col_len=len(grid)
        rows={}
        cols={}
        
        for row in range(row_len):
            
            row_val=""
            col_val=""
            
            for col in range(col_len):
                
                row_val+=" ".join(str(grid[row][col]))
                col_val+=" ".join(str(grid[col][row]))
            
            if row_val in rows:
                
                rows[row_val]+=1
                
            else:
                rows[row_val]=1
            
            if col_val in cols:
                
                cols[col_val]+=1
            
            else:
                
                cols[col_val]=1
        
        
        count_pair=0
        for key,val in rows.items():
            
            if key in cols:
                count_pair+=val*cols[key]
                
        return count_pair
                
                
                
                
                
        
        