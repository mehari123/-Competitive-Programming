class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def gcd(a,b):
            
            # print(a,b)
            if b == 0:
                
                return a
            
            return gcd(b,(a % b))
            
        ans = 0
        for num in range(len(nums)):
            
            GCD = nums[num]
            
            for num2 in range(num,len(nums)):
                
                
                GCD = gcd(GCD,nums[num2])
                
                if GCD == k:
                    
                    ans += 1
        return ans
        