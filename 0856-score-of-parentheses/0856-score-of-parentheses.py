class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        ans, bal = 0, 0
        for i, st in enumerate(s):
            bal = bal + 1 if st == "(" else bal - 1
            if i > 0 and s[i-1:i+1] == "()":
                ans += 1 << bal
        return ans
        