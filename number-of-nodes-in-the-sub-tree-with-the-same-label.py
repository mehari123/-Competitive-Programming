from collections import defaultdict
from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0]) 

        ans = [1] * n
        label = ""

        def dfs(root):
            nonlocal label
            count = [0] * 26  
            node_label = ord(labels[root]) - ord('a')
            count[node_label] = 1  
            for child in graph[root]:
                graph[child].remove(root)  
                child_count = dfs(child)
                for i in range(26):
                    count[i] += child_count[i] 
            ans[root] = count[node_label]
            return count

        dfs(0)  

        return ans