class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:

            return nums[0]
            
        def dp(i,prev,current,m):

            if i == len(nums) -m:

                return current

            temp = max(prev + nums[i],current)
            prev = current
            current = temp
            return dp(i+ 1,prev,current,m)

        max1 = dp(0,0,0,1)
        max2 = dp(-(len(nums)-1),0,0,len(nums))

        return max(max1,max2)