class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        good_meal={}
        meal_count=0

        for food in deliciousness:

            for meal in range(22):

                if (2**meal)-food in good_meal:

                    meal_count+=good_meal[(2**meal)-food]

            if food in good_meal:

                good_meal[food]+=1

            else:
                
                good_meal[food]=1

        return meal_count % ((10**9)+7)





















        # brute force solution 


        # good_meal=0
        # try1=[]
        # deli=0
        # deli1=1
        # while deli<len(deliciousness):
        #     deli1=deli+1
        #     while deli1<len(deliciousness):
        #         meal=0.0
        #         meal=deliciousness[deli]+deliciousness[deli1]
        #         while meal>0:
        #             if meal<=1:
        #                 break
        #             meal=meal/2    
        #         if meal==1.0:
        #             good_meal+=1
        #         deli1+=1
        #     deli+=1
        # return good_meal


        