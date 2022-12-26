class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size1=len(word1)
        size2=len(word2)
        size=size1+size2
        merged=''
        i=0
        k=0
        while i<size:
            if k<size1:
                merged+=word1[k]
                i+=1
            if k<size2:
                merged+=word2[k]
                i+=1
            k+=1
        return merged
