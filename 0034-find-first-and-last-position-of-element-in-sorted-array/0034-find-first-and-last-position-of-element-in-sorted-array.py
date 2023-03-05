class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left_l = 0
        left_h = len(nums)-1
        
        if len(nums)==0: return [-1,-1]
        
        while left_l < left_h:
            
            mid = ( left_l + left_h ) // 2
            
            if nums[mid] >= target:
                
                left_h = mid
                
            else:
                
                left_l = mid + 1
                
        ans1 = left_h if (0<= left_h < len(nums)) and nums[left_h] == target else -1
        
        right_l = 0
        right_h = len(nums)-1
        ans2 = 0
        
        while right_l < right_h:
            
            mid = ( right_l + right_h ) // 2
            
            if nums[mid] > target:
                
                right_h = mid
                
            else:
                
                right_l = mid+1
                ans2= mid
                      
        ans2 = ans2 if ( 0 <= ans2 < len(nums)) and nums[ans2] == target else -1
        ans2 = len(nums)-1 if nums[len(nums)-1] == target else ans2
        
        return [ans1,ans2]
            
            
            
                
                