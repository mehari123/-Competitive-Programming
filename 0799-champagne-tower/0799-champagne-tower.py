class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        champagne = [[0 for _ in range(x)] for x in range(1, query_row + 2)]
        champagne[0][0] = poured
        
        
        for i in range(query_row):
            for j in range(len(champagne[i])):
                temp = (champagne[i][j] - 1) / 2.0
                if temp>0:
                    champagne[i+1][j] += temp
                    champagne[i+1][j+1] += temp
                    
        
        return champagne[query_row][query_glass] if champagne[query_row][query_glass] <= 1 else 1