class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        list1=[]
        for i in range(1,n+1):
            list1.append(i)
        
        index=0
        loser=0
        while len(list1)>1:
            
            loser = (loser+k-1)%len(list1)
            del list1[loser]
        return list1[0]
        
