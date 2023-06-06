class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        memo = defaultdict(int)
        def find_min (i,row):


            if row == len(triangle):

                return 0

            if (i,row) in memo:

                return memo[(i,row)]
                
            min_ = triangle[row][i]
            if len(triangle[row]) > i:

                min_ += min(find_min(i,row+1),find_min(i+1,row+1))

            else:

                min_ = find_min(i,row+1)

            memo[(i,row)] = min_
            return min_

        return find_min(0,0)