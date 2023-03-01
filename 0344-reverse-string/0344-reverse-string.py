class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reveerse(self,s,left,right) :
            
            
            if left<right:
                s[left],s[right]=s[right],s[left]
                reveerse(self,s,left+1,right-1)
            else:
                
                return s
                
        reveerse(self,s,0,len(s)-1)