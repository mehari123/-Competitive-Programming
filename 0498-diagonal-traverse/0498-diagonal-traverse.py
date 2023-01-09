class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals={}
        
        row_=len(mat)
        col_=len(mat[0])
        
        for row in range(row_):
            
            for col in range(col_):
                
                if row+col in diagonals:
                    diagonals[row+col].append(mat[row][col])
                else:
                    
                     diagonals[row+col]=[mat[row][col]]
        
        diagonal=[]
        
        for key,diago in diagonals.items():
            dgnl=[]
            if key%2==0:
                diago.reverse()
         
            for d in diago:
                diagonal.append(d)
            
        return diagonal
                
        