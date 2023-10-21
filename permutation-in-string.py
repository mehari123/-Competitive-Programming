class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        str2=defaultdict(lambda:0)
        str2=Counter(s2[:len(s1)])
        standard=Counter(s1)
        left=0
        right=len(s1)
        
        for  right in range(right,len(s2)):
           
            if standard==str2:
                
                return True
                
            str2[s2[right]]+=1
            str2[s2[left]]-=1
            
            if str2[s2[left]]==0:
                
                del str2[s2[left]]
            
            left+=1
          
        if standard==str2:
               
                return True
            
        else:
            return False