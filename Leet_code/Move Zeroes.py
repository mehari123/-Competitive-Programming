class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index=''
        i=0
        zero_index=''
        while i<len(nums):
            if ((nums[i]==0 and zero_index=='')):
                zero_index=i
            elif (nums[i]!=0 and zero_index!=''):
                nums[zero_index]=nums[i]
                nums[i]=0
                if (nums[zero_index+1]!=0):
                    zero_index=i
                else:
                    zero_index+=1
            i+=1
