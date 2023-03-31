class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
       
    
        prev = None
        while n:

            last_bit = n % 2

            if last_bit == prev :

                return False

            prev = last_bit
            n = n >> 1

        return True