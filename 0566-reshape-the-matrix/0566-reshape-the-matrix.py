class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        reshaped_mat=[[[] for col in range(c)] for row in range(r)]
        row_m=col_m=0
        
        if len(mat)*len(mat[0])==r*c:
            
            for row in range (len(mat)):
                
                for col in range(len(mat[0])):
                    reshaped_mat[row_m][col_m]=mat[row][col]
                    col_m+=1
                    if col_m==c:
                        row_m+=1
                        col_m=0
            return reshaped_mat
                        
                        
        else:
            return mat
        
       
        