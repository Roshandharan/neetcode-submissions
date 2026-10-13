class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return

        height = len(board)
        width = len(board[0])

        def dfs(r,c):
            if 0<=r<height and 0<=c<width and board[r][c]=='O':
                board[r][c] = 'C'
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r, c+1)
                dfs(r,c-1)        
        for r in [0, height-1]:
            for c in range(width):
                if board[r][c]=='O':
                    dfs(r,c)
        
        for c in [0, width -1]:
            for r in range(height):
                if board[r][c]=='O':
                    dfs(r,c)
        
        for r in range(height):
            for c in range(width):
                if board[r][c]=='C':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

        