class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums2 = {}
        
        for i,n in enumerate(nums):
            
            if n in nums2:
                
                return [nums2[n],i]
            nums2[target - n] = i
            
        print(nums)