"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        
        graph = defaultdict(int)
        importance = defaultdict(int)
        for emp in employees:
            # print(emp)
            graph[emp.id] = emp.subordinates
            importance[emp.id] =emp.importance
       
        self.total = 0
        def dfs(currId):
            
            
            for idi in graph[currId]:
                
                dfs(idi)
            
            self.total += importance[currId]
         
        dfs(id)
        return self.total
        
        