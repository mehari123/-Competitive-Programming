class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        # memo = defaultdict(int)
        # max_ = 0
        # def max_p(i):
            
        #     nonlocal max_
        #     if i >= len(questions):
        #         return 0
        #     if i in memo:
        #         return memo[i]
                
        #     take  = questions[i][0] + max_p(i + questions[i][1]+1)
        #     not_take = max_p(i+1)

        #     max_ = max(take, not_take) 
        #     memo[i] = max_
        #     return max_

        # return max_p(0)
        n = len(questions)
        ans = [0]*n
        for i in range(n-1, -1, -1):
            if i + questions[i][1]+1>=n:
                take =  questions[i][0]
            else: 
                take = questions[i][0] + ans[i + questions[i][1]+1]
            if i+1>=n:
                not_take = 0

            else: 
                not_take = ans[i+1]
            ans[i] =  max(take, not_take)
        
        return ans[0]