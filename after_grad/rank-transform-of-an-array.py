class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        sorted1 = defaultdict(int)
        sortedarr = sorted(set(arr))
        
        for i,j in enumerate(sortedarr):

            sorted1[j] = i + 1

        ans = []
        for a in arr:
            ans.append(sorted1[a])

        return ans

        


        