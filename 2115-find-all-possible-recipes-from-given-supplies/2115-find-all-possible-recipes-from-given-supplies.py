class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for index,recip in enumerate(recipes):
            
            indegree[recip] = len(ingredients[index])
            
            for ing in ingredients[index]:
                
                graph[ing].append(recip)
                
        
        
        que = deque(supplies)
        answer = []
        while que:
            
            for _ in range(len(que)):
                
                current = que.popleft()
                childes = graph[current]
                
                if current in recipes:
                    
                    answer.append(current)

                for child in childes:

                    indegree[child] -= 1

                    if indegree[child] == 0:

                        que.append(child)
                        

                        
        return answer
                    
                    
            
            
            
                
                
                
                
            
            
            
            
        