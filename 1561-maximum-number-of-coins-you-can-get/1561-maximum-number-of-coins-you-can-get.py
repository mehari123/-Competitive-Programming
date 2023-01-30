class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        left=0
        right=len(piles)-2
        max_p=0
        
        piles.sort()
        
        while left<right:
            max_p+=piles[right]
            right-=2
            left+=1
        return max_p
            
            