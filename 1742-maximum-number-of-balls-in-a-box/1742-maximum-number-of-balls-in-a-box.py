class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        d = defaultdict(int)
        maxi = 0
        for i in range(lowLimit,highLimit + 1):
            
            r = str(i)
            su = 0
            for k in r:
                
                su += int(k)
                
            d[su] += 1
            maxi = max(maxi,d[su])
            
        return maxi
            
        
                
                
        