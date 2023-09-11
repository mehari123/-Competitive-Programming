import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        ans = []
        
        # Ensure k is not greater than the total number of pairs
        k = min(k, len(nums1) * len(nums2))
        
        for i, num1 in enumerate(nums1):
            heapq.heappush(heap, (num1 + nums2[0], i, 0))

        while heap and len(ans) < k:
            s, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return ans