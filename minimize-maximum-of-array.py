class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        sum1 = 0
        ans = 0

        for i in range(len(nums)):

            sum1 += nums[i]

            ans = max(ans,(sum1 + i ) // (i + 1))

        return ans