class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        stack = [(-1, 0)]
        pre_sum, min_sub = 0, float("inf")
        
        for i, val in enumerate(nums):
            
            pre_sum += val
            
            while stack and pre_sum-stack[0][1] >= k:
                
                min_sub = min(min_sub, i-stack[0][0])
                stack.pop(0)
                
            while stack and pre_sum < stack[-1][1]:
                
                stack.pop()
                
            stack.append((i, pre_sum))
            
        return -1 if min_sub == float("inf") else min_sub
        