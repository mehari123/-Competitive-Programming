class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        sum_arr=[item *2 for item in arr]
        size=len(sum_arr)
        for i,num1 in enumerate(arr):
            for j,num2 in enumerate(arr):
                if num1==2*num2 and i!=j:
                    return True
        return False
