class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        adjecency = {i : set() for i in range(1,len(edges) + 2)}
        
        for edge in edges:
            
            adjecency[edge[0]].add(edge[1])
            adjecency[edge[1]].add(edge[0])
        
        value = sorted(adjecency.items(),key = lambda x: len(x[1]))
        return value[-1][0]
        