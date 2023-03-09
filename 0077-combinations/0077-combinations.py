class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combination = []
        combi=[]
        
        def backtrack(left,n):
            
            
            if len(combi) == k:

                combination.append(combi[::])

                return 
            
            for i in range(left,n):

                combi.append(i)
                backtrack(i+1,n)
                combi.pop()
                # backtrack(left+1)
        backtrack(1, n+1)
        
        return combination

        
        