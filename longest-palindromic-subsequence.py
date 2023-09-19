class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}  # Use a regular dictionary instead of defaultdict
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i > j:
                return 0
            elif i == j:
                return 1
            max_p = 0
            if s[i] == s[j]:
                max_p = dp(i + 1, j - 1) + 2
            else:
                max_p = max(dp(i, j - 1), dp(i + 1, j))
            memo[(i, j)] = max_p  # Fix the typo here (use = instead of ==)
            return max_p
        return dp(0, len(s) - 1)