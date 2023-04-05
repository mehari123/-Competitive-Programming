class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        perm = []
        
        def dfs(i, prev):
            if i==len(nums):
                if len(perm)>=2:
                    res.add(tuple(perm))
                return
                
            dfs(i+1, prev)
            
            if nums[i]>=prev:
                perm.append(nums[i])
                dfs(i+1, nums[i])
                perm.pop()
        
        dfs(0, -inf)
        return list(res)