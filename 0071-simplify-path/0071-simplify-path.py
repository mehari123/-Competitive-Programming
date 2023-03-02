class Solution:
    
    def simplifyPath(self, path: str) -> str:
        
        ans=[]
        path1=path.split("/")
        
        for p in path1:
            
            if p=="" or p==".":
                
                continue
                
            if p=="..":
                
                if len(ans)>=1:
                    
                    ans.pop()
            else:
                
                ans.append(p)
                
        str1=""
            
        for a in ans:
                
            str1+="/"
            str1+=a[0:]
                
        if str1=="":
                
            str1="/"
                
        return str1
        