class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        box_r=3
        box={}
        row_start=0
    
        while box_r<=9:
            col_start=0
            box_c=3
        
            while box_c<=9:
                box={}
                for row in range(row_start,box_r):
            
                    for col in range(col_start,box_c):
                        
                        if board[row][col]!='.':
                            if board[row][col] in box:
                    
                                return False
                            else:
                                box[board[row][col]]=1
                col_start=box_c
                box_c+=3
            row_start=box_r
            box_r+=3
            
        for row in range(9):
                
                row_b={}
                for col in range(9):
                    
                     if board[row][col]!='.':
                            if board[row][col] in row_b:
                    
                                return False
                            else:
                                row_b[board[row][col]]=1
            
        for col in range(9):
                
                col_b={}
                for row in range(9):
                    
                     if board[row][col]!='.':
                            
                            if board[row][col] in col_b:
                    
                                return False
                            else:
                                col_b[board[row][col]]=1
                    
                    
        return True
                
                    
                    
        
        
        
        
        
        