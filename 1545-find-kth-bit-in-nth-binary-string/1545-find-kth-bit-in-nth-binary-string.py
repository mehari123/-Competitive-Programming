class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def KthBit(s,n):
            
            nonlocal k
            if n==0:
                
                return s
            
            s1=s+"1"
            invert=""
            for st in s:
                
                if st=="1":
                    
                    invert+="0"
                    
                else:
                    invert+="1"
                    
            Rinvert=invert[::-1]
            
            s=s1+Rinvert
            
            return KthBit(s,n-1)
            
        s=KthBit("0",n)
        # print(s)
        return s[k-1]
        