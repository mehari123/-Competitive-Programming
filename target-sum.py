class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}
        def dp(index,sum1):

            if index == len(nums):

                if sum1 == target:

                    return 1

                else:

                    return 0
    
            if (sum1,index) not in memo:

                 memo[(sum1,index)] = dp(index + 1,sum1 - nums[index]) + dp(index + 1,sum1 +nums[index])


            else:

                return memo[(sum1,index)]
     
            return memo[(sum1,index)] 
            
        return dp(0,0)