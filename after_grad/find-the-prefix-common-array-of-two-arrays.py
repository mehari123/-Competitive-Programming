class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        dick1 = defaultdict(int)
        dick2 = defaultdict(int)
        ans = [0 for i in range(len(A))]
        index = 0

        for a,b in zip(A,B):
            
            thisturn = 0
            if a not in dick1:

                dick1[a]= 0

            if b not in dick2:

                dick2[b]= 0

            

            if a in dick2 and dick2[a] == 0:

                thisturn += 1
                dick2[a] += 1

            if b in dick1 and dick1[b] == 0:

                thisturn += 1
                dick1[b] += 1
            
            if a == b:
                thisturn -=1
                
            ans[index] += thisturn + ans[index-1]
            index += 1
        
        return ans
                



        