class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums.sort()
        
        nums = Counter(nums)
        nums = sorted(nums.items(),key = lambda item : item[1])
        ans = []
        for i in range(len(nums)-1, -1 ,-1):
            
            ans.append(nums[i][0])
            
            if len(nums)-i == k:
                return ans
      
        
        
        