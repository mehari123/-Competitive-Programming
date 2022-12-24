class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapper={}
        for i in range(26):
            if i>=9:
                key=str(i+1)+"#"
                value=chr(i+96+1)
            else:
                key=str(i+1)
                value=chr(i+96+1)
            mapper[key]=value
        size=len(s)-1
        output=""
        while size>=0:
            if s[size]=="#":
                key=s[size-2] + s[size-1]+s[size]
                size-=3
            else:
                key=s[size]
                size-=1
            output+=mapper[key]
            output_reversed=output[::-1]
        return output_reversed
