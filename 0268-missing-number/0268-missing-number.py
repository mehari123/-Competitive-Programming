class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums1 = [-1]* (len(nums) + 1)
        
        
        for num in nums:
            
            nums1[num]= num
            
        
        for index,n in enumerate(nums1):
            print(index,n)
            if index != n:
                return index
            
            