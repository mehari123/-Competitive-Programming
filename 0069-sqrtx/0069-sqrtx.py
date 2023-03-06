class Solution:
    def mySqrt(self, x: int) -> int:
        
        high = x
        low = 0
        
        while low < high :
            
            
            mid = ( high + low ) // 2
            
            if mid * mid <= x < (mid + 1) * (mid + 1):
                
                return mid
            
        
            if mid * mid > x :
                
                high = mid - 1
                
            else:
               
                low = mid + 1
                     
        return low
        