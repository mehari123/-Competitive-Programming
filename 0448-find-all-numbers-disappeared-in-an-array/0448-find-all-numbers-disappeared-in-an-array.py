class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        sorted1 = [0]* len(nums)
        
        print(sorted1)
        for num in nums:
            
            sorted1[num-1] = num
        print(sorted1)
        ans = []
        for index,n in enumerate(sorted1):
            
            if n == 0:
                
                ans.append(index+1)
                
        return ans
            
            
        
            
            
        
            
            