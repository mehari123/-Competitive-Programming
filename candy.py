class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = len(ratings)
        givcan = [1]* candy
        dep = 0
        count = len(ratings)

        for i in range(len(ratings)):

            if i - 1 >= 0:

                if ratings[i-1] < ratings[i]:

                    if givcan[i-1] >= givcan[i]:

                        givcan[i] = givcan[i-1] + 1

                
            if i + 1 < len(ratings):

                if ratings[i+1] < ratings[i]:

                    if givcan[i+1] >= givcan[i]:

                        givcan[i] = givcan[i+1] + 1
        i=0
        for i in range(len(ratings)-1,-1,-1):

            if i - 1 >= 0:

                if ratings[i-1] < ratings[i]:

                    if givcan[i-1] >= givcan[i]:

                        givcan[i] = givcan[i-1] + 1

                
            if i + 1 < len(ratings):

                if ratings[i+1] < ratings[i]:

                    if givcan[i+1] >= givcan[i]:

                        givcan[i] = givcan[i+1] + 1
                        
        return sum(givcan)