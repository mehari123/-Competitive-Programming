from collections import defaultdict

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        num_path = defaultdict(int)
        added_path = set()

        def dp(k,r):

            if  not (0 <= k < m  and 0 <= r < n):
                return 0
            if (k,r) == (m-1,n-1) :
                return 1
            if (k,r) not in num_path:
                
                path =  dp(k+1,r) + dp(k,r+1)
                num_path[(k,r)] = path
            
            return num_path[(k,r)]

        # print(num_path)           
        return dp(0,0)