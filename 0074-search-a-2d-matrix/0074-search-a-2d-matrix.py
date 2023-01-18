class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_pointer=0
        row2_pointer=len(matrix)-1
        col=len(matrix[0])-1
        
        while row_pointer<=row2_pointer:
            
            if matrix[row_pointer][col]>=target:
                
                for index in range(col,-1,-1):
                    
                    if matrix[row_pointer][index]==target:
                        
                        return True
                return False
            
                    
            if matrix[row2_pointer][0]<=target:
                
                for index in range(col,-1,-1):
                    
                    if matrix[row2_pointer][index]==target:
                        
                        return True
                return False
            row_pointer+=1
            row2_pointer-=1
            
        return False
                    
                
        
        