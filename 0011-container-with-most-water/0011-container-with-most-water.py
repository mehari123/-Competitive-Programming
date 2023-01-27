class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        right=len(height)-1
        left=0
        
        result=0
        index=0
        while left<right:
            temp=0
            mini=min(height[left],height[right])
            
            if mini==height[left]:
                temp=mini*(right-left)
                left+=1
            elif mini==height[right] :
                temp=mini*(right-left)
                right-=1
            if temp>result:
                result=temp
                
        return result
        