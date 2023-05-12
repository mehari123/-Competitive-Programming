class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for edge in edges:
            
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
            indegree[edge[1]] += 1
            
        
        graph = dict(sorted(graph.items(),key = lambda items: len(graph.values()),reverse=True))
        
        que = deque()
        for key,value in graph.items():
            if len(value) == 1:
                
                que.append(key)
        
        ans = list()
        visited = set()
        if not edges:
            return [0]
        
        while que:
            
            
            next_ = list()
            for _ in range(len(que)):
            
                parent = que.popleft()
                visited.add(parent)
                childs = graph[parent]
                for child in childs:
                
                    if child in que:
                        
                        
                        ans.append(child)
                        ans.append(parent)
                        return ans
                    
                    if child not in visited:
                        
                        indegree[child] -= 1

                        if indegree[child] == 1:

                            next_.append(child)

                        if indegree[child] == 0:

                            ans.append(child)
                            return ans
                
            que.extend(next_)
            
                        

                    
                
                    
                    
                    
                
            
            
            
            
                
            
                    
            
        
            
        