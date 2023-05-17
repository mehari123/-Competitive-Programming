class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = {i:i for i in range(n)}
        rank = { i :1 for i in range(n)}
        
        def find_root(x):
            
            if graph[x] == x:
                
                return x
            root = find_root(graph[x])
            graph[x] = root
            return root
            
        for edge in edges:
            
            root1 = find_root(edge[0])
            root2 = find_root(edge[1])
            
            if root1 != root2:
                
                if rank[root1] > rank[root2]:

                    graph[root2] = graph[root1]
                    rank[root2] += rank[root1]

                else:

                    graph[root1] = graph[root2]
                    rank[root1] += rank[root2]
                
                
        return find_root(graph[source]) == find_root(graph[destination])
        
        
        