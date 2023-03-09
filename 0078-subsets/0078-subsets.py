class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        Sub =[[]]
        def subset(index,temp):
            
            if index >= len(nums):
                
                return 
            
            temp.append(nums[index])
            
            Sub.append(temp[::])
            
            subset(index+1,temp)
            temp.pop()
            subset(index+1,temp)
            
            return
        
        subset(0,[])
        return Sub
        
            
            
        