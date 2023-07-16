from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def bounded(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        def dfs(i, j):
            if not bounded(i, j) or (i, j) in visited:
                return

            visited.add((i, j))

            if board[i][j] == "M":
                board[i][j] = "X"
                return

            mines_count = 0
            di = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

            for d in di:
                ni, nj = i + d[0], j + d[1]
                if bounded(ni, nj) and board[ni][nj] == "M":
                    mines_count += 1

            if mines_count > 0:
                board[i][j] = str(mines_count)
            else:
                board[i][j] = "B"
                for d in di:
                    dfs(i + d[0], j + d[1])

        visited = set()
        dfs(click[0], click[1])
        return board