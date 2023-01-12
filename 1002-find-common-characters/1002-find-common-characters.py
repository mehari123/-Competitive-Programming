class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        first_w=[0]*26

        for w in words[0]:
            char=ord(w)%97
            first_w[char]+=1

        for word in words:

            second_w=[0]*26
            for w in word:
                char=ord(w)%97
                second_w[char]+=1
            for index in range(26):
                first_w[index]=min(first_w[index],second_w[index])

        ans=[]
        for index,value in enumerate(first_w):
            for i in range(value):
                ans.append(chr(97+index))
        
        return ans

            
        


