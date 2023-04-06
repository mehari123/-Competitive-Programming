class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        
        def findPrimeSieve(n):
            
            nums = [1] * (n+1)
            
            nums[0],nums[1]=0,0
            
            prime = 2
            
            while math.sqrt(n) >= prime:
                
                if nums[prime] == 1:
                    
                    i = prime * prime
                    while i <= n:
                    
                        nums[i] = 0
                        i += prime
                        
                prime += 1
                
            ans = []
            
            for index,num in enumerate(nums):
                
                if num == 1:
                    
                    ans.append(index)
                    
            return ans
        
        primes = findPrimeSieve(1001)
        count = 0
        num_primes = set()
        
        for num in nums:
            
            for prime in primes:
                
                if prime > num:
                    break
                elif num % prime == 0:
                    
                    num_primes.add(prime)
                    
        return len(num_primes)
                    
            
            
        
        
        
        