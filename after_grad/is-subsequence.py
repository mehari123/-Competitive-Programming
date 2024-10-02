class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        len_sub = len(s)
        len_str = len(t)
        def dp(i,j):

            if len_sub == j:

                return True

            if  (i == len_str-1 and s[j] != t[i]) or i == len_str :

                return False

            if s[j] == t[i]:

                return dp(i+1,j+1)

            else:

                return dp(i+1,j)
        
        return dp(0,0)
        