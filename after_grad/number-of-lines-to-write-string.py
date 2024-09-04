class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        p2 = 0
        sum1 = 0
        line_count = 1
        char_pixel = defaultdict(int)
        for i in range(26):

            char_pixel[chr(i+97)] = widths[i]

        while p2 <= len(s)-1:

            if sum1 + char_pixel[s[p2]] <= 100:

                sum1 += char_pixel[s[p2]]
            else:
                sum1 = char_pixel[s[p2]]
                line_count += 1
            
            p2 += 1

        return [line_count,sum1]

            


        