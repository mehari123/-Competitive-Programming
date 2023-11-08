class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        decrease = False
        if nums[0] >= nums[-1]:

            decrease = True
        
        for i in range(1,len(nums)):

            if decrease:

                if nums[i-1] < nums[i]:

                    return False
            else:

                if nums[i-1] > nums[i]:

                    return False
        return True
        
        