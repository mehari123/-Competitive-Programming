class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs=='':
            return ''
        else:
            prefix=''
            leng=len(strs)
        
            for cur_index,cur_str in enumerate(strs[0]):
                for word in strs:
                    if len(word)-1<cur_index:
                        return prefix
                    elif word[cur_index]!=cur_str:
                        return prefix
                prefix+=cur_str
            return prefix
            