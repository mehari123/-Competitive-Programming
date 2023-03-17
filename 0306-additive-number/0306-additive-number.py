class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def Additiv(index,sub_add):
            
            if sub_add and len(sub_add[-1])>1 and sub_add[-1][0] == "0":
                
                return False
            
            if len(sub_add) >= 3:
                
                if  int(sub_add[-3]) + int(sub_add[-2]) != int(sub_add[-1]):
                    
                    return False
                
                elif index == len(num) :
                
                    return  True
                
            for i in range(index + 1, len(num) +1):
                
                if Additiv(i,sub_add + [num[index:i]]):
                    
                    return True
                
        return Additiv(0,[])
                
    
                    
                    
        