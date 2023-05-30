class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        d = defaultdict(int)
        def getnum(n):
            if n == 0 or n == 1:
                return d[n]
            if n not in d:
                if n % 2 == 0:
                    d[n] = getnum(n/2)
                else:
                    x = (n-1)/2
                    d[n] = getnum(x) + getnum((x+1))
            return d[n]
        d[0] = 0
        d[1] = 1
        maxi = 0
        for i in range(n+1):
            num = getnum(i)
            maxi = max(maxi,num)

        return maxi