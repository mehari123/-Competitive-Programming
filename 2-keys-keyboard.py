import math
class Solution:
    def minSteps(self, n: int) -> int:

        operation = [0 for i in range(n+1)]

        for j in range(2,n+1):

            if j % 2 == 0:

                operation[j] = operation[j//2] + 2

            elif j % 2 != 0:

                r = j // 2
                while r > 0:

                    if j % r == 0:

                        operation[j] = operation[r] + j // r
                        break
                    r -= 1
        print(operation)
        return operation[n]