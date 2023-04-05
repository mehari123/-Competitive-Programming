import math
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def isprime(n):
            
            if n < 3:
                return n > 1
            index = 2   
            while index <= math.sqrt(n):
                
                if n % index == 0:
                    
                    return False
                index += 1
            return True
        
        nums = []
        gap = float("inf")
        ans = []
        
        while left < right +1:
            
            if isprime(left):
                if nums and gap > (left- nums[-1]):
                    
                    ans =[nums[-1],left]
                    gap = left- nums[-1]
                    
                    if gap <= 2:
                        return ans

                nums.append(left)
                
            left +=1
        
        
        return ans if len(ans) > 1 else [-1,-1]
        
        