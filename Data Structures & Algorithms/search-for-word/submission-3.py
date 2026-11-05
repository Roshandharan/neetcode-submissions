class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        w = len(word)

        if row == 1 and col == 1:
            return board[0][0]==word

        def backtrack(pos, index):
            i,j = pos
            if index == w:
                return True
            if board[i][j]!=word[index]:
                return False
            
            char = board[i][j]
            board[i][j] = '#'

            for i_off, j_off in [(1,0),(0,1),(-1,0),(0,-1)]:
                r,c = i+i_off, j+j_off
                if 0<=r<row and 0<=c<col:
                    if backtrack((r,c), index+1):
                        return True
            board[i][j] = char
            return False
        
        for i in range(row):
            for j in range(col):
                if backtrack((i,j), 0):
                    return True
        
        return False