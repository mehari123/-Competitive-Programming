class Solution:
    def decodeString(self, s: str) -> str:
        
        result=""
        stack=[]
        
        def decode(index):
            
            nonlocal result
            nonlocal stack
            
            if index>=len(s):
                
                return result
            
            if s[index].isdigit():
                
                num=""
                
                while index<len(s)and s[index].isdigit():
                    
                    num+=s[index]
                    index+=1
                
                stack.append([int(num)])
                return decode(index+1)
            
            elif s[index]=="]":
                
                value1=stack.pop()
                
                if len(stack)==0:
                    
                    result+="".join(str(e) for e in value1[0]*value1[1:])
                    return decode(index+1)
                else:
                    
                    value1="".join(value1[0]*value1[1:])
                    stack[-1].append(value1)
                    return decode(index+1)
            else:
                
                if len(stack)==0:
                    
                    stack.append([])
                    
                stack[-1].append(s[index])
                
                if str(stack[-1][0]).isnumeric()==False:
                    
                    value2=stack.pop()
                    result+="".join(value2)
                      
                return decode(index+1)
                
        output=decode(0)
        
        if len(stack)>=1:
            
            value1=stack.pop()
            output+="".join(value1[0]*value1[1:])
            
        return output
            
                