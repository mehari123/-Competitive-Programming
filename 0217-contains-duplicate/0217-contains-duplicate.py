class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        duplicate = {}
        
        for num in nums:
            
            if num in duplicate:
                
                return True
            duplicate[num] = 0
            
        return False
        