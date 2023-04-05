class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        power = []
        
        def subset(sub ,index ):
            
            if index == len(nums):
                
                power.append(sub[::])
                return 
           
          
            sub.append(nums[index])
            subset(sub,index + 1)
            sub.pop()
            subset(sub,index + 1)
                
        
        subset([] , 0)
        return power