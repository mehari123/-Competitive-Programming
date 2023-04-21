class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        pointer1=0 
        pointer2 = len(needle)
        
        while pointer2 <= len(haystack):
            
            if haystack[pointer1:pointer2] == needle:
                
                return pointer1
            
            pointer2 +=1 
            pointer1 +=1 
            
            
        return -1
        