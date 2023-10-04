class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        output,mask = 0,0
        for i in range(32,-1,-1):
            mask = mask | 1 << i
            found = set([i & mask for i in nums])
            temp = output | 1 << i
            for i in found:
                if i ^ temp in found:
                    output = temp
        return output