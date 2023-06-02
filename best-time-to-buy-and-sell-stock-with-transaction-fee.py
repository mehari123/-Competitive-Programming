class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        value = 0
        max_ = float("-inf")
        memo = defaultdict(set)
        def dp(index,trans):

            if index >= len(prices):
                return 0

            if (index,trans) in memo :

                return memo[(index,trans)]

            currency = 0
            if trans:

                buy = dp(index + 1, False) - prices[index]
                not_buy = dp(index + 1,True)
                
                currency = max(buy,not_buy)
             

            else:

                sell = prices[index] + dp(index + 1, True) -fee
                not_sell = dp(index + 1 , False)
                currency = max(sell,not_sell)

            memo[(index,trans)] = currency
            return currency


        

        return dp(0,True)