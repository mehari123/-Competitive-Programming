class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []
        # print(s)
        for st in s:

            # print(i,st)
            if not stack:
                
                stack.append([st,1])

            else:
                # print(stack[-1][0] ,st)
                if stack[-1][0] == st:

                    if stack[-1][1] + 1 == k:

                        stack.pop()

                    else:

                        stack[-1][1] += 1

                else:

                    stack.append([st,1])

            # print(stack)
        ans = ''.join(i[0] * i[1] for i in stack)
        return ans