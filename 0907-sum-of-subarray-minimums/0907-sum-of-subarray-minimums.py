class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = [-1]
        left = 0
        right = 0
        mid = 0
        res = 0
        arr += [0] 
        for i in range(len(arr)):
            
            while stack and arr[stack[-1]] > arr[i]:
                
                
                mid = stack.pop()
                right = i
                left = stack[-1]
                
                res += arr[mid] * (right - mid ) * (mid - left)
                
            
            stack.append(i)
            
        return res % (10**9 + 7)
                