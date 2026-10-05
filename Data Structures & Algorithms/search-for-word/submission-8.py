class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(word)
        row, col = len(board), len(board[0])

        def backtrack(index, r, c):
            if board[r][c] != word[index]:
                return False
            if index == l-1:
                return True

           

            temp = board[r][c]
            board[r][c] = '#'

            if r > 0:
                if backtrack(index + 1, r - 1, c):
                    board[r][c] = temp
                    return True

            if r < row - 1:
                if backtrack(index + 1, r + 1, c):
                    board[r][c] = temp
                    return True

            if c > 0:
                if backtrack(index + 1, r, c - 1):
                    board[r][c] = temp
                    return True

            if c < col - 1:
                if backtrack(index + 1, r, c + 1):
                    board[r][c] = temp
                    return True

            board[r][c] = temp
            return False

        for i in range(row):
            for j in range(col):
                if backtrack(0, i, j):
                    return True

        return False