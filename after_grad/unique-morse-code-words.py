class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha_morse = defaultdict(str)

        for i,ch in zip(range(26),morse):

            alpha_morse[chr(i+97)]= ch

        morse_words = []

        for word in words:

            mors = ''
            print(word)
            for w in word:

                mors += alpha_morse[w]
            # print(mors)
            morse_words.append(mors)
        # print(alpha_morse)
        # print(morse_words)
        return len(set(morse_words))
        