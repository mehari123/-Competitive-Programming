class Solution:
    def similarPairs(self, words: List[str]) -> int:
        distinct=[]
        for i in range(len(words)):
            str1=sorted(set(words[i]))
            str1="".join(str1)
            distinct.append(str1)
        index=0
        numPair=0
        word=sorted(distinct)
        while index<len(words):
            pairs=word.count(word[index])
            pairsu=sum([i for i in range(pairs)])
            if pairs>1:
                numPair+=pairsu
                index+=pairs
            else:
                index+=1
        return numPair
            
        