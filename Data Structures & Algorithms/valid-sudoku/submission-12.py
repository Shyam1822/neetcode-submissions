class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #28/8/26

        # for row
        for i in range(9):
            cur = board[i]
            for j in cur:
                if (j!='.') and (cur.count(j)>1):
                    return False
        
        # for col

        for i in range(9):
            cur=[]
            for j in range(9):
                cur.append(board[j][i])

            for k in cur:
                if (k!='.') and (cur.count(k)>1):
                    return False
                    
        # for box
        cur = [[] for _ in range(9)]
        for i in range(9):
            
            for j in range(9):

                if (board[i][j]!='.' and (board[i][j] in cur[(i//3)+(j//3)*3])):
                    return False
                cur[(i//3)+(j//3)*3].append(board[i][j])
        
        return True