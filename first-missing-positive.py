class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        i = 1
        while i in num_set:
            print(i)
            i += 1
        return i