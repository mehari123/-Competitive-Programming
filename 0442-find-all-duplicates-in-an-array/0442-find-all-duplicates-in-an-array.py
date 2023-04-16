class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        i = 0
        
        while i < len(nums):
            
            c=nums[i]-1
            
            if nums[i] != nums[c]:
                
                nums[i],nums[c] = nums[c],nums[i]
            else:
                
                i += 1
                
        ans = []
        
        for index, num in enumerate(nums):
            
            if (index + 1) != num:
                
                ans.append(num)
                
        return ans
            
            
                
                
                