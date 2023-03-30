class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums2 = [i for i in range(len(nums)+1)]
        num1= 0
        
        for n in nums2:num1 ^= n
            
        for j in nums: num1 ^= j
        
        return num1