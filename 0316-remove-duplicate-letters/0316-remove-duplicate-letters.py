class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_index = defaultdict(lambda:-3)
        
        for index,st  in enumerate(s):
            
            last_index[st] = index
            
        stack =[]
        visitd = defaultdict (lambda: -3)
        
        for index,st in enumerate(s):
            
            if st  in visitd:
                continue
                
            while stack and stack[-1] > st and last_index[stack[-1]] > index:
                
                visitd.pop(stack[-1])
                stack.pop()
               
            stack.append(st)
            visitd[st] = 1  
              
        return "".join(stack)
                
                
        
                
                    
                    
                    
                    
                    
                    
        
        