class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]: 
        # queens_dict={}
        # for index,value in enumerate(queens):
        #     queens_dict[value]=index
            
        ans=[]
        row=king[0]
        col=king[1]
        for horizontal in [-1,0,1]:

            for vertical in [-1,0,1]:

                for dist in range(8):

                    row_i=row+horizontal*dist
                    col_i=col+vertical*dist
                    if [row_i,col_i] in queens:
                        ans.append([row_i,col_i])
                        break
        return ans






        






        