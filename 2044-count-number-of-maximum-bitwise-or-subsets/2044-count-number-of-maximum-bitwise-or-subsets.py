class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        
        maxb = 0
        for num in nums:
            
            maxb |= num
        
        count = 0
        
        def orbitwise(sub=0,index=0):
            
            nonlocal count
            
            if sub == maxb:
                
                count += 1
    
            subset = 0
            for i in range(index,len(nums)):
                
                orbitwise(sub | nums[i],i + 1)
                
        
        orbitwise()
        return count