from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        sortedList = SortedList()
        ans = []

        for i in range(len(nums)-1,-1,-1):

            sortedList.add(nums[i])
            index = bisect_left(sortedList,nums[i])
            ans.append(index)

        ans.reverse()
        return ans