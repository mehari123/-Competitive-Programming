class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sorted_num=sorted(nums,reverse=False)
        size=len(nums)
        index_1=size-1
        index_2=index_1-1
        index_3=index_2-1
        while index_3>=0:
            long_side=sorted_num[index_1]
            sum_short=sorted_num[index_2] + sorted_num[index_3]
            if long_side<sum_short:
                return long_side+sum_short
            elif index_3>=0:
                index_3-=1
                index_2-=1
                index_1-=1
        return 0
               
