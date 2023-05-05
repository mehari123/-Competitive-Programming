class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        mat2 = [[0] * c for _ in range(r)]
        que = deque()
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    que.append((i, j))
                else:
                    mat2[i][j] = -1
        
        while que:
            x, y = que.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and mat2[nx][ny] == -1:
                    mat2[nx][ny] = mat2[x][y] + 1
                    que.append((nx, ny))
        
        return mat2