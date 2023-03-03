# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        low=0
        high=n
        mid=0
        ans=0
        while low<=high:
            
            mid=(low+high)//2
            
            if isBadVersion(mid):
                
                high=mid-1
                ans=mid
            else:
                
                low=mid+1
                    
        return ans
            
        