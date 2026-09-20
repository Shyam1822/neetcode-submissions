class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 17/9/26

        size = len(word)
        l, w = len(board), len(board[0])

        path = []
        row, col = 0, 0
        w_i = 0

        def backtrack(w_i, row, col):
            if w_i == size:
                return True

            if (
                row < 0
                or row == l
                or col < 0
                or col == w
                or (row, col) in path
                or board[row][col] != word[w_i]
            ):
                return False

            path.append((row, col))

            found = (
                backtrack(w_i+1, row + 1, col)
                or backtrack(w_i+1, row, col + 1)
                or backtrack(w_i+1, row - 1, col)
                or backtrack(w_i+1, row, col - 1)
            )

            path.remove((row,col))
            return found

        for r in range(l):
            for c in range(w):
                if backtrack(0, r, c):
                    return True

        return False
