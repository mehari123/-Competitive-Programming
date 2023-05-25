class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = float("inf")
        second = float("inf")
        # third = float("inf")
    
        for num in nums:

            if num < first:

                first = num

            if num > first and num < second:

                second = num

            if num > second:

                return True
        
       
        return False