class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        left_r=0
        right_r=len(matrix)-1
        
        for col in range(len(matrix[0])):
            
            left_r=0
            right_r=len(matrix)-1
            
            while left_r<right_r:
                
                matrix[left_r][col],matrix[right_r][col]=matrix[right_r][col],matrix[left_r][col]
                left_r+=1
                right_r-=1
                
        diagonal=0
        for row in range(len(matrix)):
            
            for col in range(diagonal,len(matrix[0])):
                
                matrix[row][col],matrix[col][row]=matrix[col][row],matrix[row][col]
                
            diagonal+=1