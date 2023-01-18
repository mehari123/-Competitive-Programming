class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        row=0
        col=0
        
        for index in range(len(matrix)-1):
            toe_value=matrix[index][0]
            row=index
            col=0
            while row<len(matrix) and col<len(matrix[0]):
                if matrix[row][col]!=toe_value:
                    return False
                row+=1
                col+=1
        row=0
        col_len=len(matrix[0])
        for index in range(col_len):
            toe_value=matrix[0][index]
            col=index
            row=0
            while row<len(matrix) and col<len(matrix[0]):
                if matrix[row][col]!=toe_value:
                    return False
                row+=1
                col+=1
        return True