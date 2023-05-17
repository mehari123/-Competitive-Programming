class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        graph = {i:i for i in range(1,len(edges) + 1)}
        rank = {i:1 for i in range(1,len(edges) + 1)}
        
        def find_root(x):
            
            if graph[x] == x:
                
                return x
            
            root = find_root(graph[x])
            graph[x] = root
            return root
        
        for edge in edges:
            
            root1 = find_root(edge[0])
            root2 = find_root(edge[1])
            
            if root1 == root2:
                
                return [edge[0],edge[1]]
            else:
                
                if rank[root1] > rank[root2]:
                    
                    graph[root2] = graph[root1]
                    rank[root1] = rank[root2]
                    
                else:
                    
                    graph[root1] = graph[root2]
                    rank[root2] = rank[root1]
                    
        