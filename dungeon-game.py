from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        memo = {}  # Memoization dictionary

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: Knight reaches the princess
            if i == m - 1 and j == n - 1:
                memo[(i, j)] = max(1, 1 - dungeon[i][j])
                return memo[(i, j)]

            # Calculate minimum health required to reach the princess
            min_health_on_exit = float('inf')
            if i + 1 < m:
                min_health_on_exit = min(min_health_on_exit, dp(i + 1, j))
            if j + 1 < n:
                min_health_on_exit = min(min_health_on_exit, dp(i, j + 1))
            
            memo[(i, j)] = max(min_health_on_exit - dungeon[i][j], 1)
            return memo[(i, j)]

        return dp(0, 0)