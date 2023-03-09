class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        Sub =[[]]
        def subset(index,temp):
            
            if index == len(nums):
                
                return 
            
            temp.append(nums[index])
            
            if temp not in Sub:
                
                Sub.append(temp[::])
              
            subset(index+1,temp)
            temp.pop()
            subset(index+1,temp)
            
            return
        
        subset(0,[])
        return Sub
        