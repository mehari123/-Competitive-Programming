class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        separate_str=[]
        len_spa=len(spaces)
        
        if spaces[0]==0 and len_spa==1:
            separate_str.append("")
            separate_str.append(s[spaces[0]:])
            
        elif len_spa==1:
            separate_str.append(s[:spaces[0]])
            separate_str.append(s[spaces[0]:])
        else:
             separate_str.append(s[:spaces[0]])
            
        
        
        for index in range(1,len_spa):
            
            if index==len_spa-1:
                separate_str.append(s[spaces[index-1]:spaces[index]])
                separate_str.append(s[spaces[index]:])
                
            else:
                separate_str.append(s[spaces[index-1]:spaces[index]])
            
            
            
        return " ".join(separate_str)
        