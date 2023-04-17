class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        num = 0
        sum1  = sum([i for i in range(1,len(nums)+1)])
        sum2 = sum(nums)
        
        for n in nums:
            
            if (num >> (n)) & 1:
                
                return n
            
            num ^= 1 << n

            
        