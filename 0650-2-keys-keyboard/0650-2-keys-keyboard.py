import math
class Solution:
    def minSteps(self, n: int) -> int:
        
        def isPrime(n):
            
            if n <= 3:
                
                return n > 1
            
            if n % 2 == 0 or n % 3 == 0:
                
                return True
            
            i = 1
            
            while i < math.sqrt(n):
                
                if n % i == 0 :
                    
                    return True
                
                i += 1
                
            return False
        
        
        operation_count = 0
        index = 2
        
        while index <= n:
            
            if  (index > 2 and index % 2 != 0) or index <= 2:
                
                if isPrime(index) :

                    if n % index == 0:

                        operation_count += index
                        n //= index
                        index = 1

            index += 1
            
        return operation_count
            
        
        
        
        
        
        