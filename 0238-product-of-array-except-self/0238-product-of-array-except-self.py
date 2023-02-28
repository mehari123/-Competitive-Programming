class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix=[1]
        suffix=[1]
        
        for num in nums:
            
            prefix.append(prefix[-1]*num)
            
        # prefix=prefix[1:]
            
        for index in range(len(nums)-1,-1,-1):
            
            suffix.append(suffix[-1]*nums[index])
         
        suffix=list(reversed(suffix))
        print(suffix,prefix)
        
        ans=[0]*len(nums)
        print(len(suffix),len(prefix),len(nums))
        index=0
        while index<len(nums):
            
            ans[index]=prefix[index]*suffix[index+1]  
            
            index+=1
            
        return ans
            
            
        