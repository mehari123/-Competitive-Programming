class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        next_g = []
        size = 2*(len(nums))
        ans = [-1]* len(nums) 
        
        for index in range(size):
            
            i = index % len(nums)
            
            while next_g and next_g[-1][1] < nums[i]:
                
                print(next_g[-1][1])
                ans [next_g[-1][0]] = nums[i]
                next_g.pop()
                
            next_g.append([i,nums[i]])
        
        return ans
            
            