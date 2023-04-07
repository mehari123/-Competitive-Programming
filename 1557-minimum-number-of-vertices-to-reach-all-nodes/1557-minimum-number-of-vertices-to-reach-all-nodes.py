class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        outdegree = set()
        indegree = set()
        
        for edge in edges:
            
            outdegree.add(edge[0])
            indegree.add(edge[1])
            
        intersection = outdegree & indegree
        ans = []
        
        for out in outdegree:
            
            if out not in intersection:
                
                ans.append(out)
                
        return ans