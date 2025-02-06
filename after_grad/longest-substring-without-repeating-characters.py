class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 1
        max_sub = 0
        sub_str = set()
        if len(s)<1:return 0
        sub_str.add(s[0])

        while r < len(s):

            while s[r] in sub_str:

                max_sub = max(max_sub,r-l)
                sub_str.remove(s[l])
                l += 1
            sub_str.add(s[r])
            r += 1 
        
        max_sub = max(max_sub,r-l)
        return max_sub


        