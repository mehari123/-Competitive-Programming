class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        maxi = 0 
        ro_m = float("inf")
        col_m = float("inf")
        
        if not ops:
            
            return m * n
        
        for op in ops:
            
            ro_m = min(ro_m,op[0])
            col_m = min(col_m,op[1])
            
        return int(ro_m * col_m)
                
        
    