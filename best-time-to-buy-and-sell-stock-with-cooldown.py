from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        memo = [[-1 for _ in range(3)] for _ in range(n)]
        print(memo[0][0])
        def dp(i, state):
            if i >= n:
                return 0

            if memo[i][state] != -1:
                return memo[i][state]

            if state == 0:  # 0 means buy
                memo[i][state] = max(-prices[i] + dp(i + 1, 1), dp(i + 1, 0))
            elif state == 1:  # 1 means sell
                memo[i][state] = max(prices[i] + dp(i + 2, 0), dp(i + 1, 1))
            else:  # 2 means cooldown
                memo[i][state] = dp(i + 1, 0)

            return memo[i][state]

        a = dp(0, 0)
        print(memo)
        return a