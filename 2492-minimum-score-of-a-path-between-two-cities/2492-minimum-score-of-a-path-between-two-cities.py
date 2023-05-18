class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(int)
        rank = defaultdict(int)
        
        for x,y,z in roads:
            
            graph[x] = x
            graph[y] = y
            rank[x] = 1
            rank[y] = 1
            
        min_ = 10 ** 5
        
        def root_find(x):
            
            if x in graph and graph[x] == x:
                
                return x
            
            root = root_find(graph[x])
            graph[x] = root
            return root
        
        for road in roads:
            
            root1 = root_find(road[0])
            root2 = root_find(road[1])
            
            if root1 != root2:
                
                if rank[root1] > rank[root2]:
                    
                    graph[root2] = graph[root1]
                    rank[root1] += rank[root2]
                    
                else:
                    
                    graph[root1] = graph[root2]
                    rank[root2] += rank[root1]
                  
                
                    
        for x,y,z in roads:
          
            if root_find(x) == root_find(1) :

                min_ = min(min_,z)
                
        return min_
                    
        