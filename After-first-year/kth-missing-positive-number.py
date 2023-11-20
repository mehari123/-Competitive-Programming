class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:


        missed = 0
        index = 0
        for a in arr:
            new1 = k - missed
            missed += a - index-1
            if k <= missed:
                return index + new1
            index = a

        new1 = k - missed
        return index + new1