class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # get the island boundary
        n = len(grid)
        queue = deque()
        directions =  [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            nonlocal n
            return (0 <= row < n and 0 <= col < n)


               
        def dfs(row, col):
             
            grid[row][col] = 2
            queue.append((row,col))
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                    dfs(new_row, new_col)

        for r in range(n):
            if queue:
                break
            
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r,c)
                    break
        distance=0

        while queue:
            for _ in range(len(queue)):
                row,col=queue.popleft()
                for row_change,col_change in directions:
                    new_row=row+row_change
                    new_col=col+col_change
                    if inbound(new_row,new_col):
                        if grid[new_row][new_col]==1:
                            return distance
                        if grid[new_row][new_col]==0:
                            grid[new_row][new_col]=2
                            queue.append((new_row,new_col))
            distance+=1
        return distance