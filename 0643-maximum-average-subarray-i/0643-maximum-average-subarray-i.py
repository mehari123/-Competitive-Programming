class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        
        sum1=sum(nums[:k])
        
        maxsum=sum1
        
        index=0
        index2=k
        
        
        while index2<len(nums):
            
            sum1=sum1+nums[index2]-nums[index]
            maxsum=max(sum1,maxsum)
            index+=1
            index2+=1
        
        return maxsum/k
        
        