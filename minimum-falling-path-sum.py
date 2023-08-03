class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        minF = [[0 for i in range(n)] for _ in range(n)]
        minF[n-1] = matrix[n-1]

        for row in range(n-2,-1,-1):

            for col in range(n):
                
                f1 = float("inf") if col-1 < 0  else minF[row+1][col-1]
                f2 = float("inf") if col+1 > n-1 else minF[row+1][col+1]
                f3 = minF[row+1][col]
                minF[row][col] =  matrix[row][col] + min(f1,f2,f3)

        return min(minF[0])