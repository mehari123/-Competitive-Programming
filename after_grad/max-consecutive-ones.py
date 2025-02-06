class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        le = 0
        ri = 0
        max_con = 0

        while ri < len(nums):

            if nums[ri] == 0:

                max_con = max( max_con,ri-le)
                le = ri + 1

            ri += 1 
        
        max_con = max( max_con,ri-le)
        return max_con
        