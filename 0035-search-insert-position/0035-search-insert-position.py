class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)-1
        ans = 0
        while low <= high:
            
            mid = ( low + high ) // 2
            
            if nums[mid] > target :
                
                high = mid -1
                ans=mid
            elif nums[mid] < target:
                
                low = mid + 1
                ans = low
                
            else:
                
                return mid
  
        return ans if ans >= 0 else 0