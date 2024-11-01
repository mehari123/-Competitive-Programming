class Solution:
    def makeFancyString(self, s: str) -> str:

        n = len(s)
        p1 = 0
        p2 = 1
        p3 = 2
        remove = {}
        if n < 3:
            return s
        
        while p3 < len(s):

            if s[p1] == s[p2] and s[p2] == s[p3]:

                remove[p1] = 0
            p1 += 1
            p2 += 1
            p3 += 1
        ans = ''

        for i in range(n):

            if i not in remove:
                ans += s[i]
        return ans
