from sortedcontainers import SortedList

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def count_reverse_pairs(arr):
            if len(arr) <= 1:
                return 0

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            count = count_reverse_pairs(left) + count_reverse_pairs(right)

            j = 0
            for num in left:
                while j < len(right) and num > 2 * right[j]:
                    j += 1
                count += j

            left.extend(right)
            arr[:] = sorted(left)

            return count

        sortedList = SortedList(nums)
        return count_reverse_pairs(nums)