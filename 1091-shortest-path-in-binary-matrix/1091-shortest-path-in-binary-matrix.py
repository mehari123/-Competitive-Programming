from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        visited = set()
        visited.add((0, 0))
        queue = deque([(0, 0, 1)])
        
        while queue:
            x, y, steps = queue.popleft()
            
            if x == n-1 and y == n-1:
                return steps
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps+1))
        
        return -1 