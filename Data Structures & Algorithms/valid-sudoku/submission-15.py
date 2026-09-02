class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #3/9/26

        for i in range(9):
            cur = board[i]
            cur_ele = []
            for j in cur:
                if (j!='.') and (j in cur_ele):
                    return False
                cur_ele.append(j)
        # column
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            cur_ele = []
            for j in col:
                if (j!='.') and (j in cur_ele):
                    return False
                cur_ele.append(j)

        # box
        box = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if (board[i][j]!=".") and (board[i][j] in box[(i//3)+(j//3)*3]):
                    return False
                box[(i//3)+((j//3)*3)].append(board[i][j])
        return True
            
                