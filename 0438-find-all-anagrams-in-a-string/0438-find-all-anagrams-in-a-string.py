class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
    
        standard={}
        anagram={}
        standard=Counter(p)
        anagram=Counter(s[:len(p)])
      
        left=0
        right=len(p)
        ans=[]
        
        while right<len(s):
            
            if standard==anagram:
                ans.append(left)
          
         
            if s[right] in anagram:
                
                anagram[s[right]]+=1
            else:
                anagram[s[right]]=1
            
            anagram[s[left]]-=1
            
            if anagram[s[left]]==0:
                
                del anagram[s[left]]
                
            left+=1
            right+=1
           
        if standard==anagram:
                ans.append(left)
        return ans
            
                    
                    
                    
        
        
        
                
                