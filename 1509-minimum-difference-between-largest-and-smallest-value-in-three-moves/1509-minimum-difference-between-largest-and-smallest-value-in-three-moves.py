class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        hash_ = {
            
            0:len(nums)-4,
            1:len(nums)-3,
            2:len(nums)-2,
            3:len(nums)-1
          
        }
        
        if len(nums) <= 3 : return 0
        ans = float("inf")
        
        for key,value in hash_.items():
            
            ans = min(ans,nums[value] - nums[key])
            
        return ans