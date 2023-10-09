class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {}
        if len(stones) == 1:

            return stones[0]
        for i in stones:

            temp = dp.copy()

            for j in dp:

                temp[j + i] = 0

            temp[i] = 0
            dp.update(temp)

        half = sum(stones)//2
        for i in range(100):

            if (half-i) in dp:

                return sum(stones) - 2*(half-i)