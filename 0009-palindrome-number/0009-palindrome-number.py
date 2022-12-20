class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        size=len(num)
        i,j=0,size-1

        while i<j:
            if (num[i]!=num[j]):
                return False
            i=i+1
            j=j-1
        return True
        