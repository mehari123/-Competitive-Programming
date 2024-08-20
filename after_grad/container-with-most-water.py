class Solution:
    def maxArea(self, height: List[int]) -> int:

        left,right = 0, len(height)-1
        max_area = 0 

        while left < right:

            width = right - left
            max_height = min ( height[left],height[right])
            max_area = max(max_area,width * max_height)

            if height[left] > height[right]:

                right -= 1

            else:
                left += 1

        return max_area

        