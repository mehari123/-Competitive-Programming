class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        d = defaultdict(int)

        def path(i,sums):
            
            if i == n:
                return 0
            if sums == target:
                return 1
            if sums > target:
                return 0
            
            if (i,sums) not in d:
               d[(i,sums)] = path(0, sums + nums[i]) + path(i+1, sums)
                
            return d[(i,sums)]
            
    
        return (path(0,0))