class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_dict = defaultdict(int)

        for n in nums :

            nums_dict[n] += 1

        sorted_n = sorted(nums_dict.items(), key=lambda x: x[1])
        ans = []
        n = len(sorted_n)-1

        while k > 0:

            ans.append(sorted_n[n][0])
            k-= 1
            n-=1
        
        return ans


        