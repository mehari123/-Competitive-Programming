class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def analyze_stretch(s: str) -> List[List]:
            stretches = []
            char = s[0]
            count = 1

            for i in range(1, len(s)):
                if s[i] == char:
                    count += 1
                else:
                    stretches.append([char, count])
                    char = s[i]
                    count = 1

            stretches.append([char, count])  # Add the last stretch
            return stretches

        s_stretch = analyze_stretch(s)
        expressive_count = 0

        for word in words:
            word_stretch = analyze_stretch(word)
            print("s stretch", s_stretch, "word stretch",word_stretch)
            if len(s_stretch) != len(word_stretch):
                continue

            stretchy = True
            for s_group, word_group in zip(s_stretch, word_stretch):
                if s_group[0] != word_group[0] or (s_group[1] < word_group[1]) or (word_group[1] != s_group[1] and s_group[1] < 3):
                    stretchy = False
                    break

            if stretchy:
                expressive_count += 1

        return expressive_count
        