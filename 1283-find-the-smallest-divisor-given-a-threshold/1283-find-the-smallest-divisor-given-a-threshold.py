class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        high = max(nums)
        low = 1
        ans = high
        
        while low < high:
            
            mid = (low + high) //2
            sums = sum([math.ceil(num / mid) for num in nums])
            
            if sums > threshold:
                
                low = mid + 1
                
            else:
                
                high = mid
                ans = min(ans,high)
                
        return ans
            
        