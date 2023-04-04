class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        nums.sort()
        a = nums[0]
        b = nums[len(nums)-1]
        
        def gcd(a,b):
            
            if b == 0:
                
                return a
            
            return gcd(b,a%b)
        
        return gcd(a,b)