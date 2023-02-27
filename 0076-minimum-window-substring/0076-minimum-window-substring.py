class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        str_t=Counter(t)
        
        left=0
        ans=["" for r in range(len(s))]
      
        missing=len(t)
        
        for right in range(len(s)+1):
            
            while missing==0:
                
                
                
                if len(ans)>=(right-left):
                    
                    ans=list(s[left:right])
                
                
                if s[left] in str_t:    
                    str_t[s[left]]+=1
                
                if str_t[s[left]]>0:
                        missing+=1
                    
                left+=1
                
            if right <len(s) and s[right] in str_t:
                
                str_t[s[right]]-=1
                
                if str_t[s[right]]>=0:
     
                    missing-=1
                
                
                    
        return "".join(ans)
                
        