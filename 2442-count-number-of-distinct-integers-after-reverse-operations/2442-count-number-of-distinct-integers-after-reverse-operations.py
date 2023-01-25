class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        nums=list(map(str,[num for num in nums]))
        size=len(nums)
        for index in range(size):
            nums.append(nums[index][::-1])
        
        nums=list(map(int,[str2 for str2 in nums]))
        
        nums=sorted(nums)
        count=0
        
        size2=len(nums)
        for index in range(1,size2):
            
            if nums[index-1]==nums[index]:
                count+=1
                size2-=1
        
        return size2
            
        