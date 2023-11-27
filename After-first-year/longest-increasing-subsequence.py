class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        count = 0
        memo = defaultdict(int)
        visited = set()
        

        def dp(index):

            nonlocal memo
            if index == len(nums)-1:

                return 0

            subs = 0
            maxs = 0
            for i in range(index + 1,len(nums)):

                
                if nums[index] < nums[i]:

                    if i in memo:

                        subs = memo[i] + 1

                    else:

                        subs = dp(i) + 1
                        
                    if maxs < subs:

                        maxs = subs
                else:

                    if i not in memo:

                        dp(i)

            memo[index] = maxs
            return memo[index]

        dp(0)
        return max([val for key,val in memo.items()]) + 1 if len(nums) > 1 else 1
                



        