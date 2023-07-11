class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if not str1 or not str2:
            return ""

        min_len = min(len(str1), len(str2))

        for i in range(min_len, 0, -1):
            
            if len(str1) % i == 0 and len(str2) % i == 0:
                divisor = str1[:i]
                if str1 == divisor * (len(str1) // i) and str2 == divisor * (len(str2) // i):
                    return divisor

        return ""
        