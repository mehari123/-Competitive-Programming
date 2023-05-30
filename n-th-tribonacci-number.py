class Solution:
    def tribonacci(self, n: int) -> int:

        tribi = {0:0,1:1,2:1}

        def tribo(n):

            if n == 0:

                return 0
            
            elif n == 1 or n == 2 :

                return 1

            tr1 = 0
            tr2 = 0
            tr3 = 0

            if n-1 not in tribi:

                tr1 = tribo(n-1)
            else:

                tr1 = tribi[n-1]

            if n-2 not in tribi:

                tr2 = tribo(n-2)
            else:

                tr2 = tribi[n-2]

            if n-3 not in tribi:

                tr3 = tribo(n-3)
            else:

                tr3 = tribi[n-3]

            tribi[n] = tr1 + tr2 + tr3
            return tribi[n]

        tribo(n)
        return tribi[n]