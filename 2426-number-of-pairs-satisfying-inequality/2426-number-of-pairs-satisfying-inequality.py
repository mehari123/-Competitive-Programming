from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        L = SortedList()
        res = 0
        
        for num1,num2 in zip(nums1,nums2):
            
            res += L.bisect_right(num1 - num2 + diff)
            
            L.add(num1 - num2)
            
        return res