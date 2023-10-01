class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        row = defaultdict(int)
        col = defaultdict(int)
        
        for i in indices:
            
            row[i[0]] += 1
            col[i[1]] += 1
            
        ans = 0
        
        for r in range(m):
            
            for c in range(n):
                
                su = row[r]
                su += col[c]
                
                if su % 2 != 0:
                    
                    ans += 1
                
                
        # print(ans)
        return ans
        
        