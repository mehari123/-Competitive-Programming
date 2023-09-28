class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        ans = [""] * len(score)
        sorted_ = []
        for index,num in enumerate(score):
            
            sorted_.append((num,index))
            
        sorted_.sort(reverse = True)
      

        for index,(i,j) in enumerate(sorted_):
            

            if index == 0:

                ans[j] = "Gold Medal"

            elif index == 1:

                ans[j] = "Silver Medal"

            elif index == 2:

                ans[j] = "Bronze Medal"

            else:

                ans[j] = str(index + 1)
      
        return ans



        