class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # 23/9/26

        # initially started with cover and uncover logic, but proble is while uncovering, we could uncover squares that could be covered by pre placed queens before the current row

        # so the hack is for diagonals, split into two parts, negative and positive diagonals, r+c and r-c will be a constant for ny diagonal in a chess board, based on that we can identify the square is safe or not

        op = []
        cur = [["."] * n for _ in range(n)]
        # not cur = [["."*n]*n] creates the reference of the 1st list element in other elements, which leads to modification of one element -> modifying all which we dont want
        # print(cur)

        # col,posDia,negDia = [],[],[]

        # Note: Using Python set with add() and remove() is also much faster than doing in lookups on a list!

        col = set()
        posDia = set()  # (r - c)
        negDia = set()  # (r + c)

        def backtrack(row):
            if row == n:
                op.append(["".join(row) for row in cur])
                return
            for i in range(n):
                if (i not in col) and (row + i not in negDia) and (row - i not in posDia):
                    # col.append(i)
                    # negDia.append(row+i)
                    # posDia.append(row-i)

                    col.add(i)
                    posDia.add(row - i)
                    negDia.add(row + i)

                    cur[row][i] = "Q"
                    backtrack(row + 1)
                    cur[row][i] = "."
                    col.remove(i)
                    negDia.remove(row + i)
                    posDia.remove(row - i)

        backtrack(0)
        return op
