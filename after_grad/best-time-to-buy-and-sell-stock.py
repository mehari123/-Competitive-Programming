class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min1 = prices[0]
        answer = 0
        for i in prices[1:]:

            if i-min1 > answer:

                answer = i-min1
            
            min1 = min(i,min1)
        
        return answer




        


        