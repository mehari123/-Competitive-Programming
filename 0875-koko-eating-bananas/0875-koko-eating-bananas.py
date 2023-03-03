class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        high = max(piles)
        low = 1
        mid = high
        ans = mid
        
        while low < high:
            
            mid=(low+high)//2
            hour=0
            
            for pile in piles:
                
                hour += (pile//mid) + int(pile%mid > 0)
            
            if hour <= h:
                high = mid
                
            else:
                low = mid + 1 
                
        return high