from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count = 0
        prev = float('-inf')  # Initialize prev to negative infinity
        
        for i in range(len(nums)):
            if nums[i] <= prev:  # If the current number is not greater than the previous one
                count += 1
                if count > 1:  # If we've made more than one change, return False
                    return False
                
                # Check if we can remove the current or previous element
                if i == 1 or nums[i] > nums[i - 2]:
                    prev = nums[i]  # Remove the current element
                else:
                    prev = nums[i - 1]  # Remove the previous element
            else:
                prev = nums[i]  # Keep the current element as the new previous
        
        return True
