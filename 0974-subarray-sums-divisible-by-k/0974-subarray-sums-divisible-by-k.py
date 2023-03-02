class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        
        pre_sum=[0]
        ans=0
        
        division={0:0}
        
        for num in nums:
            
            pre_sum.append(pre_sum[-1]+num)
            
        for sum1 in pre_sum:
            
            if (sum1%k) in division:
                
                ans+=division.get(sum1%k,0)
                
                division[sum1%k]=division.get(sum1%k,0)+1
            else:
                division[sum1%k]=1
                
            
        print(division)      
        return ans
        
        
        