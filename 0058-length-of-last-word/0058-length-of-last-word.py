class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        str1 = s.strip(" ").split(" ")
        return len(str1[-1])