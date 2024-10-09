class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []
        
        def backtrack(start,path):

            if start == len(s):

                result.append(path)
                return

            for end in range(start+1,len(s) + 1):

                if s[start:end] == s[start:end][::-1]:

                    backtrack(end,path+[s[start:end]])

        backtrack(0,[])
        return result





    


        