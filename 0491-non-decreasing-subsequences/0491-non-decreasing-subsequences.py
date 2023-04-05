class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        increasing ={}
        sub = []
        def bactrack(index):
            
            if len(sub)>1:
                
                increasing[tuple(sub)]=1

            
            for i in range(index,len(nums)):
        
                if not sub or sub[-1] <= nums[i]:

                    sub.append(nums[i])
                    bactrack(i+ 1)
                    sub.pop()
              
          
        
        bactrack(0)
        return increasing.keys()