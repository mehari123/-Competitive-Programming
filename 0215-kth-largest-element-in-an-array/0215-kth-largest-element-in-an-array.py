import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        h.heapify(nums)
        ans = []
        
        while nums:
            
            ans.append(h.heappop(nums))
            
        return ans[-k]