class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        min_c = float("inf")
        n = len(cost)
        memo = {}
        def dp(n):

            if n >= len(cost):
                return 0

            if n not in memo:
                memo[n] = min(dp(n+1), dp(n+2)) + cost[n]

            return memo[n]

        return min(dp(0) ,dp(1))