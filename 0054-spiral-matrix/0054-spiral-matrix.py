class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        r_size=len(matrix)
        rows=len(matrix)-1
        c_size=len(matrix[0])
        cols=len(matrix[0])-1
        spiral=[]
        index=0
        appended=0
        while rows>=0 and cols>=0:  
            row=index
            col=index
            while row >=index and col>=index:
                
                if appended==r_size*c_size:
                    break
                elif col<(cols+index) and row==index:    
                        spiral.append(matrix[row][col])
                        col+=1
                        appended+=1
                elif col==(cols+index) and row<(rows+index):   
                        spiral.append(matrix[row][col])
                        row+=1 
                        appended+=1
                elif row==(rows+index) and col>index:   
                        spiral.append(matrix[row][col])
                        col-=1
                        appended+=1
                elif col==index and row>=index:      
                    # print(matrix[row][col])
                    spiral.append(matrix[row][col])
                    row-=1
                    appended+=1
                    if row==index:
                        break
                        
            cols-=2
            rows-=2 
            index+=1
        return spiral         
        
        
        
        