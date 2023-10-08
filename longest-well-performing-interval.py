class Solution:
   def longestWPI(self,hours):
    prefix_sum = [0]
    for hour in hours:
        if hour > 8:
            prefix_sum.append(prefix_sum[-1] + 1)
        else:
            prefix_sum.append(prefix_sum[-1] - 1)
    
    stack = []
    for i in range(len(prefix_sum)):
        if not stack or prefix_sum[i] < prefix_sum[stack[-1]]:
            stack.append(i)
    
    max_length = 0
    for i in range(len(prefix_sum) - 1, -1, -1):
        while stack and prefix_sum[i] > prefix_sum[stack[-1]]:
            max_length = max(max_length, i - stack.pop())
    
    return max_length