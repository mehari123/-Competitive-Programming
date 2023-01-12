class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        len_num=len(nums)
        index=0

        for index in range(1,len_num):

            if nums[index-1]==nums[index]:
                nums[index-1]=2*nums[index-1]
                nums[index]=0

        
        read=0
        write=0
        while read<len(nums):
            if nums[read]!=0:
                nums[write],nums[read]=nums[read],nums[write]
                write+=1
            read+=1

        return nums
        