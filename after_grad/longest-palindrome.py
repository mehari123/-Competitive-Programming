class Solution:
    def longestPalindrome(self, s: str) -> int:

        count_s = Counter(s)
        ans = 0
        ode_once = True
        one_once = True
        for key,val in count_s.items():

            if val > 1:

                if val % 2 == 0:

                    ans += val

                elif ode_once or one_once:

                    ans += val
                    ode_once = False
                    one_once = False
                else:

                    ans += val-1

            elif one_once:
                ans += 1
                one_once = False
                ode_once = False

        return ans if ans > 0  and len(s) > 0 else 1
            





        