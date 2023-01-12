class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        deleted=0
        len_str=len(strs[0])
        
        for index in range(len_str):
            
            prev_char=strs[0][index]
            
            for chars in strs:
                
                if ord(chars[index])>= ord(prev_char):
                    
                    prev_char=chars[index]
                    
                else:
                    
                    deleted+=1
                    break
                    
        return deleted
        
        
        