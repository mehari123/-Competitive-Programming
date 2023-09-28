class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        d = {"b":0,"a":0,"l":0,"o":0,"n":0}
        
        for t in text:
            
            if t in d:
                d[t] += 1
                
      
        count  = 0
        for key,value in d.items():
            
            if key == "b" or key == "a" or key == "n":
                
                d[key] //= 1
                
            elif key == "l" or key == "o":
                
                d[key] //= 2
                
        ans = sorted(d.items(),key = lambda x: x[1])
        return ans[0][1]
        
        
        