class Solution:
    def findComplement(self, num: int) -> int:
        
        ans = []
        binary = []
        
        while num > 0:
            
            mod = num % 2 
            
            num = num // 2
            
            if mod == 1 :
                
                ans .append(0)
                binary.append(0)
                
            else:
                
                ans .append(1)
                binary.append(1)
                
        ans_num = 0 
        
        for index, n in enumerate(ans):
            
            if n == 1 :
                
                ans_num += 2 ** index
            
        return ans_num
                
    
                