class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        odds=defaultdict(lambda:0)
        pre_sum=[0]
        
        for num in nums:
            
            if num%2!=0:
                pre_sum.append(1+pre_sum[-1])
            else:
                pre_sum.append(pre_sum[-1])
            
  
        for pre in pre_sum:
            
            odds[pre]+=1

        odd_count=0
        
        for pre in pre_sum:
            
            odd_count+=odds[pre-k]
         
        # print(odds,pre_sum)
        return odd_count
        
       
        
                
                