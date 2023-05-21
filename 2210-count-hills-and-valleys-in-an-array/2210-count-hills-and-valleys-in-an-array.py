class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        left = None
        right = None
        total = 0
        for i in range(1, len(nums)-1):

            if nums[i] == nums[i+1]:
                continue
            for j in range(-i+1,1):

                if nums[-j] < nums[i]:
                    
                    left = 0
                    break
                elif nums[-j] > nums[i]:
                    left = 1
                    break
                else:
                    continue
            for k in range(i+1,len(nums)):

                if nums[k] < nums[i]:
                    right = 0
                    break
                elif nums[k] > nums[i]:
                    right = 1
                    break
                else:
                    continue

            if left == right:
                total += 1

        return total