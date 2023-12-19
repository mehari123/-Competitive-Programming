class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # using shortest path algo
        graph = defaultdict(set)

        for eq,va in zip(equations,values):

            graph[eq[0]].add((eq[1],va))
            graph[eq[1]].add((eq[0],1/va))

        ans = []
        print(graph)
        for qr in queries:

            que = deque()
            que.append((qr[0],1))
            br = False
            visited = set()
            while que:

                parent,val = que.popleft()
                # print(parent,val)
                visited.add(parent)
                children = graph[parent]
                # print(que,children)

                for ch in children:

                    # print(ch[0],qr[1],"ch and qr")
                    if ch[0] == qr[1]:
                        ans.append(val * ch[1])
                        br = True
                        break
                    if ch[0] not in visited:

                        que.append((ch[0],val * ch[1]))

                if br:
                    break
            if not br:

                ans.append(-1.0)
        return ans
            


                

                    



