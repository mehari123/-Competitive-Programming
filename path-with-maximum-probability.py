class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(set)
        distance = defaultdict(int)
        for index,edge in enumerate(edges):

            graph[edge[0]].add(edge[1])
            distance[(edge[0],edge[1])] = succProb[index]
            graph[edge[1]].add(edge[0])
            distance[(edge[1],edge[0])] = succProb[index]

        pro = [float("-inf") for i in range(n)]
        pro[start_node] = 1
        heap = [(start_node,1)]
        n = 0
        while heap:

            p,pr = heappop(heap)
            child = graph[p]
            # print(distance,heap)
            for ch in child:

                new_p = distance[(p,ch)] * pr
                # print(p,ch,new_p)
                
                if new_p > pro[ch]:
                    
                    # if ch == end_node -1 :

                        # return new_p
                    pro[ch] = new_p
                    heappush(heap,(ch,new_p))
                # print(pro[ch])

        # print(pro)
        return pro[end_node] if  pro[end_node]  != float("-inf") else 0.000