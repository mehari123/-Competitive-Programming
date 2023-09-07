class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        graph = defaultdict(list)
        for child, p in enumerate(parent):
            graph[p].append(child)
        
        if len(parent) == 0:

            return 0

        elif len(parent) == 1:

            return 1

        long_path= 0
        def dfs(node):
            nonlocal long_path
            if node not in graph:

                return 1
           
            longest_path = 0
            second_longest = 0

            for child in graph[node]:

                child_path_len= dfs(child)
                
                if s[child] == s[node]:
                    continue
                
                if child_path_len > longest_path:

                    second_longest = longest_path
                    longest_path=child_path_len 

                elif  child_path_len > second_longest:

                    second_longest = child_path_len 

            long_path = max(long_path,longest_path + second_longest + 1)
            return longest_path + 1
            
        
        dfs(0)
        return long_path