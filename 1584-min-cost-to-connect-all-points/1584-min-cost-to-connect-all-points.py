class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        connected_p = []
        
        for i in range(len(points)):
            
            for j in range(len(points)):
                
                if i != j:
                    
                    dist = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                    connected_p.append([i,j,dist])
                    
        
        connected = sorted(connected_p, key = lambda x: x[2])
        
        graph = defaultdict(int)
        rank = defaultdict(int)
        
        graph = {i:i for i in range(len(connected))}
        rank = {i:1 for i in range(len(connected))}
        
        def find(x):
            
            if graph[x] == x:
                
                return x
            
            root = find(graph[x])
            graph[x] = root
            return root
        
        
        # print(connected)
        def union(connected):
            
            min_d = 0
            count = 0
            for con in connected:
                
                root1 = find(con[0])
                root2 = find(con[1])
                
                if root1 != root2:
                    
                    graph[root2] = graph[root1]
                    
                    min_d += con[2]
                    count += 1
                    
                if count == len(points)-1:
                    
                    return min_d
                
        return union(connected) if connected else 0
                    
                
        
                    
                