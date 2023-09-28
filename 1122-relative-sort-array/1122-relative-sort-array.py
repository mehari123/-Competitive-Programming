class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        d = defaultdict(list)
        
        for k in arr2:
            
            d[k] = []
        
        d2 = []
        for a in arr1:
            
            if a in d:
                d[a].append(a)
                
            else:
                d2.append(a)

        # print(d,d2)
        ans = []

        for b in arr2:
            
            ar = d[b]
            
            for j in ar:
                
                ans.append(j)
        
        # print(ans)
        ans.extend(sorted(d2))
        return ans
        