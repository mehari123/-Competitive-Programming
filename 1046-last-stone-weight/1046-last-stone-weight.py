class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        
        for s in stones:
            
            heappush(heap,-s)
            
        
        while len(heap)> 1:
            
            x = - heappop(heap)
            y = - heappop(heap)
            
            if x > y:
                
                heappush(heap,-(x-y))
                
            elif x < y:
                
                heappush(heap,-(y-x))
                
        return -heap[0] if len(heap) == 1 else 0
                