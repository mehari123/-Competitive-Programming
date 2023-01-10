class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split(" ")
        
        max_len=max(len(word) for word in words)
        
        vert_word=[]
        
        for index in range(max_len):
            str_temp=""
            for word in words:
                
                if len(word)>index:
                    str_temp+=word[index]
                else:
                    str_temp+=" "
            str1=str_temp.rstrip()  
            vert_word.append(str1)
        
        return vert_word
                
                
                
                