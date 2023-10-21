class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        lastDay = max(days)
        dp = [-1] * (lastDay + 2)
        dp[lastDay + 1] = 0  # no trips after the last day, so the price is 0

        for day in days:
            dp[day] = 0

        for i in range(lastDay, -1, -1):
            if dp[i] == -1:  # no trips that day, take the price of the next day
                dp[i] = dp[i + 1]
            else:
                dp[i] = dp[min(i + 1, lastDay + 1)] + costs[0]  
                # 1-day pass
                dp[i] = min(dp[i], dp[min(i + 7, lastDay + 1)] + costs[1])  
                # 7-day pass
                dp[i] = min(dp[i], dp[min(i + 30, lastDay + 1)] + costs[2])  
                # 30-day pass

        return dp[0]