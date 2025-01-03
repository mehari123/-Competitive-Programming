class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        sum_p = sum(nums)
        prefix = 0
        ans = 0

        for i in range(len(nums)-1):

            prefix += nums[i]
            sum_p -= nums[i]
            # print(i,prefix,sum_p,nums[i])

            if prefix >= sum_p:
                ans += 1
        
        return ans


        