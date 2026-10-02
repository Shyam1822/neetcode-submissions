class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # combine soln1's open close and soln2's backtrack to obtain best time

        op = []
        
        def backtrack(cur,op_c,cl_c):
            if op_c<cl_c or op_c>n:
                return
            
            if len(cur)==n*2:
                op.append("".join(cur))
                return
            
            cur.append('(')
            backtrack(cur,op_c+1,cl_c)
            cur.pop()
            cur.append(')')
            backtrack(cur,op_c,cl_c+1)
            cur.pop()
        
        backtrack([],0,0)
        return op

        
        