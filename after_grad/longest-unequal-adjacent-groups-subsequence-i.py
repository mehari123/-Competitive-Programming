class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:


        prev = -1 
        ans = []

        for ind,g in enumerate(groups):

            # print(g,ind)
            if prev != g:
                ans.append(words[ind])
                prev = g
        
        return ans