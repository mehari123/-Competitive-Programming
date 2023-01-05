class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sum_nums=sum(nums)
        
        size_num=len(nums)+1
        full_sum=sum(num for num in range(size_num))
        
        return full_sum-sum_nums
        
        