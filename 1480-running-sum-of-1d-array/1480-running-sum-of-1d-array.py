class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        for index in range(len(nums)-1):
            
            nums[index+1]=nums[index]+nums[index+1]
            
        return nums