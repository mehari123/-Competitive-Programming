class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        p1 = 0
        p2 = 1
        du = 0

        while p2 < len(nums):

            if nums[p1] == nums[p2] and du >= 1:

                p2 += 1

            elif nums[p1] != nums[p2]:

                p1 += 1
                nums[p1] = nums[p2]
                p2 += 1
                du = 0
            elif  du < 2:

                if nums[p1] == nums[p2]:
                    du += 1
                p1 += 1
                nums[p1] = nums[p2]
                p2 += 1

        # print(nums)
        return p1 + 1

