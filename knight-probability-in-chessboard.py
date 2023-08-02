class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def inbound(i, j):
            return 0 <= i < n and 0 <= j < n

        memo = {}  # Memoization dictionary to store computed probabilities
        
        def dfs(p, i, j, move):
            nonlocal k

            if move == k:
                return p

            if (i, j, move) in memo:
                return memo[(i, j, move)]

            di = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
            total_prob = 0

            for d in di:
                new_i, new_j = i + d[0], j + d[1]
                if inbound(new_i, new_j):
                    total_prob += dfs(p * 0.125, new_i, new_j, move + 1)

            memo[(i, j, move)] = total_prob  # Memoize the computed probability
            return total_prob

        return dfs(1, row, column, 0)