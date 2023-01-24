class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        index=0
        
        while index<len(nums)-1:
            
            if nums[index]==nums[index+1]:
                nums.remove(nums[index])
                index-=1
                
                
            index+=1
                
        