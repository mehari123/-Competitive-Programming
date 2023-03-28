import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-num for num in nums]
        h.heapify(nums)
        ans = 0
        
        while nums and k > 0:
            
            ans = h.heappop(nums)
            k -= 1
            
        return - ans