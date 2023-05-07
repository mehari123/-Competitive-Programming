
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        subsequences = []
        
        for num in nums:
            if not subsequences or subsequences[0][0] == num:
                heapq.heappush(subsequences, [num, 1])
            else:
                while subsequences and subsequences[0][0] + 1 < num:
                    if subsequences[0][1] < 3:
                        return False
                    heapq.heappop(subsequences)
                if subsequences and subsequences[0][0] + 1 == num:
                    sub = heapq.heappop(subsequences)
                    heapq.heappush(subsequences, [num, sub[1] + 1])
                else:
                    heapq.heappush(subsequences, [num, 1])
        
        while subsequences:
            if subsequences[0][1] < 3:
                return False
            heapq.heappop(subsequences)
        
        return True
