class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        over_sight = 0
        prevS = 0
        
        for num in values:
            
            over_sight = max(over_sight,num+prevS-1)
            prevS = max(prevS-1,num)
            
        return over_sight
        
        
        