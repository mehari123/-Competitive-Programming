class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row=len(matrix)
        col=len(matrix[0])
        zero_row={}
        zero_col={}
        
        for r in range(row):
            
            for c in range(col):
                
                if matrix[r][c]==0:
                    
                    if r in zero_row:
                        pass
                    else:
                        zero_row[r]=1
                    if  c in zero_col:
                        pass
                    else:
                        zero_col[c]=1
                    
        for ro in zero_row:
            
            for c in range(col):
                
                matrix[ro][c]=0
        
        for co in zero_col:
            
            for r in range(row):
                
                matrix[r][co]=0
                
        return zero_col
                
        