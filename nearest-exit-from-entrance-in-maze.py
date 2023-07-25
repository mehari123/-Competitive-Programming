class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = [(entrance[0], entrance[1], 0)]
        visited = {(entrance[0], entrance[1])}

        while queue:
            i, j, steps = queue.pop(0)

            if (i, j) != (entrance[0], entrance[1]) and (i in (0, m - 1) or j in (0, n - 1)):
                return steps

            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_i, new_j = i + x, j + y

                if 0 <= new_i < m and 0 <= new_j < n and maze[new_i][new_j] == '.' and (new_i, new_j) not in visited:
                    queue.append((new_i, new_j, steps + 1))
                    visited.add((new_i, new_j))

        return -1