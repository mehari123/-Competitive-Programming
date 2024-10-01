class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        len_word = len(word)
        len_sequence = len(sequence)
        dp = [0] *  (len_sequence + 1)

        for i in range(len_word,len_sequence + 1):

            if word == sequence[i-len_word:i]:

                dp[i] = dp[i-len_word] + 1

        return max(dp)

       

            


            

        