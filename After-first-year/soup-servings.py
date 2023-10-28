from collections import defaultdict

class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0  # If n is large, the probability is very close to 1

        n = (n + 24) // 25  # Scale down n to reduce computation

        memo = defaultdict(float)

        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0

            if (a, b) in memo:
                return memo[(a, b)]

            su = 0

            for p in [[4, 0], [3, 1], [2, 2], [1, 3]]:
                su += 0.25 * dp(max(a - p[0], 0), max(b - p[1], 0))

            memo[(a, b)] = su
            return su

        return dp(n, n)