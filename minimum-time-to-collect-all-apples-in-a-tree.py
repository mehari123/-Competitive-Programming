class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])  
            
        def dfs(root, parent):
            total_time = 0

            for child in graph[root]:
                if child != parent:
                    child_time = dfs(child, root)

                    if child_time > 0 or hasApple[child]:
                        total_time += child_time + 2

            return total_time

        return dfs(0, -1)