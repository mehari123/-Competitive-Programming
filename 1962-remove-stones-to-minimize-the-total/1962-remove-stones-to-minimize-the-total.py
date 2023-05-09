class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = []
        
        for pile in piles:
            
            heappush(heap,-pile)
        print(heap)  
        
        while k > 0:
            
            large_num = heappop(heap)
            large_num //=2
            heappush(heap,large_num)
            k -= 1
        
        return sum([-h for h in heap])