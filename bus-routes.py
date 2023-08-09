class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        graph = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].append(i)  # Create a mapping of stop to the routes it's a part of
        
        que = deque([(source, 0)])  # Start from the source with a distance of 0
        visited_routes = set()  # Keep track of visited routes
        
        while que:
            stop, distance = que.popleft()
            
            for route_idx in graph[stop]:
                if route_idx in visited_routes:
                    continue
                
                visited_routes.add(route_idx)
                for next_stop in routes[route_idx]:
                    if next_stop == target:
                        return distance + 1
                    que.append((next_stop, distance + 1))
        
        return -1  # If not reachable