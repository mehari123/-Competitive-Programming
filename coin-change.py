class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        mini = float('inf')
        count = 0
        min_ = defaultdict(int)
        memo={}
        def dp(amountr):

            nonlocal count,mini
            if amountr == 0:
                

                return 0 

            if amountr in memo:
                
                return memo[amountr ]
            s=float('inf')
            for i in coins:

                if amountr-i >= 0:
                    
                   
                    s= min(s,dp(amountr-i))
            
            memo[amountr]=s+1
            return s+1
                        
          
        mini = dp(amount)        
        return mini if mini!= float('inf ') else -1