import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        sum1=0
        a=0
        b=int(math.sqrt(c))
        while a<=b:
            sum1=0
            sum1=(a*a) + (b*b)
            if sum1<c:
                a+=1
            elif sum1>c:
                b-=1
            elif sum1==c:
                return True
        return False