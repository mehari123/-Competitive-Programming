class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        shufled_str={}

        for char in t:
            if char in shufled_str.keys():
                shufled_str[char]+=1
            else:
                shufled_str[char]=1

        for char in s:
            if char in shufled_str.keys():
                shufled_str[char]-=1

        output=""
        for char in shufled_str.keys():
            str_dub=shufled_str[char]
            while str_dub>0:
                output+=char
                str_dub-=1
        
        return output
