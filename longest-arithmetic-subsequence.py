from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # Create a dictionary to store the length of arithmetic subsequence
        arr = defaultdict(int)
        n = len(nums)
        max_length = 0

        for i in range(n):
            for j in range(i + 1, n):
                diff = nums[j] - nums[i]
                # Calculate the length of the current arithmetic subsequence
                arr[(j, diff)] = arr[(i, diff)] + 1
                # Update the maximum length found so far
                max_length = max(max_length, arr[(j, diff)])

        return max_length + 1  # Add 1 to include the current element in the subsequence