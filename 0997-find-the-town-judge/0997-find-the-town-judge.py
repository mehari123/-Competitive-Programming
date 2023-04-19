class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        graph = {i:{} for i in range(1,n+1)}
        for x,y in trust:
            graph[x][y] = True
        
        possible = []
        for x,y in graph.items():
            if len(y) == 0:
                possible.append(x)
        
        hashmap = {}
        for j in possible:
            count = 0
            for x,y in graph.items():
                if j in y.keys():
                    count += 1
            
            if count == n-1:
                return j
        
        return -1