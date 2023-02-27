class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        shifted=defaultdict(lambda:0)
        
        for shift in shifts:
            
            if shift[2]==0:
                
                shifted[shift[0]]-=1
                shifted[shift[1]+1]+=1
                    
            elif shift[2]==1:
                
                shifted[shift[0]]+=1
                shifted[shift[1]+1]-=1
                
        shifting=[0]
        
        for r in range(len(s)):
            
            shifting.append(shifting[-1]+shifted[r])
            
        new_str=[]
        shifting=shifting[1:]
        
        for index in range(len(s)):
            
            if shifting[index]>=0:
                
                char=ord(s[index])-97
                sh=(shifting[index]+char)%26
                new_str.append(chr(sh+97))
            
            else:
                
                char=ord(s[index])-97
                sh=(char+shifting[index])%26
                # print(ord(s[index]),shifting[index],sh+97,100000000)
                new_str.append(chr(sh+97))
                                  
        return "".join(new_str)
                
                
        
        
        