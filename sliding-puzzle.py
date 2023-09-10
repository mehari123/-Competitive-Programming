from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        correct = [[1, 2, 3], [4, 5, 0]]
        board_tuple = tuple(board[0] + board[1])
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(board_tuple, 0)]) 
        visited = set()
        
        while queue:
            current_board, moves_count = queue.popleft()
            
            if current_board == tuple(correct[0] + correct[1]):
                return moves_count  

            empty_index = current_board.index(0)
            row, col = empty_index // 3, empty_index % 3
            
            
            for dr, dc in moves:
                new_row, new_col = row + dr, col + dc
                
                if 0 <= new_row < 2 and 0 <= new_col < 3:
                    new_board = list(current_board)
                    new_board[empty_index], new_board[new_row * 3 + new_col] = new_board[new_row * 3 + new_col], new_board[empty_index]
                    new_board_tuple = tuple(new_board)
                    
                    if new_board_tuple not in visited:
                        queue.append((new_board_tuple, moves_count + 1))
                        visited.add(new_board_tuple)
        
        return -1  # If no solution is found, return -1.