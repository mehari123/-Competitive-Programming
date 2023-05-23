class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:      
        graph = {i:i for i in range(len(stones))}
        rank = {i:1 for i in range(len(stones))}
        
        canBeRemoved = lambda x1, y1, x2, y2: x1==x2 or y1==y2
        
        def find(x):
            if x == graph[x]:
                return x
            
            root = find(graph[x])
            graph[x] = root
            return root
        
        
        
        def union(i,j):
            root1 = find(i)
            root2 = find(j)
                
            if root1 != root2:
                if rank[root1] < rank[root2]:
                        root1, root2 = root2, root1
                        
                graph[root2] = root1
                rank[root1] += rank[root2] 

                
        
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                    if canBeRemoved(stones[i][0], stones[i][1], stones[j][0], stones[j][1]): 
                        union(i, j)
                
        parents = set()        
        for i in range(len(stones)):
            parents.add(find(i))
            
        return len(stones) - len(parents)
        
                        
                    
                
                
                
                
        