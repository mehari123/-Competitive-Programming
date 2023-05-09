class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        
        heap = []
        
        for i in range(len(matrix)):
            
            for j in range(len(matrix[0])):
                
                if len(heap) < k:
                    
                    heappush(heap,-matrix[i][j])
                
                else:
                    
                    larg = heappop(heap)
                    
                    if -larg > matrix[i][j]:
                        
                        heappush(heap,-matrix[i][j])
                    else:
                        
                        heappush(heap,larg)
                        
        return -heappop(heap)
                